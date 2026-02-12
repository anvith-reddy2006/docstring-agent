import ast
from tools import generate_docstring


class DocstringGenerator(ast.NodeTransformer):

    def visit_FunctionDef(self, node):
        if ast.get_docstring(node) is None:
            code = ast.unparse(node)
            doc = generate_docstring(code, "function")
            node.body.insert(0, ast.Expr(value=ast.Constant(value=doc)))
        return node

    def visit_ClassDef(self, node):
        if ast.get_docstring(node) is None:
            code = ast.unparse(node)
            doc = generate_docstring(code, "class")
            node.body.insert(0, ast.Expr(value=ast.Constant(value=doc)))
        self.generic_visit(node)
        return node
