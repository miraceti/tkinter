from tkinter import *
import wikipedia as wiki


root=Tk()
root.title('search_wikipedia app')
root.iconbitmap('ergo64.ico')
root.geometry('700x700')
root.resizable(True, True)  #largeur , hauteur

def clear():
    my_entry.delete(0, END)
    my_text.delete(0.0, END)

def search():
    # data = wiki.page(my_entry.get())
    # data = wiki.summary(my_entry.get())
    # data = wiki.summary(my_entry.get(), sentences=10)
    data = wiki.page(my_entry.get())
    clear()
    # my_text.insert(0.0, data.content)
    # my_text.insert(0.0, data)
    my_text.insert(0.0, data.title)
    


my_label_frame = LabelFrame(root, text="Search Wikipedia")
my_label_frame.pack(pady=20)

my_entry = Entry(my_label_frame, font=("helvetica",18), width = 47)
my_entry.pack(pady=20, padx=20)

my_textbox_frame = Frame(root)
my_textbox_frame.pack(pady=5)

text_scroll = Scrollbar(my_textbox_frame)
text_scroll.pack(side=RIGHT, fill=Y)

hor_scroll = Scrollbar(my_textbox_frame, orient = 'horizontal')
hor_scroll.pack(side = BOTTOM, fill = X)

my_text = Text(my_textbox_frame, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
my_text.pack()

text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)


my_button_frame = Frame()
my_button_frame.pack(pady=10)

search_button = Button(my_button_frame, text = "Search", font=("helvetica",32), fg = "#3a3a3a", command=search)
search_button.grid(row=0, column=0, padx=20)

clear_button = Button(my_button_frame, text = "Clear", font=("helvetica",32), fg = "#3a3a3a", command=clear)
clear_button.grid(row=0, column=1)

root.mainloop()