from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("400x400")

def clicker(event):
    # myLabel = Label(root, text="you clicked" + str(event.x) + ' ' + str(event.y))
    myLabel = Label(root, text="you clicked : " + str(event.keysym))
    # myLabel = Label(root, text="you clicked : " + str(event.char))
    myLabel.pack()

# myButton = Button(root, text="Click Me!", command=clicker)
myButton = Button(root, text="Click Me!")
# myButton.bind(event, action)
#click gauche souris
# myButton.bind("<Button-1>", clicker)
# #click milieu souris
# myButton.bind("<Button-2>", clicker)
#click droit souris
# myButton.bind("<Button-3>", clicker)
# souris entre sur le widget
# myButton.bind("<Enter>", clicker)
#souris quitte le widget
# myButton.bind("<Leave>", clicker)
#focus sur le widget
# myButton.bind("<FocusIn>", clicker)
#click gauche souris
# myButton.bind("<Return>", clicker)
#touche clavier quelconque
myButton.bind("<Key>", clicker)

myButton.pack(pady=20)


root.mainloop()