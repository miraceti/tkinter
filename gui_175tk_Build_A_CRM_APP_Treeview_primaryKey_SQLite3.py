from tkinter import *
from tkinter import ttk
import sqlite3


root = Tk()
root.title('TreeBase')
root.iconbitmap('ergo64.ico')
root.geometry('1000x500')
root.resizable(True, True)  # largeur , hauteur

'''
# add data
data = [
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
'''
# database config
# create database or coonect to an exist one
conn = sqlite3.connect('tree_crm.db')

# create a cursor
c = conn.cursor()

# create table
c.execute("""CREATE TABLE if not exists customers 
            (
            first_name text,
            last_name text,
            id integer,
            address text,
            city text,
            state text,
            zipcode text
            )
        """)

# add data to the table
'''
for record in data:
    c.execute("INSERT INTO customers VALUES (:first_name, :last_name, :id, :address, :city, :state, :zipcode) " , 
              {
                  'first_name': record[0],
                  'last_name':  record[1],
                  'id':         record[2],
                  'address':    record[3],
                  'city':       record[4],
                  'state':      record[5],
                  'zipcode':    record[6]
              }
              )
'''
# commit changes
conn.commit()

# close connection
conn.close()


def query_database():
    conn = sqlite3.connect('tree_crm.db')

    # create a cursor
    c = conn.cursor()
    
    c.execute("SELECT rowid, * FROM customers")
    records = c.fetchall()
    print(records)
    # add data to the screen
    global count
    count = 0

    for record in records:
        print(record)
    
    for record in records:
        if count % 2 == 0:  # even
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2],
                                                                            record[0], record[4],
                                                                            record[5], record[6],
                                                                            record[7]), tags=('evenrow', ))

        else:  # odd row
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2],
                                                                            record[0], record[4],
                                                                            record[5], record[6],
                                                                            record[7]), tags=('oddrow', ))
        # increment count
        count += 1
    
    # commit changes
    conn.commit()

    # close connection
    conn.close()


# add style
style = ttk.Style()

# pick theme
style.theme_use('default')

# configure treeview color
style.configure("Treview",
                background="#d3d3d3",
                foreground="black",
                rowheight=25,
                fieldbackground="#d3d3d3")

# change selected color
style.map('Treeview',
          background=[('selected', "#347083")])


# create treeview frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# create treeview scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)


# create the treeview
my_tree = ttk.Treeview(
    tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# configure scrollbar
tree_scroll.config(command=my_tree.yview)


# define our column
my_tree['columns'] = ("First Name", "Last Name", "ID",
                      "Address", "City", "State", "Zipcode")

# format our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("First Name", anchor=W, width=140)
my_tree.column("Last Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Address", anchor=CENTER, width=140)
my_tree.column("City", anchor=CENTER, width=140)
my_tree.column("State", anchor=CENTER, width=140)
my_tree.column("Zipcode", anchor=CENTER, width=140)

# create headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Address", text="Address", anchor=CENTER)
my_tree.heading("City", text="City", anchor=CENTER)
my_tree.heading("State", text="State", anchor=CENTER)
my_tree.heading("Zipcode", text="Zipcode", anchor=CENTER)




# create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")




# add record entry boxes
data_frame = LabelFrame(root, text="record")
data_frame.pack(fill=X, expand="yes", padx=20)

fn_label = Label(data_frame, text="First Name")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)

ln_label = Label(data_frame, text="Last Name")
ln_label.grid(row=0, column=2, padx=10, pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0, column=3, padx=10, pady=10)

id_label = Label(data_frame, text="ID")
id_label.grid(row=0, column=4, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=5, padx=10, pady=10)

address_label = Label(data_frame, text="address")
address_label.grid(row=1, column=0, padx=10, pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=1, column=1, padx=10, pady=10)

city_label = Label(data_frame, text="City")
city_label.grid(row=1, column=2, padx=10, pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1, column=3, padx=10, pady=10)

state_label = Label(data_frame, text="state")
state_label.grid(row=1, column=4, padx=10, pady=10)
state_entry = Entry(data_frame)
state_entry.grid(row=1, column=5, padx=10, pady=10)

zipcode_label = Label(data_frame, text="Zipcode")
zipcode_label.grid(row=1, column=6, padx=10, pady=10)
zipcode_entry = Entry(data_frame)
zipcode_entry.grid(row=1, column=7, padx=10, pady=10)

# move row up
def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

# move row down
def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

# remove 1 record
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

# remove many records
def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)
        
# remove all records
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)

#clear entry boxes
def clear_entries():
    # clear entrybox
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)
    


# select record
def select_record(e):
    # clear entrybox
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)
    
    # grab record number
    selected = my_tree.focus()
    # grab record value
    values = my_tree.item(selected, 'values')
    
    # output values to entrybox
    fn_entry.insert(0, values[0])
    ln_entry.insert(0, values[1])
    id_entry.insert(0, values[2])
    address_entry.insert(0, values[3])
    city_entry.insert(0, values[4])
    state_entry.insert(0, values[5])
    zipcode_entry.insert(0, values[6])
    

# update record 
def update_record():
    # grab record number
    selected = my_tree.focus()
    # update record
    my_tree.item(selected, text="", values=(fn_entry.get(),ln_entry.get(),id_entry.get(),
                                            address_entry.get(),city_entry.get(),state_entry.get(),
                                            zipcode_entry.get(),))
     # clear entrybox
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)
    

# add buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill=X, expand="yes", padx=20, )

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record")
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down", command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = Button(button_frame, text="Clear Entry boxes", command= clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

# bind the treeview
my_tree.bind("<ButtonRelease-1>", select_record)

#run to pull data from database on start
query_database()



root.mainloop()
