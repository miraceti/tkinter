from tkinter import *
from tkinter import ttk

root=Tk()
root.title('TreeBase')
root.iconbitmap('ergo64.ico')
root.geometry('1000x500')
root.resizable(True, True)  #largeur , hauteur

#add style
style = ttk.Style()

#pick theme
style.theme_use('default')

# configure treeview color
style.configure("Treview", 
                background="#d3d3d3",
                foreground="black",
                rowheight=25,
                fieldbackground="#d3d3d3")

# change selected color
style.map('Treeview',
          background=[('selected',"#347083")])


# create treeview frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# create treeview scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)


#create the treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended" )
my_tree.pack()

#configure scrollbar
tree_scroll.config(command=my_tree.yview)


#define our column
my_tree['columns']=("First Name", "Last Name", "ID", "Address", "City", "State", "Zipcode") 

#format our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("First Name", anchor=W, width=140)
my_tree.column("Last Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Address", anchor=CENTER, width=140)
my_tree.column("City", anchor=CENTER, width=140)
my_tree.column("State", anchor=CENTER, width=140)
my_tree.column("Zipcode", anchor=CENTER, width=140)

#create headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Address", text="Address", anchor=CENTER)
my_tree.heading("City", text="City", anchor=CENTER)
my_tree.heading("State", text="State", anchor=CENTER)
my_tree.heading("Zipcode", text="Zipcode", anchor=CENTER)

# add data
data=[
    ["John1", "ELDER1", 1, "1231 elder street", "Las vegas", "texas", "3332221"],
    ["John2", "ELDER2", 2, "1232 elder street", "paris", "florida", "3332222"],
    ["John3", "ELDER3", 3, "1233 elder street", "otawa", "california", "3332223"],
    ["John4", "ELDER4", 4, "1234 elder street", "rennes", "oklahoma", "3332224"],
    ["John5", "ELDER5", 5, "1235 elder street", "tokyo", "georgia", "3332225"],
    ["John6", "ELDER6", 6, "1236 elder street", "berlin", "michigan", "3332226"],
    ["John7", "ELDER7", 7, "1273 elder street", "moscou", "allabama", "3332227"],
    ["John8", "ELDER8", 8, "1238 elder street", "pekin", "wyioming", "3332228"],
    ["John9", "ELDER9", 9, "1293 elder street", "dubai", "missouri", "3332229"],
    ["John10", "ELDER10", 10, "123A elder street", "rome", "virginia", "33322210"],
    ["John1", "ELDER1", 1, "1231 elder street", "Las vegas", "texas", "3332221"],
    ["John2", "ELDER2", 2, "1232 elder street", "paris", "florida", "3332222"],
    ["John3", "ELDER3", 3, "1233 elder street", "otawa", "california", "3332223"],
    ["John4", "ELDER4", 4, "1234 elder street", "rennes", "oklahoma", "3332224"],
    ["John5", "ELDER5", 5, "1235 elder street", "tokyo", "georgia", "3332225"],
    ["John6", "ELDER6", 6, "1236 elder street", "berlin", "michigan", "3332226"],
    ["John7", "ELDER7", 7, "1273 elder street", "moscou", "allabama", "3332227"],
    ["John8", "ELDER8", 8, "1238 elder street", "pekin", "wyioming", "3332228"],
    ["John9", "ELDER9", 9, "1293 elder street", "dubai", "missouri", "3332229"],
    ["John10", "ELDER10", 10, "123A elder street", "rome", "virginia", "333222109"]
    
]



# create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")


#add data to the screen
global count
count=0

for record in data:
    if count % 2 == 0: #even
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], 
                                                                           record[2], record[3], 
                                                                           record[4], record[5], 
                                                                           record[6]), tags=('evenrow', ))
        
    else:  #odd row
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], 
                                                                           record[2], record[3], 
                                                                           record[4], record[5], 
                                                                           record[6]), tags=('oddrow', ))
    #increment count
    count += 1   

#add record entry boxes
data_frame = LabelFrame(root, text="record")
data_frame.pack(fill=X, expand="yes", padx=20)

fn_label = Label(data_frame, text="First Name")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = Entry(data_frame )
fn_entry.grid(row=0, column=1, padx=10, pady=10)

ln_label = Label(data_frame, text="Last Name")
ln_label.grid(row=0, column=2, padx=10, pady=10)
ln_entry = Entry(data_frame )
ln_entry.grid(row=0, column=3, padx=10, pady=10)

id_label = Label(data_frame, text="ID")
id_label.grid(row=0, column=4, padx=10, pady=10)
id_entry = Entry(data_frame )
id_entry.grid(row=0, column=5, padx=10, pady=10)

address_label = Label(data_frame, text="address")
address_label.grid(row=1, column=0, padx=10, pady=10)
address_entry = Entry(data_frame )
address_entry.grid(row=1, column=1, padx=10, pady=10)

city_label = Label(data_frame, text="City")
city_label.grid(row=1, column=2, padx=10, pady=10)
city_entry = Entry(data_frame )
city_entry.grid(row=1, column=3, padx=10, pady=10)

state_label = Label(data_frame, text="state")
state_label.grid(row=1, column=4, padx=10, pady=10)
state_entry = Entry(data_frame )
state_entry.grid(row=1, column=5, padx=10, pady=10)

zipcode_label = Label(data_frame, text="Zipcode")
zipcode_label.grid(row=1, column=6, padx=10, pady=10)
zipcode_entry = Entry(data_frame )
zipcode_entry.grid(row=1, column=7, padx=10, pady=10)




#add buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill=X , expand="yes", padx=20, )

update_button = Button(button_frame, text="Update Record")
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record")
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All")
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected")
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected")
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up")
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down")
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = Button(button_frame, text="Select Record")
select_record_button.grid(row=0, column=7, padx=10, pady=10)
# n





root.mainloop()