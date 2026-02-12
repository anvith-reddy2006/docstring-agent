import ast
from .tools import generate_docstring

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

def process_file(input_path, output_path):
    with open(input_path, "r") as f:
        source_code = f.read()

    tree = ast.parse(source_code)

    transformer = DocstringGenerator()
    modified_tree = transformer.visit(tree)
    ast.fix_missing_locations(modified_tree)

    new_code = ast.unparse(modified_tree)

    with open(output_path, "w") as f:
        f.write(new_code)

    print(f"Docstrings added successfully to {output_path}")
