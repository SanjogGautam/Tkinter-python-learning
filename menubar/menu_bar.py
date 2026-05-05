import tkinter as tk

def openfile():
    print("File opened!")

def closefile():
    print("File closed!")

def edit():
    print("Editing mode active!")

root = tk.Tk()
root.geometry("300x200")

# 1. Create the main Menu Bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# 2. Creating 'File' dropdown menu
# tearoff=0 prevents the menu from being "detached" into a separate window
file_menu = tk.Menu(menubar, tearoff=0)

# 3. Adding the File menu to the Menu Bar
menubar.add_cascade(label="File", menu=file_menu)

# 4. Adding commands to the File menu
file_menu.add_command(label="Open", command=openfile)
file_menu.add_command(label="Close", command=closefile)
file_menu.add_separator() # This adds a nice horizontal line
file_menu.add_command(label="Exit", command=quit)

# 5.  adding an 'Edit' menu just for practice
edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)#this adds a drop down
edit_menu.add_command(label="Cut", command=edit)
edit_menu.add_command(label="Copy", command=edit)
edit_menu.add_command(label="Paste", command=edit)

root.mainloop()