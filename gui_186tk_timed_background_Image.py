from tkinter import *

root = Tk()
root.title('timer_image_background')
root.iconbitmap('ergo64.ico')
root.geometry('1000x800')

global our_images, count
count=-1
our_images = [
    PhotoImage(file="images/1.png"),
    PhotoImage(file="images/2.png"),
    PhotoImage(file="images/3.png"),
    PhotoImage(file="images/4.png"), 
    PhotoImage(file="images/5.png"),
    PhotoImage(file="images/6.png"),
    
]

# create canvas
my_canvas = Canvas(root, width=1000, height=800, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

# set canvas image
my_canvas.create_image(0,0, image=our_images[0], anchor='nw')

def next():
    global count
    if count==5:
        my_canvas.create_image(0,0, image=our_images[0], anchor='nw')
        count=0
    else:
        my_canvas.create_image(0,0, image=our_images[count+1], anchor='nw')
        count += 1
    
    root.after(5000, next)

next()
root.mainloop()
