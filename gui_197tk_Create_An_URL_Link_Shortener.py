from tkinter import *
import pyshorteners


root = Tk()
root.title('create shorten link')
root.iconbitmap('ergo64.ico')
root.geometry('500x500')

def shorten():
    if shorty.get():
        shorty.delete(0, END)
    
    if my_entry.get():
        # convert to tyniurl
        url = pyshorteners.Shortener().tinyurl.short(my_entry.get())
        # output to screen
        shorty.insert(END, url)
        
        # reverse URL
        print(pyshorteners.Shortener().tinyurl.expand(url))
    
    
my_label = Label(root, text="Enter link to Shorten", font=("helvetica",34))
my_label.pack(pady=20)

my_entry = Entry(root, font=("helvetica",24))
my_entry.pack(pady=20)

my_button = Button(root, text="Shorten Link", command=shorten, font=("helvetica",24))
my_button.pack(pady=20)

shorty_label = Label(root, text="Shortened Link", font=("helvetica",14))
shorty_label.pack(pady=50)

shorty = Entry(root, font=("helvetica",22), justify=CENTER, width=30, bd=0, bg="systembuttonface")
shorty.pack(pady=20)

root.mainloop()
