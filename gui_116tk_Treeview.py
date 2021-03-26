from tkinter import *
from tkinter import ttk

root = Tk()
root.title('ERIC PY PROGRAM')
root.geometry("500x500")


my_tree = ttk.Treeview(root )

#define our columns
my_tree['columns'] = ("Name", "ID", "Favorite Pizza")

#formatage des colonnes
my_tree.column("#0", width=0, stretch=NO)
# my_tree.column("#0", width=0, minwidth=0)
my_tree.column("Name", anchor=W,width=120, minwidth=2)
my_tree.column("ID", anchor=CENTER, width=80, minwidth=5)
my_tree.column("Favorite Pizza", anchor=W, width=120, minwidth=10)

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


root.mainloop()