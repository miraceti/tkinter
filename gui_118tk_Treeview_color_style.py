from tkinter import *
from tkinter import ttk

root = Tk()
root.title('ERIC PY PROGRAM')
root.geometry("500x600")

#add some style
style = ttk.Style()

#add a theme
style.theme_use("alt")

#configure our treeview colors
style.configure("Treeview", 
                background =  "silver",
                foreground = "black",
                rowheight = 25,
                fieldbackground = "silver"                
                )

# change selectd color
style.map("Treeview",
          background=[('selected','red')]
          )

my_tree = ttk.Treeview(root )

#define our columns
my_tree['columns'] = ("Name", "ID", "Favorite Pizza")

#formatage des colonnes
my_tree.column("#0", width=0, stretch=NO)
# my_tree.column("#0", width=0, minwidth=0)
my_tree.column("Name", anchor=W,width=140, minwidth=2)
my_tree.column("ID", anchor=CENTER, width=100, minwidth=5)
my_tree.column("Favorite Pizza", anchor=W, width=140, minwidth=10)

#Headings
my_tree.heading("#0", text="Label", anchor=W )
my_tree.heading("Name", text="Nom", anchor=W)
my_tree.heading("ID", text="Id", anchor=CENTER)
my_tree.heading("Favorite Pizza", text="Pizza Favorites", anchor=W)

#add datas
data =[
    ["John", 1, "Peperroni" ],
    ["Marc", 2, "Champignon"],
    ["Eric", 3, "Vegetales"],
    ["Pierre", 4, "Jambon"],
    ["Luc", 5, "Fromage"],
    ["Philippe", 6, "Complète"]
]
global count 
count = 0
for record in data:
    my_tree.insert(parent='', index='end',iid=count, text="", values=(record[0], record[1], record[2]) )
    count += 1



# my_tree.insert(parent='', index='end',iid=0, text="", values=("John", 1, "Peperroni") )
# my_tree.insert(parent='', index='end',iid=1, text="", values=("Marc", "2", "Champignon") )
# my_tree.insert(parent='', index='end',iid=2, text="", values=("Eric", "3", "Vegetales") )
# my_tree.insert(parent='', index='end',iid=3, text="", values=("Pierre", "4", "Jambon") )
# my_tree.insert(parent='', index='end',iid=4, text="", values=("Luc", "5", "Fromage") )
# my_tree.insert(parent='', index='end',iid=5, text="", values=("Philippe", "6", "Complète") )

#add child
# my_tree.insert(parent='0', index='end',iid=6, text="Enfant", values=("Philippe", "1.3", "Complète") )
# ou
# my_tree.insert(parent='', index='end',iid=6, text="Child", values=("Steeve", "1.2", "Forestiere") )
# my_tree.move('6','0','0') 

my_tree.pack(pady=20)

add_frame = Frame(root)
add_frame.pack()

# labels
nl = Label(add_frame, text="Name")
nl.grid(row=0, column=0)

il = Label(add_frame, text="ID")
il.grid(row=0, column=1)

tl = Label(add_frame, text="Topics")
tl.grid(row=0, column=2)

#entry box

name_box = Entry(add_frame )
name_box.grid(row=1, column=0)

id_box = Entry(add_frame )
id_box.grid(row=1, column=1)

topics_box = Entry(add_frame )
topics_box.grid(row=1, column=2)

#add record function
def add_record():
    global count
    
    my_tree.insert(parent='', index='end',iid=count, text="", values=(name_box.get(), id_box.get(), topics_box.get()) )
    
    count += 1
    
    #  clear the entry boxes
    name_box.delete(0, END)
    id_box.delete(0, END)
    topics_box.delete(0, END)

#remove all records
def remove_all_records():
    for record in my_tree.get_children():
        my_tree.delete(record)

#remove one record
def remove_one():
   x =  my_tree.selection()[0]
   my_tree.delete(x)

#remove many
def remove_many():
   x =  my_tree.selection()
   for record in x:
       my_tree.delete(record)

# buttons
add_record = Button(root, text="Add Record", command=add_record )
add_record.pack(pady=20)

#remove all 
add_record = Button(root, text="Remove All", command=remove_all_records )
add_record.pack(pady=10)

# remove one
remove_one = Button(root, text="Remove One", command=remove_one )
remove_one.pack(pady=10)

# remove many
remove_many = Button(root, text="Remove Many", command=remove_many )
remove_many.pack(pady=10)

root.mainloop()