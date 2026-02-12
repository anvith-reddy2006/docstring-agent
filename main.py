import sys
from models import process_file

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python -m docstring-agent input.py output.py")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_file(input_file, output_file)

