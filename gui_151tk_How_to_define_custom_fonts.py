from tkinter import *
from tkinter.font import Font

root=Tk()
root.title('font!')
root.geometry('996x689')

#define our font
bigfont = Font(
    family = "Helvetica",  # ou Times
    size = 42,
    weight = "bold" ,  # ou normal 
    slant = "roman",  # ou roman , 
    underline = 0 ,   # 0:pas de sousligne et 1: avec
    overstrike = 0   # 1: ligne barrée et 0 sans ligne barrée
    )

mediumfont = Font(
    family = "Times",  # ou Times
    size = 24,
    weight = "normal" ,  # ou normal 
    slant = "italic",  # ou roman , 
    underline = 1 ,   # 0:pas de sousligne et 1: avec
    overstrike = 0   # 1: ligne barrée et 0 sans ligne barrée
    )
#define a button
my_button1 =  Button(root, text="big text", font=bigfont)
my_button1.pack(pady=20)


#label
my_label = Label(root, text="more big text", font=mediumfont)
my_label.pack(pady=20)

mainloop()