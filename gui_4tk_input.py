from tkinter import *

root = Tk()

#e = Entry(root, width =50, borderwidth=5, bg="blue", fg="white")
e = Entry(root, width =50)
e.pack()
#valeur par defaut
e.insert(0, "Enter your name: ")

def myClick():
    hello = "hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

#myButton = Button(root, text="Click Me!", state=DISABLED)
#pour la taille : padx et pady
#myButton = Button(root, text="Click Me!", padx=100, pady=50)
#myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="red")
myButton = Button(root, text="Enter your name", command=myClick, fg="blue", bg="#ff00ff")
myButton.pack()

root.mainloop()