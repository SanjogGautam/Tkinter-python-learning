import tkinter as tk
def move_up(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)
def move_left(event):
    label.place(x=label.winfo_x()-10,y=label.winfo_y())
def move_right(event):
    label.place(x=label.winfo_x()+10,y=label.winfo_y())
def move_down(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()+10)


root=tk.Tk()
root.bind("<w>",move_up)
root.bind("<a>",move_left)
root.bind("<s>",move_down)
root.bind("<d>",move_right)
photo=tk.PhotoImage(file="images/racecar.png").subsample(2,2)
label=tk.Label(root,image=photo)
label.pack(anchor="nw")
root.mainloop()