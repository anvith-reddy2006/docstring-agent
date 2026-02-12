import sys
from docstring_agent.agents import run_agent   # adjust if needed

def main():
    if len(sys.argv) != 3:
        print("Usage: docstring-agent input.py output.py")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    run_agent(input_file, output_file)

if __name__ == "__main__":
    main()

