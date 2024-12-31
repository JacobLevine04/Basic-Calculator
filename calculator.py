import tkinter as tk

def click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# main window
root = tk.Tk()
root.title("Basic Calculator")
root.configure(bg="#add8e6")  # background to light blue
root.geometry("400x500")  # default window size

# entry widget for display
entry = tk.Entry(root, width=20, font=("Arial", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4)

# labels for each button
buttons = [
    "1", "2", "3", "+",
    "7", "8", "9", "-",
    "4", "5", "6", "*",
    "C", "0", "=", "/"
]

# create buttons
for i, text in enumerate(buttons):
    row, col = divmod(i, 4)
    button = tk.Button(
        root, text=text, font=("Arial", 20), bg="#e0f7fa", relief="flat",
        command=lambda t=text: click(t)
    )
    button.grid(row=row+1, column=col, sticky="nsew", padx=2, pady=2)

# adjust row and column weights
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i+1, weight=1)

# start the main loop
root.mainloop()