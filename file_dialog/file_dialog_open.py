#it is used to open and read teh content of a file
import tkinter as tk
from tkinter import filedialog
def display():
    filepath=filedialog.askopenfilename(title="open_a_file",
                                    filetypes=(("text files","*.txt"),("allfiles","*.*")))
    with open(filepath,'r') as file:
        print(file.readline())
    if filepath is None:#this doesn't throw an crash error
        return

root=tk.Tk()
button=tk.Button(root,text="read_File",fg="green",bg="black",activebackground="black",activeforeground="green",command=display)
button.pack(pady=10)
root.mainloop()