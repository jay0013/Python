import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the display
display = tk.Entry(window, width=20, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the buttons
button_list = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "+", "="
]

row = 1
col = 0
for button_text in button_list:
    button = tk.Button(window, text=button_text, width=5, height=2,
                       command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Define the button click function
def button_click(text):
    if text == "=":
        try:
            result = str(eval(display.get()))
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    else:
        display.insert(tk.END, text)

# Run the main loop
window.mainloop()