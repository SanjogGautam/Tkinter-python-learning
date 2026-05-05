#label: it is an area widget that holds text and/or an image within a window
import tkinter as tk
root=tk.Tk()
label=tk.Label(root,text="Hello Wolrd")
#label.place(x=0,y=0) it use used the place the given label whereever we want
label.pack()#it puts the label in the default top and center postion of the 
photo=tk.PhotoImage(file="images/logo.png")
label2=tk.Label(root,text="Hello My name is Sanjog",font=('arial',30,'bold'),fg="green",bg="black",padx=10,pady=10,image=photo,compound="bottom")
label2.pack()
root.mainloop()