import tkinter as tk
def display():
    tk.messagebox.showinfo(title="this is info",message="You are a person")
root=tk.Tk()
root.config(bg="gray")
root.attributes('-topmost', True)#this brings the root window infront of the vscode 
button=tk.Button(text="Click Me!",font=("Arial",20),fg="green",background="black",activebackground="black",activeforeground="green",command=display)
button.pack(pady=20)
root.mainloop()