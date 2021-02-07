from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look i clik a button!")
    myLabel.pack()

#myButton = Button(root, text="Click Me!", state=DISABLED)
#pour la taille : padx et pady
#myButton = Button(root, text="Click Me!", padx=100, pady=50)

#myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="red")
myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="#ff00ff")


myButton.pack()

root.mainloop()