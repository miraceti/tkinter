from tkinter import *

root=Tk()
root.title('bell!')
root.geometry('996x689')

bell = PhotoImage(file="images/bell1.png")

bell_label = Label(root, image=bell)
bell_label.pack(pady=20)

#define ring function
def ring():
    root.bell()

#create a button
my_button = Button(root, text="Sonnez!!", command=ring, font=("helvetica",20), fg="#4d4d4d")
my_button.pack(pady=20)

root.bell()

mainloop()