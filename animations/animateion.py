import tkinter as tk
import time
W = 500
H = 500
global xvelocity, yvelocity
xvelocity = 1
yvelocity = 1
root = tk.Tk()
canvas = tk.Canvas(root, width=W, height=H)
canvas.pack()
race_car=tk.PhotoImage(file="images/racecar.png").subsample(4,4)
space_img = tk.PhotoImage(file="images/space.png").zoom(3,3)
my_img=canvas.create_image(0, 0, image=space_img, anchor="nw")
my_car=canvas.create_image(0,0,image=race_car,anchor="nw")
while True:
    coordinates=canvas.coords(my_car)
    print(coordinates)
    if (coordinates[0]>=(W-race_car.width()) or coordinates[0]<0):
        xvelocity=-xvelocity
    if (coordinates[1]>=(H-race_car.height()) or coordinates[1]<0):
        yvelocity=-yvelocity
    canvas.move(my_car,xvelocity,yvelocity)
    time.sleep(0.005)
    root.update()

root.mainloop()