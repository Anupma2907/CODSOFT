import tkinter as tk

# Core functions
def click(value):
    entry_field.insert(tk.END, str(value))

def clear():
    entry_field.delete(0, tk.END)
    history_label.config(text="")

def backspace():
    entry_field.delete(len(entry_field.get()) - 1)

def dot():
    entry_field.insert(tk.END, ".")

def equal():
    try:
        expression = entry_field.get().replace('x', '*').replace('÷', '/')
        result = eval(expression)
        history_label.config(text=entry_field.get())
        entry_field.delete(0, tk.END)
        entry_field.insert(0, result)
    except:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, "Error")

# Main app window
app = tk.Tk()
app.title("Calculator")
app.configure(bg="black")

# Entry field
entry_field = tk.Entry(app, width=25, justify="right", font=("Arial", 18), borderwidth=5, bg="black", fg="white")
entry_field.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# History label
history_label = tk.Label(app, text="", bg="black", fg="gray", anchor="e", font=("Arial", 10))
history_label.grid(row=0, column=0, columnspan=4, sticky="we")

# Buttons: text and command pairs
buttons = [
    ('AC', clear), ('⌫', backspace), ('+/-', lambda: click('-')), ('÷', lambda: click('÷')),
    ('7', lambda: click(7)), ('8', lambda: click(8)), ('9', lambda: click(9)), ('x', lambda: click('x')),
    ('4', lambda: click(4)), ('5', lambda: click(5)), ('6', lambda: click(6)), ('-', lambda: click('-')),
    ('1', lambda: click(1)), ('2', lambda: click(2)), ('3', lambda: click(3)), ('+', lambda: click('+')),
    ('%', lambda: click('%')), ('0', lambda: click(0)), ('.', dot), ('=', equal),
]

# Place buttons in grid
row = 2
col = 0
for (text, cmd) in buttons:
    btn = tk.Button(app, text=text, width=7, height=2, font=("Arial", 12), command=cmd,
                    bg="#2E2B3A" if text not in ['AC', '=', '⌫'] else "#5A4E7C", fg="white")
    
    btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Optional: Expandable/responsive layout
for i in range(6):
    app.grid_rowconfigure(i, weight=1)
for j in range(4):
    app.grid_columnconfigure(j, weight=1)

app.mainloop()
