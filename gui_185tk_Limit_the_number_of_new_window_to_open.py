from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('TreeBase')
root.iconbitmap('ergo64.ico')
root.geometry('300x200')


global counter
counter=1

def open():
    global counter
    
    #create counter logic
    if counter < 2:
        top = Toplevel()
        top.title('new window')
        top.iconbitmap('ergo64.ico')
        top.geometry('300x200')
        
        my_label = Label(top, text="new window!", font=("helvetica,24"))
        my_label.pack(pady=50, padx=50)
        
        counter +=1
    else:
        messagebox.showinfo("Error", "Hey, tu as deja ouvert une nouvelle fenêtre! ")

my_button = Button(root, text="Open Window", command=open)
my_button.pack(pady=50, padx=50)

root.mainloop()
