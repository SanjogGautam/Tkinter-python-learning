import tkinter as tk
def dosomething(event):
    print("You hve pressed: ", event.keysym)
    label.config(text=f"You have pressed: {event.keysym}")
root=tk.Tk()
root.bind("<Return>",dosomething)
label=tk.Label(root,font=("arial",20),bg="black",fg="green")
label.pack()
root.mainloop()