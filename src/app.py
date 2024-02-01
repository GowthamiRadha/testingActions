import tkinter as tk
from tkinter import messagebox

# Function to safely evaluate the expression
def safe_eval(expression):
    try:
        # Evaluate the expression within the safe restricted globals.
        return eval(expression, {"__builtins__": {}}, {})
    except Exception as e:
        messagebox.showerror("Error", "Invalid expression entered.")
        return None

# The main Calculator class
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.expression = ""

        self.screen = tk.Entry(master, state='normal', width=30, bg="yellow", fg="blue", justify='right')
        self.screen.grid(row=0, column=0, columnspan=4, pady=5)
        self.screen.configure(state='readonly')

        # Initialize the interface with all buttons
        self.initialize_interface()

    def initialize_interface(self):
        # Buttons layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '.', '+'
        ]

        # Create and position buttons
        for index, label in enumerate(buttons):
            button = tk.Button(self.master, text=label, command=lambda l=label: self.click(l))
            row, col = divmod(index, 4)
            button.grid(row=row+1, column=col, sticky="nsew", padx=1, pady=1)

        # Add equal and backspace button separately to customize their behavior
        equals_button = tk.Button(self.master, text='=', command=self.evaluate)
        backspace_button = tk.Button(self.master, text='\u232B', command=self.backspace)  # Unicode for backspace symbol
        equals_button.grid(row=5, column=2, columnspan=2, sticky="nsew", padx=1, pady=1)
        backspace_button.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=1, pady=1)
    
    def click(self, text):
        current = self.screen.get()
        if text == '=':
            self.evaluate()
        else:
            self.update_screen(current + text)

    def clear(self):
        self.update_screen("")

    def backspace(self):
        self.update_screen(self.screen.get()[:-1])

    def evaluate(self):
        expression = self.screen.get()
        result = safe_eval(expression)
        if result is not None:
            self.update_screen(str(result))

    # Function to update the content of the screen
    def update_screen(self, content):
        self.screen.config(state='normal')
        self.screen.delete(0, tk.END)
        self.screen.insert(tk.END, content)
        self.screen.config(state='readonly')

# Main loop
if __name__ == '__main__':
    root = tk.Tk()
    my_calculator = Calculator(root)

    # Configure button grid proportions
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
    for i in range(1, 6):
        root.grid_rowconfigure(i, weight=1)

    root.mainloop()
