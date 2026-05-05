import tkinter as tk
a=0
def click():
    global a
    a+=1
    print(f"clicked {a}")
root=tk.Tk()
photo=tk.PhotoImage(file="images/logo.png")
button=tk.Button(root,text="clickme!",command=click,font=("comic sans",30),fg='green',bg="black",
                 activeforeground="green",activebackground="black",
                 image=photo,compound="bottom")
button.pack()
root.mainloop()