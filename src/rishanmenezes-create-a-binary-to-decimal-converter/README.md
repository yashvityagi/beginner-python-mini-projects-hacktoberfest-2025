# Binary to Decimal Converter

Tiny, beginner-friendly Python project that converts binary strings (for example `1011`) to decimal integers.

How to run

There are two simple ways to run this project.

- Option 1 — Run the CLI (recommended for beginners):

  1. Open PowerShell and change into the project folder:

  ```powershell
  cd .\src\rishanmenezes-create-a-binary-to-decimal-converter
  ```

  2. Run the CLI:

  ```powershell
  python cli.py
  ```

  Then type binary numbers (for example `1011`) and press Enter. Type `exit` or Ctrl+C to quit.

- Option 2 — One-liner import (run from the project folder):

  ```powershell
  cd .\src\rishanmenezes-create-a-binary-to-decimal-converter
  python -c "from converter import binary_to_decimal; print(binary_to_decimal('1011'))"
  ```

Notes about imports

- The folder name contains hyphens which are not valid Python module names. For simple usage run the examples from inside the project folder. If you want to import the package from elsewhere, rename the folder to a valid Python identifier (use underscores) or add the folder to PYTHONPATH.

Requirements

- No external dependencies required. See `requirements.txt`.

Sample output

```
Binary to Decimal Converter (type 'exit' to quit)
Enter a binary number: 1011
Decimal: 11
Enter a binary number: 100100
Decimal: 36
Enter a binary number: exit
Goodbye!
```
