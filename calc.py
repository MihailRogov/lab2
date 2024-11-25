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