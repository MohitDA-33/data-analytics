# AI-Assisted Software Development.

# Creating a gui based calculator using python and tkinter with the help of AI (chatgpt).

# tkinter- is a buit-in python library for creating GUIs. its a desktop app library.

import tkinter as tk   # tkinter as tk means we are creating an alias/shortform of tkinter, now if i write tk it will take it as tkinter.


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")   # Throught this you can change the title of the calculator.
        self.root.geometry("320x450")   # By this you can change the window size.
        self.root.resizable(False, False)   # If you write True then you can change the dimensions.
        self.root.configure(bg="#202124")   # # It will change the bg color of the calculator.

        self.expression = ""

        # -----------------------------
        # Display
        # -----------------------------
        self.display = tk.Entry(
            root,
            font=("Segoe UI", 28),   # Changes the font size of the displayed numbers.
            bg="#303134",
            fg="white",
            insertbackground="white",
            justify="right",
            bd=0,
            relief="flat"
        )
        self.display.pack(
            fill="both",
            padx=15,
            pady=(20, 15),
            ipady=15
        )

        # -----------------------------
        # Button area
        # -----------------------------
        button_frame = tk.Frame(root, bg="#202124")
        button_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        # Make rows/columns expand equally
        for row in range(5):
            button_frame.rowconfigure(row, weight=1)

        for col in range(4):
            button_frame.columnconfigure(col, weight=1)

        # -----------------------------
        # Calculator buttons
        # -----------------------------
        buttons = [
            ("C", 0, 0, self.clear),
            ("⌫", 0, 1, self.backspace),
            ("%", 0, 2, self.percentage),
            ("÷", 0, 3, lambda: self.add_operator("/")),

            ("7", 1, 0, lambda: self.add_number("7")),
            ("8", 1, 1, lambda: self.add_number("8")),
            ("9", 1, 2, lambda: self.add_number("9")),
            ("×", 1, 3, lambda: self.add_operator("*")),

            ("4", 2, 0, lambda: self.add_number("4")),
            ("5", 2, 1, lambda: self.add_number("5")),
            ("6", 2, 2, lambda: self.add_number("6")),
            ("−", 2, 3, lambda: self.add_operator("-")),

            ("1", 3, 0, lambda: self.add_number("1")),
            ("2", 3, 1, lambda: self.add_number("2")),
            ("3", 3, 2, lambda: self.add_number("3")),
            ("+", 3, 3, lambda: self.add_operator("+")),

            ("(", 4, 0, lambda: self.add_number("(")),
            ("0", 4, 1, lambda: self.add_number("0")),
            (")", 4, 2, lambda: self.add_number(")")),
            ("=", 4, 3, self.calculate),
        ]

        for text, row, column, command in buttons:
            self.create_button(
                button_frame,
                text,
                row,
                column,
                command
            )

        # -----------------------------
        # Keyboard support
        # -----------------------------
        self.root.bind("<Key>", self.keyboard_input)
        self.root.bind("<Return>", lambda event: self.calculate())
        self.root.bind("<KP_Enter>", lambda event: self.calculate())
        self.root.bind("<BackSpace>", lambda event: self.backspace())
        self.root.bind("<Escape>", lambda event: self.clear())

    # =========================================================
    # GUI
    # =========================================================

    def create_button(self, parent, text, row, column, command):
        """Create a calculator button."""

        if text == "=":
            bg = "#8ab4f8"
            fg = "#202124"
        elif text in ("+", "−", "×", "÷"):
            bg = "#3c4043"
            fg = "#8ab4f8"
        elif text in ("C", "⌫", "%"):
            bg = "#5f6368"
            fg = "white"
        else:
            bg = "#303134"
            fg = "white"

        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 18, "bold"),   # Changes the font size of the buttons.
            bg=bg,
            fg=fg,
            activebackground="#70757a",
            activeforeground="white",
            bd=0,
            relief="flat",
            cursor="hand2"
        )

        button.grid(
            row=row,
            column=column,
            sticky="nsew",   # This will change the buttons size automtically when you try to change the window size, you dont need to manually resize every button.
            padx=4,
            pady=4
        )

    # =========================================================
    # Calculator functions
    # =========================================================

    def add_number(self, value):
        """Add a number or parenthesis to the expression."""
        self.expression += value
        self.update_display()

    def add_operator(self, operator):
        """Add an arithmetic operator."""
        if not self.expression:
            # Allow a negative number at the beginning
            if operator == "-":
                self.expression = "-"
                self.update_display()
            return

        # Prevent two operators from appearing together
        if self.expression[-1] in "+-*/":
            self.expression = self.expression[:-1] + operator
        else:
            self.expression += operator

        self.update_display()

    def clear(self):
        """Clear the calculator."""
        self.expression = ""
        self.update_display()

    def backspace(self):
        """Remove the last character."""
        if self.expression:
            self.expression = self.expression[:-1]

        self.update_display()

    def percentage(self):
        """
        Convert the last number in the expression to a percentage.

        Example:
            50 -> 0.5
            200 + 10% -> 200 + 0.1
        """
        if not self.expression:
            return

        try:
            # Find the last number in the expression
            i = len(self.expression) - 1

            while i >= 0 and (
                self.expression[i].isdigit()
                or self.expression[i] == "."
            ):
                i -= 1

            start = i + 1

            if start < len(self.expression):
                number = self.expression[start:]

                if number:
                    percentage_value = float(number) / 100

                    # Keep integers looking clean
                    if percentage_value.is_integer():
                        replacement = str(int(percentage_value))
                    else:
                        replacement = str(percentage_value)

                    self.expression = (
                        self.expression[:start] + replacement
                    )

                    self.update_display()

        except ValueError:
            self.show_error()

    def calculate(self):
        """Evaluate the mathematical expression."""
        if not self.expression:
            return

        try:
            # Replace calculator-style symbols
            expression = self.expression.replace("×", "*")
            expression = expression.replace("÷", "/")
            expression = expression.replace("−", "-")

            # Only characters needed for basic arithmetic are allowed.
            # This prevents arbitrary Python code from being executed.
            allowed_characters = set(
                "0123456789+-*/(). "
            )

            if not all(
                character in allowed_characters
                for character in expression
            ):
                raise ValueError

            result = eval(
                expression,
                {"__builtins__": None},
                {}
            )

            # Handle invalid mathematical results
            if isinstance(result, complex):
                raise ValueError

            # Avoid displaying 10.0 instead of 10
            if isinstance(result, float) and result.is_integer():
                result = int(result)

            self.expression = str(result)
            self.update_display()

        except (ZeroDivisionError, ValueError, SyntaxError, TypeError):
            self.show_error()

    def show_error(self):
        """Display an error message."""
        self.display.delete(0, tk.END)
        self.display.insert(0, "Error")
        self.expression = ""

    def update_display(self):
        """Update the calculator display."""
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

        # Keep cursor at the end
        self.display.icursor(tk.END)

    # =========================================================
    # Keyboard input
    # =========================================================

    def keyboard_input(self, event):
        """Handle keyboard input."""

        key = event.char

        if key in "0123456789.":
            self.add_number(key)

        elif key in "+-*/":
            self.add_operator(key)

        elif key == "(":
            self.add_number("(")

        elif key == ")":
            self.add_number(")")

        elif key == "%":
            self.percentage()


# =============================================================
# Main program
# =============================================================

if __name__ == "__main__":
    root = tk.Tk()

    calculator = Calculator(root)

    root.mainloop()


# Note: Here i used chatgpt to write the code, if i am not able to understand any part i can just copy that part of the code and paste it chatgpt it will help me make understand.