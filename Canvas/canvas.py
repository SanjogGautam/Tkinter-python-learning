#it is an widget that is used to draw graphs, plots, and images in a window
import tkinter as tk
root=tk.Tk()
canvas=tk.Canvas(root,height=500,width=500)
canvas.create_line(0,0,500,500,fill="blue",width=5)
canvas.create_rectangle(0,0,50,50,fill="green",width=5)
canvas.create_arc(0,0,500,500,fill="black",outline="green",width=5,start=90)
canvas.pack()
root.mainloop()