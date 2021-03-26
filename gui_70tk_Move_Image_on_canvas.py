from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("800x600")

w = 600
h = 400
x = w/2
y = h/2

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

#add an image
img = PhotoImage(file="images/blue4.png")

my_image = my_canvas.create_image(250,160, anchor=NW, image=img)

def left(event):
    x = -10
    y = 0
    my_canvas.move(my_image,x, y)

def right(event):
    x = 10
    y = 0
    my_canvas.move(my_image,x, y)

def up(event):
    x = 0
    y = -10
    my_canvas.move(my_image,x, y)

def down(event):
    x = 0
    y = 10
    my_canvas.move(my_image,x, y)

root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.mainloop()