import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

window = tk.Tk()
window.title("Simple Calculator")
window.configure(bg="#282C34")

entry = tk.Entry(width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for button in buttons:
    button = tk.Button(window, text=button, padx=40, pady=20, command=lambda b=button: button_click(b))
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

button_clear = tk.Button(window, text="Clear", padx=79, pady=20, command=button_clear)
button_clear.grid(row=4, column=0, columnspan=2)

button_equal = tk.Button(window, text="=", padx=81, pady=20, command=button_equal)
button_equal.grid(row=4, column=2)

window.mainloop()