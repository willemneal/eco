class URI(object):
    def __init__(self):
        self.kind = ""
        self.path = []
        self.name = ""
        self.ruleid = ""
        self.index = -1

    def __repr__(self):
        path = []
        for p in self.path:
            path.append(repr(p))
        return "URI(%s:%s,\"%s\",%s)" % (self.kind, ",".join(path), self.name, self.index)

class Reference(object):
    def __init__(self, kind, name, nbrule=None):
        self.kind = kind
        self.name = name
        self.nbrule = nbrule

    def __eq__(self, other):
        return self.kind == other.kind and self.name == other.name

    def __repr__(self):
        return "Ref(%s/%s)" % (self.kind, self.name)

class AstAnalyser(object):
    def __init__(self, filename):
        self.errors = {}
        self.scope = None

        self.d = {}

        self.data = {}
        self.index = 0

        rootnode = self.load_nb_file(filename)
        self.definitions = RuleReader().read(rootnode)

    def load_nb_file(self, filename):
        from jsonmanager import JsonManager
        from grammar_parser.bootstrap import BootstrapParser
        from grammars.grammars import lang_dict

        manager = JsonManager(unescape=True)

        # load nb file
        root, language, whitespaces = manager.load(filename)[0]

        # load scoping grammar
        grammar = lang_dict[language]
        parser, lexer = grammar.load()
        parser.previous_version.parent = root
        parser.reparse()
        return parser.previous_version.parent

    def has_var(self, name):
        return False

    def get_field(self, ref):
        return None

    def get_definition(self, nodename):
        for d in self.definitions:
            if d.name == nodename:
                return d

    def scan(self, node, path):
        if node is None:
            return

        if node.__dict__.has_key('alternate') and node.alternate:
            node = node.alternate

        from grammar_parser.bootstrap import AstNode, ListNode

        if isinstance(node, AstNode):
            base = None
            nbrule = self.get_definition(node.symbol.name)
            uris = []
            if nbrule:
                _type = nbrule.get_type() # class, method, reference, etc (as declared in nb-file)
                name = node.get(nbrule.get_name())

                if isinstance(name, ListNode):
                    names = name.children
                else:
                    names = [name]

                scoped_path = list(path)
                if not nbrule.is_reference():
                    if scoped_path != [] and not self.scopes(scoped_path[-1], _type): #XXX should be while?
                        # if last parent hasn't scope, delete from path
                        scoped_path.pop(-1)

                for n in names:
                    uri = URI()
                    if n is None:
                        uri.name = None
                    else:
                        uri.name = n.symbol.name
                    uri.kind = _type
                    uri.path = scoped_path
                    uri.nbrule = nbrule
                    uri.node = n
                    uri.vartype = node.get('type') # XXX needs to be defined by autocomplete rules
                    uri.astnode = node

                    visibility = nbrule.get_visibility()
                    if visibility not in ['surrounding','subsequent']:
                        # URI has a base
                        base = node.get(visibility)
                        base_uri = self.scan(base, path)
                        path = [base_uri]
                        uri.path = path

                    # add this uri to the path of its children
                    path = list(path)
                    path.append(Reference(_type, uri.name, nbrule))

                    uris.append(uri)

            # scan ASTNodes children
            for c in node.children:
                if node.children[c] is base:
                    continue # don't scan base twice
                self.scan(node.children[c], path)

            # set index AFTER children have been scanned: XXX not correct. int x = x needs to be treated extra
            uri = None
            for uri in uris:
                uri.index = self.index
                self.data.setdefault(uri.kind, [])
                self.data[uri.kind].append(uri)
                self.index += 1

            return uri # only needed for base

        else:
            for c in node.children:
                self.scan(c, path)
            return

    def analyse(self, node):
        # scan
        self.errors = {}

        self.data.clear()
        self.index = 0
        self.scan(node, [])
        self.analyse_refs()

    def analyse_refs(self):
        for key in self.data:
            nbrule = self.data[key][0].nbrule
            if nbrule.is_reference():
                obj = self.data[key]
                for reference in self.data[key]:
                    self.find_reference(reference)

    def find_reference(self, reference):
        for refers in reference.nbrule.get_references()[0]:

            # global variable
            if len(reference.path) == 0:
                x = self.get_reference(refers, reference.path, reference.name)
                if x:
                    return x

            # iteratate through path prefixes
            path = list(reference.path)
            while len(path) > 0:
                x = self.get_reference(refers, path, reference.name)
                if x:
                    if x.nbrule.get_visibility() != "subsequent":
                        return x
                    if x.nbrule.get_visibility() == "subsequent" and x.index < reference.index:
                        return x
                path.pop() # try with prefix of path

        # URI is alias (nested URIs)
        # evaluate references, then get_reference
        if len(reference.path) > 0 and isinstance(reference.path[0], URI):
            x = self.find_reference(reference.path[0])
            if x:
                for refers in reference.nbrule.get_references()[0]:
                    z = self.get_reference(refers, x.path + [Reference(x.kind, x.name)], reference.name)
                    if z:
                        return z

        self.errors[reference.node] = "'%s' cannot be resolved to a variable." % (reference.name)

    def get_reference(self, kind, path, name):
        if not self.data.has_key(kind):
            return None
        for candidate in self.data[kind]:
            if candidate.name != name:
                continue
            if not self.paths_eq(candidate.path, path):
                continue
            return candidate
        return None

    def paths_eq(self, path1, path2):
        if len(path1) != len(path2):
            return False
        for i in range(len(path1)):
            if path1[i].name != path2[i].name:
                return False
            if path1[i].kind != path2[i].kind: #XXX only if types matter (e.g. python doesn't care)
                return False
        return True

    def scopes(self, scope, _type):
        return _type in scope.nbrule.get_scopes()

    def has_error(self, node):
        return self.errors.has_key(node)

    def get_error(self, node):
        try:
            return self.errors[node]
        except KeyError:
            return ""

    def get_completion(self, scope):
        # find astnode with rule
        astnode = self.get_correct_astnode(scope)
        if not astnode:
            return []
        nbrule = self.get_definition(astnode.symbol.name)
        name = astnode.get(nbrule.get_name())

        uri = self.find_uri_by_astnode(name)
        if uri:
            path = uri.path + [uri]
            names = self.get_reachable_names_by_path(path)
            if scope.lookup in ["NAME","nonterminal","IDENTIFIER"]: #XXX this needs to be provided by the grammar
                filtered_names = []
                for uri in names:
                    if uri.name.startswith(scope.symbol.name):
                        filtered_names.append(uri)
                return filtered_names
            return names

    def get_correct_astnode(self, scope):
        # returns the correct astnode for a corresponding scope. Is needed for
        # nested astnodes that have rules, e.g. blocks inside methods
        while scope is not None:
            astnode = scope.alternate
            if astnode:
                nbrule = self.get_definition(scope.alternate.symbol.name)
                # astnode must have a corresponding entry in self.data
                if nbrule and self.data.has_key(nbrule.get_type()):
                    for e in self.data[nbrule.get_type()]:
                        if e.astnode is astnode:
                            return astnode
            scope = scope.parent

    def find_uri_by_astnode(self, node):
        for key in self.data:
            for uri in self.data[key]:
                if uri.node == node:
                    return uri
        return None

    def get_reachable_names_by_path(self, path):
        names = []
        path = list(path)   # copy to not manipulate existing path
        while path != []:
            for key in self.data:
                if key in ["reference", "block"]: #XXX needs to be supplied by codecompletion rules
                    continue
                for uri in self.data[key]:
                    if uri.path == path:
                        names.append(uri)
            path.pop()
        return names

