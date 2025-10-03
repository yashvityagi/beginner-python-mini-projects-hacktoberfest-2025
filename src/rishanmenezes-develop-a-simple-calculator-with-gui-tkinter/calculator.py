import tkinter as tk
from tkinter import messagebox
import ast


def safe_eval(expr: str):
    """Evaluate a math expression safely using AST.

    Supports numbers, + - * / % ** and unary +/-. Raises ValueError for unsafe nodes.
    """
    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Only numeric constants are allowed")
        if isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op = node.op
            if isinstance(op, ast.Add):
                return left + right
            if isinstance(op, ast.Sub):
                return left - right
            if isinstance(op, ast.Mult):
                return left * right
            if isinstance(op, ast.Div):
                return left / right
            if isinstance(op, ast.Mod):
                return left % right
            if isinstance(op, ast.Pow):
                return left ** right
            if isinstance(op, ast.FloorDiv):
                return left // right
            raise ValueError("Unsupported binary operator")
        if isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            if isinstance(node.op, ast.UAdd):
                return +operand
            if isinstance(node.op, ast.USub):
                return -operand
            raise ValueError("Unsupported unary operator")
        # allow parentheses (represented as nested expressions)
        raise ValueError(f"Unsupported expression: {type(node).__name__}")

    parsed = ast.parse(expr, mode="eval")
    return _eval(parsed)


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.resizable(False, False)
        self._build_ui()

    def _build_ui(self):
        self.display_var = tk.StringVar()
        entry = tk.Entry(self, textvariable=self.display_var, font=("Consolas", 20), bd=5, relief=tk.RIDGE, justify=tk.RIGHT)
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('%', 4, 2), ('+', 4, 3),
        ]

        for (text, r, c) in buttons:
            b = tk.Button(self, text=text, width=5, height=2, font=("Consolas", 14),
                          command=lambda t=text: self._on_button(t))
            b.grid(row=r, column=c, padx=3, pady=3)

        clear_btn = tk.Button(self, text='C', width=5, height=2, font=("Consolas", 14), command=self._clear)
        clear_btn.grid(row=5, column=0, padx=3, pady=3)

        back_btn = tk.Button(self, text='⌫', width=5, height=2, font=("Consolas", 14), command=self._backspace)
        back_btn.grid(row=5, column=1, padx=3, pady=3)

        eq_btn = tk.Button(self, text='=', width=11, height=2, font=("Consolas", 14), command=self._calculate)
        eq_btn.grid(row=5, column=2, columnspan=2, padx=3, pady=3)

    def _on_button(self, char):
        current = self.display_var.get()
        self.display_var.set(current + char)

    def _clear(self):
        self.display_var.set("")

    def _backspace(self):
        current = self.display_var.get()
        self.display_var.set(current[:-1])

    def _calculate(self):
        expr = self.display_var.get()
        if not expr.strip():
            return
        try:
            result = safe_eval(expr)
            # Normalize integer results to int
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.display_var.set(str(result))
        except Exception as e:
            messagebox.showerror("Error", f"Invalid expression:\n{e}")


if __name__ == '__main__':
    app = Calculator()
    app.mainloop()
