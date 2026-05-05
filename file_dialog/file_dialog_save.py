import tkinter as tk
from tkinter import filedialog #importing a submodule
def display():
    file=filedialog.asksaveasfile(defaultextension=".txt",
                                  filetypes=[
                                      ("text file",".txt"),
                                      ("html file",".html"),
                                      ("all types",".*")])
    file_text=str(text.get(1.0,"end"))
    file.write(file_text)
    file.close()
    if file is None:
        return

root=tk.Tk()
text=tk.Text(root,bg="black",fg="green",font=("ink free",20),height=15,width=20,padx=10,pady=10)
text.pack()
button=tk.Button(root,text="File_save",fg="green",bg="black",activebackground="black",activeforeground="green",command=display)
button.pack()
root.mainloop()