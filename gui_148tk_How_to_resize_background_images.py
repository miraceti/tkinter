from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title('RESIZE BOUTON')
root.geometry('1000x700')

#define a image
# bg = PhotoImage(file="images/mando2.png")
bg = ImageTk.PhotoImage(file="images/mando2.png")

#create a canvas
my_canvas = Canvas(root, width=1000, height=700)
my_canvas.pack(fill="both", expand=True)

#set a image in the canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")

#add a label
my_canvas.create_text(500,350, text="Welcome!", font=("helvetica", 50), fill="White")

#add some buttons
my_button1 =  Button(root, text="Exit1")
my_button2 =  Button(root, text="Exit2")
my_button3 =  Button(root, text="Exit3")

button1_window = my_canvas.create_window(10,10, anchor="nw", window=my_button1)
button2_window = my_canvas.create_window(100,10, anchor="nw", window=my_button2)
button3_window = my_canvas.create_window(230,10, anchor="nw", window=my_button3)

def resizer(e):
    global bg1, resized_bg, new_bg
    #open image
    bg1 = Image.open("images/mando2.png")
    #resize the image
    resized_bg = bg1.resize((e.width,e.height), Image.ANTIALIAS)
    #define the image again
    new_bg = ImageTk.PhotoImage(resized_bg)
    #add the image back to the canvas
    my_canvas.create_image(0,0, image=new_bg, anchor="nw")
    #readd the text
    my_canvas.create_text(500,350, text="Welcome!", font=("helvetica", 50), fill="White")


'''
#create a label
my_label= Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

#add something to the top of the image
my_text = Label(root, text="Welcome!", font=("Helvetica",50), fg="White", bg='#020304')
my_text.pack(pady=20)


#create a frame
my_frame = Frame(root, bg='#44ee44')
my_frame.pack(pady=20)

#add some button
# my_button1 =  Button(root, text="Exit")
# my_button1.pack(pady=20)

my_button1 =  Button(my_frame, text="Exit1")
my_button1.grid(row=0, column=0, padx=20)

my_button2 =  Button(my_frame, text="Exit2")
my_button2.grid(row=0, column=1, padx=20)

my_button3 =  Button(my_frame, text="Exit3")
my_button3.grid(row=0, column=2, padx=20)

'''

root.bind('<Configure>', resizer)

mainloop()