from tkinter import *
from tkinter import ttk

root=Tk()
root.title('resize app')
root.iconbitmap('ergo64.ico')
root.geometry('500x500')
root.resizable(True, True)  #largeur , hauteur

my_frame2 = Frame(root, highlightbackground="gray", highlightthickness=1)
my_frame2.pack(pady=20)

my_label = Label(my_frame2, text="Hello World!", font=("helvetica", 32))
my_label.pack(pady=50, padx=20)

#create sizegrip
my_sizegrip2 = ttk.Sizegrip(my_frame2)
# grid
# my_sizegrip.grid(row=1, sticky=SE)
# pack
my_sizegrip2.pack(side="right", anchor=SE)


#reconfigure rows and colums for grid
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# create a frame
my_frame = Frame(root, highlightbackground="gray", highlightthickness=1)
my_frame.pack(side = "bottom", fill=X)

#create sizegrip
my_sizegrip = ttk.Sizegrip(my_frame)
# grid
# my_sizegrip.grid(row=1, sticky=SE)
# pack
my_sizegrip.pack(side="right", anchor=SE)


root.mainloop()