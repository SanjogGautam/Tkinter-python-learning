#text_widget= functions like a text area, we can enter multiple lines of text
import tkinter as tk
def submit():
    print(text.get(1.0,"end"))
root=tk.Tk()

text=tk.Text(root,bg="black",fg="green",font=("ink free",20),height=5,width=10,padx=10,pady=10)
text.pack()
button=tk.Button(root,command=submit,text="submit",compound="bottom")
button.pack()
root.mainloop()