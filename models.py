# models.py

from config import client, MODEL_NAME


def clean_output(text: str) -> str:
    lines = [line.rstrip() for line in text.split("\n") if line.strip()]

    cleaned = []
    skip_block = False

    for line in lines:
        stripped = line.strip()

        # Remove forbidden content
        if any(word in stripped for word in ["Code:", "Function:", "Class:", "def ", "class "]):
            continue

        # Remove Args: None
        if stripped.startswith("Args:"):
            cleaned.append("Args:")
            skip_block = True
            continue

        if skip_block:
            if stripped == "None":
                cleaned.pop()
                skip_block = False
                continue
            if line.startswith("    "):
                cleaned.append(line)
                continue
            else:
                skip_block = False

        # Remove Returns: None
        if stripped.startswith("Returns:"):
            cleaned.append("Returns:")
            continue

        if stripped == "None" and cleaned and cleaned[-1] == "Returns:":
            cleaned.pop()
            continue

        cleaned.append(line)

    return "\n".join(cleaned).strip()


def generate_docstring(code_block: str, kind: str, parameters: list) -> str:

    if kind == "class":
        specific_rules = """
- Write a short summary of what the class represents.
- Do NOT describe constructor parameters.
- Do NOT include Args unless explicitly required.
- Do NOT include Returns.
"""
    else:
        specific_rules = """
- If no parameters, do NOT include Args.
- If no return statement exists, do NOT include Returns.
"""

    prompt = f"""
Write a concise Google-style Python docstring.

STRICT RULES:
- Describe ONLY what exists in the code.
- Do NOT invent behavior.
- If body is only 'pass', write: "Placeholder function." or "Empty class."
- Do NOT include code.
- Do NOT include triple quotes.
{specific_rules}

FORMAT:

Summary line.

Args:
    param_name (type): description

Returns:
    type: description

Here is the code:
{code_block}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
    )

    raw = response.choices[0].message.content.strip()

    return clean_output(raw)
