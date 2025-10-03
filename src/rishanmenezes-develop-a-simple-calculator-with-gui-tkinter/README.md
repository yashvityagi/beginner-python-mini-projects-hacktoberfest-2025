# Simple Calculator with GUI (Tkinter)

A beginner-friendly desktop calculator built with Python's Tkinter.

Features
- Basic arithmetic: addition, subtraction, multiplication, division
- Modulo (%) and power (**) via typing
- Decimal support
- Clear, backspace, and safe expression evaluation

How to run

1. Make sure you have Python 3.8+ installed.
2. From the project folder run:

```powershell
python calculator.py
```

The calculator window will open.

Notes
- This project intentionally avoids eval() and uses Python's ast module to safely evaluate numeric expressions.
- No external dependencies are required — Tkinter is included with standard Python distributions on most platforms.

Optional sample

Type 12+3*4 and press = to see 24.