class RuleReader(object):
    def read(self, root):
        definitions = root.children[1].children[1].alternate
        l = self.read_definitions(definitions)
        return l

    def read_definitions(self, definitions):
        l = []
        for definition in definitions.children:
            name = definition.get("name").symbol.name
            params = self.read_names(definition.get('args'))
            options = self.read_options(definition.get('options'))
            l.append(NBRule(name, params, options))
        return l

    def read_names(self, node):
        l = []
        if node:
            for n in node.children:
                l.append(n.symbol.name)
        return l

    def read_options(self, options):
        d = {}
        for option in options.children:
            if option.symbol.name == "Defines":
                d['defines'] = (option.get('type').symbol.name, option.get('name').symbol.name) # Class(name): defines class name
                scope = option.get('scope')
                if scope:
                    d['in'] = scope.symbol.name
            elif option.symbol.name == "Scopes":
                d['scopes'] = self.read_names(option.get('types'))
            elif option.symbol.name == "References":
                d['references'] = (self.read_names(option.get('types')), option.get('name').symbol.name) # Lookup(name): references field, variable name
                scope = option.get('scope')
                if scope:
                    d['in'] = scope.symbol.name
        return d

class NBRule(object):
    def __init__(self, name, params, options):
        self.name = name
        self.params = params
        self.options = options

    def is_definition(self):
        return self.options.has_key('defines')

    def is_reference(self):
        return self.options.has_key('references')

    def get_scopes(self):
        if self.options.has_key('scopes'):
            return self.options['scopes']
        return []

    def get_references(self):
        if self.options.has_key('references'):
            return self.options['references']
        return []

    def get_definition(self):
        if self.options.has_key('defines'):
            return self.options['defines']
        return None

    def get_visibility(self):
        if self.options.has_key('in'):
            return self.options['in']
        return "surrounding"

    def get_in(self):
        if self.options.has_key('in'):
            return self.options['in']
        return None

    def get_type(self):
        if self.is_reference():
            return "reference"
        elif self.is_definition():
            return self.options['defines'][0]
        return None

    def get_name(self):
        if self.is_reference():
            return self.options['references'][1]
        elif self.is_definition():
            return self.options['defines'][1]
        return None

    def __repr__(self):
        return "NBRule(%s, %s, %s)" % (self.name, self.params, self.options)