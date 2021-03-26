from tkinter import *

root=Tk()
root.title('switch')
root.geometry('600x600')
root.iconbitmap('ergo64.ico')

def update(data):
    # clear the list box
    my_list.delete(0, END)
    
    # add toppings to listbox
    for item in data:
        my_list.insert(END, item)
        
def fillout(e):
    my_entry.delete(0, END)
    
    # add clicked item to entry box
    my_entry.insert(0, my_list.get(ANCHOR))
           
def check(e):
    typed = my_entry.get()
    
    if typed == '':
        data = toppings
    else:
        data=[]
        for item in toppings:
            if typed.lower() in item.lower():
                data.append(item)
                
    # update the listbox            
    update(data)

my_label = Label(root, text="Start typing...",
                 font=("helvetica",14),
                 fg="grey")
my_label.pack(pady=20)

my_entry = Entry(root, font=("helvetica",20))
my_entry.pack()

# create listbox
my_list = Listbox(root, width=50)
my_list.pack(pady=40)

# create a list of pizza toppings
toppings = ["Pepperoni", "Peppers", "Mushroom", "Cheese", "Onions","Ham","Taco"]

# add the toppings to our list
update(toppings)

# create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)

# create a binding on the entry box
my_entry.bind("<KeyRelease>", check)

mainloop()