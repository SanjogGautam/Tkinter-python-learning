import tkinter as tk
from tkinter import messagebox
def display():
    #messagebox.showinfo(title="this is info",message="You are a person")
    #messagebox.showwarning(title="This is a Warning!",message="You have a virus")
    # if(messagebox.askokcancel(title="ask_ok_cancel",message="Do you want to know it?")):
    #     #it returns true or false
    #     print("You are awesome!")
    # else:
    #     print("You aren't awesome!")
    # if(messagebox.askretrycancel(title="ask_ok_cancel",message="Do you want to know it?")):
    #     #it returns true or false
    #     print("You are awesome!")
    # else:
    #     print("You aren't awesome!")

    # if(messagebox.askyesno(title="ask_yes_no",message="Do you want to know it?")):
    #     #it returns true or false
    #     print("You are awesome!")
    # else:
    #     print("You aren't awesome!")
    # print(messagebox.askquestion(title="axsk_question",message="Do you like momen?"))
        #it returns yes or no
    ans=messagebox.askyesnocancel(title="ask_yes_no_cancel",message="Do you want to go gym?")
    if ans is True:
        #it returns true , false and none
        print("You are awesome!")
    elif ans is False:
        print("You aren't awesome!")
    else:
        print("BE decisive")
root=tk.Tk()
root.config(bg="gray")
root.attributes('-topmost', True)#this brings the root window infront of the vscode 
button=tk.Button(text="Click Me!",font=("Arial",20),fg="green",background="black",activebackground="black",activeforeground="green",command=display)
button.pack(pady=20)
root.mainloop()