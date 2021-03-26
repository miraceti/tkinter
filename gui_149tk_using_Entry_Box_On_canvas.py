from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title('box')
root.geometry('996x689')
root.resizable(width=False, height=False)

#define a background image
# bg = PhotoImage(file="images/mando2.png")
bg = ImageTk.PhotoImage(file="images/mando2.png")

#define canvas
my_canvas = Canvas(root, width=996, height=689, bd=0, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

#put the image on the canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")

#define entry box
un_entry = Entry(root, font=("helvetica",40), width=14, fg="#336d92", bd=0)
pw_entry = Entry(root, font=("helvetica",40), width=14, fg="#336d92", bd=0)

un_entry.insert(0, "username")
pw_entry.insert(0, "password")

#add the entry box to the canvas
un_window = my_canvas.create_window(334, 290, anchor="nw", window=un_entry)
pw_window = my_canvas.create_window(334, 370, anchor="nw", window=pw_entry)

#create welcome screen , function
def welcome():
    un_entry.destroy()
    pw_entry.destroy()
    login_button.destroy()
    #add welcome message
    my_canvas.create_text(480, 200, text="WELCOME", font=("helvetica", 60), fill="white")


#define Button
login_button = Button(root, text="Login", font=("helvetica",40), width=15, fg="#336d92", command=welcome)

#add the button to the canvas
login_btn_window = my_canvas.create_window(304, 470, anchor="nw", window=login_button)

#define entry_clear function
def entry_clear(e):
    if un_entry.get()== "username" or pw_entry.get() == "password":
        un_entry.delete(0, END)
        pw_entry.delete(0, END)
        #change text to star
        pw_entry.config(show="*")

#bind entry boxes
un_entry.bind("<Button-1>", entry_clear)
pw_entry.bind("<Button-1>", entry_clear)

mainloop()