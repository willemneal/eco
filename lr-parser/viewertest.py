from viewer import Viewer

grammar = """
    E ::= E "+" T
        | T
    T ::= T "*" P
        | P
    P ::= "1" | "2"
"""

Viewer("pydot").show_ast(grammar, "1 * 2")
Viewer("pydot").show_graph(grammar)
