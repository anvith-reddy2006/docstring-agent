# tools.py

import ast


def extract_entities(code: str):
    tree = ast.parse(code)

    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            child.parent = parent

    entities = []

    for node in ast.walk(tree):

        # ---------- CLASSES ----------
        if isinstance(node, ast.ClassDef):

            entities.append((
                node,
                node.name,
                node.lineno - 1,
                node.end_lineno,
                "class",
                []
            ))

        # ---------- FUNCTIONS ----------
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):

            if not isinstance(node.parent, (ast.Module, ast.ClassDef)):
                continue

            # Skip magic methods INCLUDING __init__
            if node.name.startswith("__") and node.name.endswith("__"):
                continue

            is_async = isinstance(node, ast.AsyncFunctionDef)

            if isinstance(node.parent, ast.ClassDef):
                kind = "async method" if is_async else "method"
            else:
                kind = "async function" if is_async else "function"

            parameters = [arg.arg for arg in node.args.args]

            if parameters and parameters[0] == "self":
                parameters = parameters[1:]

            entities.append((
                node,
                node.name,
                node.lineno - 1,
                node.end_lineno,
                kind,
                parameters
            ))

    return entities


# ---------- FIX 1: Expand one-liner safely ----------

def expand_one_liner(code_lines, start_line):
    line = code_lines[start_line]

    if ":" in line and " return " in line:
        header, body = line.split(":", 1)
        indent = len(header) - len(header.lstrip())

        code_lines[start_line] = header + ":"
        code_lines.insert(
            start_line + 1,
            " " * (indent + 4) + body.strip()
        )

    return code_lines


def remove_existing_docstring(code_lines, node):

    if not node.body:
        return code_lines, 0

    first_stmt = node.body[0]

    if (
        isinstance(first_stmt, ast.Expr)
        and isinstance(first_stmt.value, ast.Constant)
        and isinstance(first_stmt.value.value, str)
    ):
        start = first_stmt.lineno - 1
        end = first_stmt.end_lineno

        removed = end - start
        new_lines = code_lines[:start] + code_lines[end:]

        return new_lines, removed

    return code_lines, 0


def insert_docstring(code_lines, start_line, docstring):

    # 🔥 Expand one-liner before inserting
    code_lines = expand_one_liner(code_lines, start_line)

    indent = len(code_lines[start_line]) - len(code_lines[start_line].lstrip())
    inner_indent = " " * (indent + 4)

    lines = [line.rstrip() for line in docstring.split("\n") if line.strip()]

    formatted = [
        f'{inner_indent}"""',
        *[f"{inner_indent}{line}" for line in lines],
        f'{inner_indent}"""',
    ]

    return code_lines[:start_line + 1] + formatted + code_lines[start_line + 1:]
