import ast
from agents import DocstringGenerator


def process_file(input_file, output_file):
    with open(input_file, "r") as f:
        source = f.read()

    tree = ast.parse(source)

    transformer = DocstringGenerator()
    updated_tree = transformer.visit(tree)

    new_code = ast.unparse(updated_tree)

    with open(output_file, "w") as f:
        f.write(new_code)
