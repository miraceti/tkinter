from tkinter import *
from PIL import Image, ImageFont, ImageDraw

root = Tk()
root.title('Photo in Image')
root.iconbitmap('ergo64.ico')
root.geometry('600x650')

# aff text to image
def add_image():
    # open the image
    my_image = Image.open("images/bitcoin1.png")
    # define the font
    text_font = ImageFont.truetype("arial.ttf", 46)
    # get text to add to the image
    text_to_add = my_entry.get()
    # edit image
    edit_image= ImageDraw.Draw(my_image)
    edit_image.text((15, 30), text_to_add, ("red"), font=text_font)
    # save the image
    my_image.save("images/bitcoin12.png")
    # clear entry box
    my_entry.delete(0, END)
    my_entry.insert(0, " saving file ...")
    # wait some second
    my_label.after(2000, show_pic)
    
def show_pic():
    global image2
    # show new image
    image2 = PhotoImage(file="images/bitcoin12.png")
    my_label.config(image=image2)
    
    # clear the entry box
    my_entry.delete(0, END)

# define an image
aspen = PhotoImage(file="images/bitcoin1.png")

# create a label
my_label = Label(root, image= aspen)
my_label.pack(pady=20)

# entry box
my_entry = Entry(root, font=("helvetica",24))
my_entry.pack(pady=20)

# a button
my_button = Button(root, text="Add Text To image", command= add_image, font=("helvetica",24))
my_button.pack(pady=20)

root.mainloop()
