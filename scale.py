import tkinter as tk
def display():
    if scale.get()>=50:
        print("IT's HOT!")
    else:
        print("it's cold!")
root = tk.Tk()
root.title("Temperature Control")
root.config(bg="gray")

# 1. Load Images
try:
    hot = tk.PhotoImage(file="images/hot.png").subsample(2, 2) # Resize the hot image to fit better
    cold = tk.PhotoImage(file="images/cold.png").subsample(2, 2) # Resize the cold image to fit better
except Exception as e:
    print(f"Error loading images: {e}")
    hot = cold = None

# 2. Hot Label (Top)
hotlabel = tk.Label(root, image=hot, bg="black")
hotlabel.pack(pady=(10, 0)) # Adds 10px padding only at the top

# 3. Scale (Middle)
scale = tk.Scale(root, 
                 from_=100, 
                 to=0, 
                 orient=tk.VERTICAL,
                 tickinterval=10,
                 showvalue=0,
                 length=300,
                 troughcolor="aqua", 
                 fg="red", 
                 bg="black",
                 highlightthickness=0) # Removes the border for a cleaner look
scale.set(50)
scale.pack()

# 4. Cold Label 
coldlabel = tk.Label(root, image=cold, bg="black")
coldlabel.pack(pady=(0, 10)) # Adds 10px padding only at the bottom
#5. submit button
submit=tk.Button(root,command=display,text="Submit",fg="black",bg="green",activebackground="green",activeforeground="black",compound="bottom")
submit.pack(pady=10)
root.mainloop()