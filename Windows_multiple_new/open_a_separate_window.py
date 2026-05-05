import tkinter as tk
def newtab():
    new_root=tk.Tk()
    old_root.destroy()
def new_newtab():
    new_root=tk.Toplevel()
old_root=tk.Tk()
c_button=tk.Button(old_root,text="New tab on top",command=new_newtab).pack()
cc_button=tk.Button(old_root,text="New separate tab",command=newtab).pack()
old_root.mainloop()