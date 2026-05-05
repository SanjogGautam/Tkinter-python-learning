import tkinter as tk
from tkinter import ttk #it is a notebook widget
root=tk.Tk()
notebook=ttk.Notebook(root)#widget that manages a collection of windows/displays
tab1=tk.Frame(notebook)#new frame for tab1 
tab2=tk.Frame(notebook)#new frame for tab2
notebook.add(tab1,text="Tab1")
notebook.add(tab2,text="Tab2")
notebook.pack(expand=True,fill="both")
tk.Label(tab1,text="Hello! My name is SanjogGautam").pack()
tk.Label(tab2,text="Hello! My name is Bhim Lal Gautam").pack()
root.mainloop()