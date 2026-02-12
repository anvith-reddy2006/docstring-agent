# 🤖 AI Docstring Generator

Automatically generates **Google-style docstrings** for Python code
using **AST parsing** and **LLM analysis**.

------------------------------------------------------------------------

## 🚀 Quick Start

### 1️⃣ Setup Virtual Environment (Recommended)

``` bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

> For macOS/Linux:

``` bash
source venv/bin/activate
```

------------------------------------------------------------------------

### 2️⃣ Run the Application

``` bash
python quick_run.py
```

------------------------------------------------------------------------

### 3️⃣ Check Results

-   📂 Input files → `app/`
-   📂 Output files → `documented_app/` (with generated docstrings)

------------------------------------------------------------------------

## 📁 Project Structure

    doc/
    ├── app/                  # Input Python files
    ├── documented_app/       # Output files with generated docstrings
    ├── venv/                 # Virtual environment (optional)
    ├── quick_run.py          # Main runner (sets API key automatically)
    ├── config.py             # API configuration
    ├── models.py             # LLM interaction layer
    ├── tools.py              # AST parsing & docstring insertion
    ├── agents.py             # Core processing logic
    └── requirements.txt      # Project dependencies

------------------------------------------------------------------------

## ✨ Features

-   🔍 **Smart Analysis** -- Uses AST parsing for accurate code
    structure detection
-   📝 **Google-Style Docstrings** -- Clean and standardized
    documentation format
-   🛡 **Safe Processing** -- Reverse-order insertion prevents code
    corruption
-   📂 **Batch Processing** -- Recursively processes entire folders
-   ⚠ **Error Handling** -- Safely skips invalid or broken files
-   ⚡ **Automatic API Setup** -- GROQ API key handled in `quick_run.py`

------------------------------------------------------------------------

## ⚙️ How It Works

1.  **Parse** Python files using AST
2.  **Extract** functions, classes, methods, and parameters
3.  **Generate** docstrings using the GROQ LLM
4.  **Insert** docstrings safely into the original source code
5.  **Save** documented files to the output directory

------------------------------------------------------------------------

## ✅ Supported Elements

-   Functions
-   Async Functions
-   Classes
-   Class Methods
-   Property Methods
-   One-line Functions (auto-expanded)
-   Nested Folder Structures

------------------------------------------------------------------------

## 📌 Requirements

-   Python 3.7+
-   Internet connection (required for GROQ API)
-   Valid GROQ API key (configured in `quick_run.py`)

------------------------------------------------------------------------

## 🛠 Troubleshooting

### ❌ Import Errors

``` bash
venv\Scripts\activate
pip install -r requirements.txt
```

Make sure the virtual environment is activated.

------------------------------------------------------------------------

### ❌ No Output Generated

-   Ensure Python files exist inside the `app/` directory
-   Verify that files contain valid Python syntax
-   Check for errors in the terminal output

------------------------------------------------------------------------

### ❌ API Connection Problems

-   Confirm internet connectivity
-   Ensure the GROQ API key is valid
-   Verify the API key is correctly set in `quick_run.py`

------------------------------------------------------------------------

## 🎯 Example

### Input (`app/example.py`)

``` python
def add(a, b):
    return a + b
```

### Output (`documented_app/example.py`)

``` python
def add(a, b):
    """Adds two numbers together.

    Args:
        a: First number to add.
        b: Second number to add.

    Returns:
        The sum of a and b.
    """
    return a + b
```
