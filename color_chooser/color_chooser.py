import tkinter as tk
from tkinter import colorchooser
def submit():
    color=colorchooser.askcolor()
    print(color)
    color_hex=color[1]
    root.config(bg=color_hex)
root=tk.Tk()
root.config(bg="gray")
root.title("Color chooser")
button=tk.Button(root,text="pick",command=submit)
button.pack()
root.mainloop()