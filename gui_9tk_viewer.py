from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("ICONS")
root.iconbitmap('D:\eric\python\gui\code2.ico')

my_img1 = ImageTk.PhotoImage(Image.open("images/1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/3.bmp"))
#my_img4 = ImageTk.PhotoImage(Image.open("images/4.jpg"))
#my_img5 = ImageTk.PhotoImage(Image.open("images/5.png"))
my_img6 = ImageTk.PhotoImage(Image.open("images/got1b.png"))

image_list = [my_img1,my_img2,my_img3,my_img6]

my_label = Label(image=my_img6)
#my_label.pack()
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: backward(image_number-1))

    if image_number == 4 :
        button_forward = Button(root, text=">>", state=DISABLED) 

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def backward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: backward(image_number - 1))

    if image_number == 1 :
        button_back = Button(root, text="<<", state=DISABLED) 

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", command= backward, state=DISABLED)
button_exit = Button(root, text="EXIT", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()