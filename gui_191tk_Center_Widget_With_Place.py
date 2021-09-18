from tkinter import *

root = Tk()
root.title('center by place')
root.iconbitmap('ergo64.ico')
root.geometry('500x500')

my_button1 = Button(root, text = "button 1", font= ("helvetica,32"))
my_button2 = Button(root, text = "button 2", font= ("helvetica,32"))

my_button1.grid(column=0, row=0)
my_button2.grid(column=1, row=0)

my_button = Button(root, text = "Click Me !", font= ("helvetica,32"))
my_button.place(relx=0.5, rely=0.5, anchor = CENTER)

my_button3 = Button(root, text = "Click Moi !", font= ("helvetica,32"))
my_button3.place(x=100, y=50)


root.mainloop()
