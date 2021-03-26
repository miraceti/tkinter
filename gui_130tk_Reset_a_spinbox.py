from tkinter import *


root = Tk()
root.title('ERIC PY PROGRAM')
root.geometry('500x500')

def reset_spinner():
    # var = IntVar(root)
    # var.set(0)
    
    var2 = StringVar(root)
    var2.set("John")
    
    
    my_spin.config(textvariable = var2)

# set Intvar
var = IntVar(root)
var.set(10)

# set Stringvar
var2 = StringVar(root)
var2.set("John")

my_spin = Spinbox(root, 
                #   from_=0, to=100, 
                values = ("John", "Mary","Bob","Tina"),
                font =("Helvetica",20),
                textvariable=var2
                  )
my_spin.pack(pady=20)

my_button = Button(root, text="reset spinner", command=reset_spinner)
my_button.pack(pady=20)


root.mainloop()