import tkinter as tk
from math import sin, cos, tan, log, sqrt, pi, e

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Научный калькулятор")
        self.root.geometry("380x380")

        # Поле для ввода
        self.input_field = tk.Entry(root, font=("Arial", 20), justify="right")
        self.input_field.grid(row=0, column=0, columnspan=5, sticky="we")
        # Кнопки
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("C", 1, 4),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("sqrt", 2, 4),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("log", 3, 4),
            ("0", 4, 0),
            (".", 4, 1),
            ("^", 4, 2),
            ("+", 4, 3),
            ("=", 4, 4),
            ("sin", 5, 0),
            ("cos", 5, 1),
            ("tan", 5, 2),
            ("pi", 5, 3),
            ("e", 5, 4),
        ]

        for text, row, col in buttons:
            tk.Button(
                self.root,
                text=text,
                font=("Arial", 18),
                bd=5,
                command=lambda t=text: self.on_button_click(t),
            ).grid(row=row, column=col, sticky="we", padx=5, pady=5)
    
    def on_button_click(self, char):
        if char == "C":
            self.input_field.delete(0, tk.END)
        elif char == "=":
            self.calculate()
        elif char == "pi":
            self.input_field.insert(tk.END, str(pi))
        elif char == "e":
            self.input_field.insert(tk.END, str(e))
        else:
            self.input_field.insert(tk.END, char)
  