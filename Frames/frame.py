#frame is a rectangulat container to group and hold widgets together
#wasd
import tkinter as tk
root=tk.Tk()
frame=tk.Frame(root,bg="green",bd=5,relief="raised")
frame.pack()
tk.Button(frame,text="W",font=("Arial",15)).pack(side="top")
tk.Button(frame,text="A",font=("Arial",15)).pack(side="left")
tk.Button(frame,text="S",font=("Arial",15)).pack(side="left")
tk.Button(frame,text="D",font=("Arial",15)).pack(side="left")

root.mainloop()