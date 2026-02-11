import os
import openai
import ast
openai.api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client = OpenAI()

def generate_docstring(code_snippet, obj_type):
    return f"""Auto-generated docstring for {obj_type}.

Description:
    This {obj_type} was analyzed automatically.

Parameters:
    Extracted from signature.

Returns:
    Depends on implementation.
"""


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


def process_file(input_file, output_file):
    with open(input_file, "r") as f:
        source = f.read()

    tree = ast.parse(source)
    transformer = DocstringGenerator()
    updated_tree = transformer.visit(tree)

    new_code = ast.unparse(updated_tree)

    with open(output_file, "w") as f:
        f.write(new_code)


process_file("input.py", "output.py")
