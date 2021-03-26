from tkinter import *
from tkinter.font import Font

root=Tk()
root.title('Liste déroulante!')
root.geometry('500x600')

#define font
my_font = Font(
    family="Brush Script MT", 
    size=30,
    weight="bold")


my_frame = Frame(root)
my_frame.pack(pady=5)

my_list = Listbox(my_frame,
                  font=my_font,
                  width=25,
                  height=5,
                  bg="SystemButtonface",
                  bd=0,
                  fg="#464646",
                  highlightthickness=0,
                  selectbackground="#a6a6a6",
                  activestyle="none"
                  
                  )
my_list.pack(side=LEFT, fill=BOTH)

stuff = ["Walk The Dog","Buy Groceries","Take a Nap","Learn Tkinter","Rule The World"]

for item in stuff:
    my_list.insert(END, item)

#create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

#add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#create entry box
my_entry = Entry(root, font=("Helvetica",20))
my_entry.pack(pady=10)

#create  button frame
button_frame = Frame(root)
button_frame.pack(pady=10)

def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def cross_off_item():
    #cross off item
    my_list.itemconfig(
        my_list.curselection(),
        fg = "#dedede"
    )
    #get rid of selection bar
    my_list.selection_clear(0, END)

def uncross_item():
    #cross off item
    my_list.itemconfig(
        my_list.curselection(),
        fg = "#464646"
    )
    #get rid of selection bar
    my_list.selection_clear(0, END)

def delete_cross():
    print(my_list.size())
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede" :
            my_list.delete(my_list.index(count))
            
        count += 1

#add some buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)
cross_off_button = Button(button_frame, text="Cross Off Item", command=cross_off_item)
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item)
delete_cross_button = Button(button_frame, text="Delete Crossed Item", command=delete_cross)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_cross_button.grid(row=0, column=4)

mainloop()