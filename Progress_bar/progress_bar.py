import tkinter as tk
from tkinter.ttk import Progressbar
import time

def sub():
    tasks = 10
    x = 0
    while(x < tasks):
        time.sleep(0.2) # Simulate work being done (0.1 seconds)
        bar['value'] += 10 # Increase progress
        x += 1
        root.update_idletasks() # This "refreshes" the GUI mid-loop!
        
    if x == tasks:
        print("Download completed")

root = tk.Tk()
root.title("Sanjog's Downloader")

# Use orient="horizontal" (lowercase string is safer in ttk)
bar = Progressbar(root, orient="horizontal", length=300)
bar.pack(pady=10)

# it's better to stay consistent.
button = tk.Button(root, text="Download!", fg="green", bg="black", command=sub)
button.pack()

root.mainloop()