import tkinter as tk 
def drag_start(event):
    widget=event.widget 
    widget.startx=event.x
    widget.starty=event.y
def drag_stop(event):
    widget=event.widget
    x=widget.winfo_x()-widget.startx+event.x
    y=widget.winfo_y()-widget.starty+event.y
    widget.place(x=x,y=y)
root=tk.Tk()
label1=tk.Label(root,bg="blue",width=10,height=5)
label1.place(x=0,y=0)
label2=tk.Label(root,bg='red',width=15,height=10)
label2.place(x=500,y=200)
label1.bind("<Button-1>",drag_start)
label1.bind("<B1-Motion>",drag_stop)
label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_stop)
root.mainloop()