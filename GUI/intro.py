import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Python GUI")
# win.resizable(0,0)
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

def clickme():
    action.configure(text="Hello " + name.get())

ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

action = ttk.Button(win, text="Click Me!", command=clickme)
action.grid(column=1, row=1)
action.configure(state='disable')
nameEntered.focus()

win.mainloop()
