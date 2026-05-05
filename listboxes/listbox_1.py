#it is a listing of selectable text items withint its own container
import tkinter as tk
def add_():
    listbox.insert(listbox.size(),entry.get())
    listbox.config(height=listbox.size())
def delete_():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())
    
root=tk.Tk()
root.title("Listbox operation by sanjog")
root.config(bg="gray")
listbox=tk.Listbox(root,selectmode="multiple",bg="black",fg="green",font=("Arial",30,"bold"))
listbox.insert(1,"Apple")
listbox.insert(2,"Banana")
listbox.insert(3,"Orange")
listbox.insert(4,"Guava")
listbox.config(height=listbox.size())
listbox.pack(padx=10,pady=10)
entry=tk.Entry(root,font=("arial",20))
entry.pack(pady=10)
add=tk.Button(root,text="add",command=add_)
add.pack()
delete=tk.Button(root,text="delete",command=delete_)
delete.pack()
root.mainloop()