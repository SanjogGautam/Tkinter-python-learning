import tkinter as tk
def do(event):
    print("Mouse event: ", event)
root = tk.Tk()
root.bind("<Button-1>", do)#it will bind the left mouse button click event to the do function
root.mainloop()
#various mouse events
#<Button-1> : left mouse button click
#<Button-2> : middle mouse button click
#<Button-3> : right mouse button click
#<Double-Button-1> : double left mouse button click
#<Double-Button-2> : double middle mouse button click
#<Double-Button-3> : double right mouse button click
#<Enter> : mouse pointer enters the widget
#<Leave> : mouse pointer leaves the widget
#<Motion> : mouse pointer moves within the widget
