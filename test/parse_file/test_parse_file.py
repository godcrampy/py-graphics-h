from src.parse_file import get_ast


def test_ast():
    ast = get_ast("test/parse_file/main.c")
    assert isinstance(ast, dict)  # returns a dictionary
    assert ast["_nodetype"] == "FileAST"  # returns AST for file
    nodes = ast["ext"]
    assert isinstance(nodes, list)
    assert nodes[0]["_nodetype"] == "FuncDef"
    assert nodes[0]["decl"]["name"] == "foo"
    assert nodes[1]["_nodetype"] == "FuncDef"
    assert nodes[1]["decl"]["name"] == "main"
