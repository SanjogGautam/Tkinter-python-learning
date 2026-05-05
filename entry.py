#entry widget= text box that accepts single line of user input is called user input
import tkinter as tk
def submit():
    username=entry.get()
    print("Hello "+username )
    entry.config(state="disabled")
def backspace():
    entry.delete(len(entry.get())-1,"end")
def delete():
    entry.delete(0,"end")
root=tk.Tk()
entry=tk.Entry(root,font=("Arial",50),show="*")#it hides the entered data in the *
entry.pack(side="left")
submit=tk.Button(root,text="submit",command=submit)
submit.pack(side="right")
backspace=tk.Button(root,text="backsapce",command=backspace)
backspace.pack(side="right")
delete=tk.Button(root,text="delete",command=delete)
delete.pack(side="right")
root.mainloop()



