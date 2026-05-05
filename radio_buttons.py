import tkinter as tk
food=["pizza","Momo","syafaley"]
def display():
    print(f"You have selected {food[x.get()]}")
root=tk.Tk()
x=tk.IntVar()
for i in range(len(food)):
    radio_button=tk.Radiobutton(root,text=food[i],variable=x,value=i,
                                width=200,font=("arial",30),fg="green",bg="black",  activebackground="black",activeforeground="green",command=display)
    radio_button.pack(anchor="nw")
root.mainloop()