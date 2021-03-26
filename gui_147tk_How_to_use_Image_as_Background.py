from tkinter import *

root=Tk()
root.title('RESIZE BOUTON')
root.geometry('1000x700')

#define a image
bg = PhotoImage(file="images/mando2.png")

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



mainloop()