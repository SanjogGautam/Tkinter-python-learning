import tkinter as tk
def display():
    if x.get()==1:
        print("You agreeed!")
    else:
        print("you didn't agree")
root=tk.Tk()
x=tk.IntVar()
photo=tk.PhotoImage(file="images/logo.png")
check_button=tk.Checkbutton(root,text="I agree to something!", variable=x,onvalue=1,offvalue=0,command=display,font=("Arial",30),fg="green",bg="black",image=photo,compound="left",activebackground="black",activeforeground="green")
check_button.pack()
root.mainloop()

