# agents.py

import os
from tools import extract_entities, remove_existing_docstring, insert_docstring
from models import generate_docstring


class DocstringAgent:

    def process_file(self, input_path, output_path):

        with open(input_path, "r", encoding="utf-8") as f:
            code = f.read()

        code_lines = code.split("\n")

        entities = extract_entities(code)

        # CRITICAL: process bottom → top
        entities.sort(key=lambda x: x[2], reverse=True)

        for node, name, start, end, kind, parameters in entities:

            print(f"   → Generating docstring for {kind}: {name}")

            code_block = "\n".join(code_lines[start:end])

            docstring = generate_docstring(code_block, kind, parameters)

            code_lines, removed = remove_existing_docstring(code_lines, node)

            start -= removed

            code_lines = insert_docstring(code_lines, start, docstring)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(code_lines))

        print(f"✅ Documented → {output_path}")

    def process_folder(self, input_folder="app", output_folder="documented_app"):

        for root, _, files in os.walk(input_folder):
            for file in files:
                if file.endswith(".py"):
                    input_path = os.path.join(root, file)

                    relative_path = os.path.relpath(input_path, input_folder)
                    output_path = os.path.join(output_folder, relative_path)

                    print(f"\n📄 Processing: {input_path}")

                    self.process_file(input_path, output_path)

        print("\n🎉 All files documented!")
