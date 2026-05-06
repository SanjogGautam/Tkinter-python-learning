#grid()=geometry manager that organizes widgets in a table-like structure(rows and columns)
import tkinter as tk
def sub():
    a=entry.get()
    print("Your First Name is = ",a)
root=tk.Tk()
entry=tk.Entry(root,fg="green",bg="black")
entry.grid(row=0,column=0)
button=tk.Button(root,text="submit",fg="gray",bg="black",command=sub).grid(row=0,column=1)
root.mainloop()