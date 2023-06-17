import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)
    entry.insert(0, f'{expression} = ')


window = tk.Tk()
window.title("Calculator")
window.configure(bg="#f2defa")

entry = tk.Entry(width=50, bg='#F5F5F8',font=("Arial", 20),justify='center')
entry.grid(row=0, column=0, columnspan=5, padx=50, pady=40,ipady=40)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.',  '00', '+' ]

row = 1
col = 0
for button in buttons:
    btn = tk.Button(window,bg="#DAF7A6", text=button, width=10, font=("Arial", 15), command=lambda x=button: button_click(x))
    btn.grid(row=row, column=col, padx=10, pady=10)
    col += 1
    if col > 3:
        col = 0
        row += 1

clear_button = tk.Button(window,bg="#DAF7A6", text="C", width=10, font=("Arial", 15), command=button_clear)
clear_button.grid(row=row, column=col, padx=5, pady=5)

equals_button = tk.Button(window,bg= "#DAF7A6", text="=", width=20, font=("Arial", 15), command=button_equal)
equals_button.grid(row=row, column=col+1, padx=10, pady=10)

window.mainloop()
