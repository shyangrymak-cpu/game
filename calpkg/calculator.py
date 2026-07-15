import tkinter as tk

# ---------------- Window ----------------
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("360x540")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# ---------------- Display ----------------
expression = ""

display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Segoe UI", 28),
    bd=0,
    bg="#1e1e1e",
    fg="white",
    justify="right",
    insertbackground="white"
)

display.pack(fill="both", ipadx=8, ipady=30, padx=15, pady=20)

# ---------------- Functions ----------------
def press(value):
    global expression
    expression += str(value)
    display_var.set(expression)

def clear():
    global expression
    expression = ""
    display_var.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display_var.set(result)
        expression = result
    except:
        display_var.set("Error")
        expression = ""

# ---------------- Buttons ----------------
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(expand=True, fill="both", padx=10, pady=10)

# AC Button
ac_btn = tk.Button(
    frame,
    text="AC",
    font=("Segoe UI", 20, "bold"),
    bg="#ff5c5c",
    fg="white",
    bd=0,
    activebackground="#ff7b7b",
    command=clear
)

ac_btn.grid(row=0, column=0, columnspan=4,
            sticky="nsew", padx=6, pady=6, ipady=15)

# Create calculator buttons
for r, row in enumerate(buttons, start=1):
    for c, char in enumerate(row):

        if char == "=":
            cmd = calculate
            bg = "#00c896"
        elif char in ['/', '*', '-', '+']:
            cmd = lambda x=char: press(x)
            bg = "#ff9f43"
        else:
            cmd = lambda x=char: press(x)
            bg = "#2d2d2d"

        btn = tk.Button(
            frame,
            text=char,
            font=("Segoe UI", 20, "bold"),
            bg=bg,
            fg="white",
            bd=0,
            activebackground="#444",
            command=cmd
        )

        btn.grid(
            row=r,
            column=c,
            sticky="nsew",
            padx=6,
            pady=6,
            ipady=20
        )

# Responsive Grid
for i in range(5):
    frame.rowconfigure(i, weight=1)

for j in range(4):
    frame.columnconfigure(j, weight=1)

# ---------------- Run ----------------
root.mainloop()