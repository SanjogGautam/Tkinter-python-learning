import time
import tkinter as tk

def update_all():
    # Get Time, Day, and Date strings
    time_str = time.strftime("%I:%M:%S %p")
    day_str = time.strftime("%A")
    date_str = time.strftime("%B %d, %Y")
    
    # Update the labels
    time_label.config(text=time_str)
    day_label.config(text=day_str)
    date_label.config(text=date_str)
    
    root.after(1000, update_all)

root = tk.Tk()
root.title("Cyber-Clock")
root.config(bg="black") # Set window background to black


time_label = tk.Label(root, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack()


day_label = tk.Label(root, font=("Arial", 25), fg="yellow", bg="black")
day_label.pack()


date_label = tk.Label(root, font=("Arial", 20), fg="cyan", bg="black")
date_label.pack()
#calling the function to start it all
update_all()

root.mainloop()