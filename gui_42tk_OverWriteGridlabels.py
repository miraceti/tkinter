from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("400x400")

def myDelete():
    #myLabel.pack_forget()
    myLabel.grid_forget()
    # myLabel.destroy()
    myButton['state']=NORMAL
    # print(myButton.winfo_exists())

def myClick():
    global myLabel
    hello = "hello " + e.get()
    myLabel = Label(root, text = hello)
    e.delete(0, 'end')
    myLabel.grid(row=3, column=0,pady=10)
    myButton['state']=DISABLED

#input
e = Entry(root, width=17, font=('helvetica', 30))
e.grid(row=0, column=0,padx=10, pady=10)

#bouton
myButton = Button(root, text="Entre your Name", command=myClick)
myButton.grid(row=1, column=0,pady=10)


DeleteButton = Button(root, text="Delete Text", command=myDelete)
DeleteButton.grid(row=2, column=0,pady=10)


root.mainloop()