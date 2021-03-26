from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("ICONS")
root.iconbitmap('D:\eric\python\gui\code2.ico')

frame = LabelFrame(root,  padx=50, pady=50)
frame.pack(padx=10, pady=10)

frame2 = LabelFrame(root, text="2",  padx=2, pady=2)
frame2.pack(padx=10, pady=10)


b = Button(frame, text="click click")
b2 = Button(frame, text="ni click")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)


b20 = Button(frame2, text="click click")
b21 = Button(frame2, text="ni click")
b20.grid(row=0, column=0)
b21.grid(row=1, column=1)



root.mainloop()