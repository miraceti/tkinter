from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.geometry("400x400")

conn = sqlite3.connect('address_book.db')

c = conn.cursor()

# c.execute("""
#             CREATE TABLE addresses (
#                 first_name text,
#                 last_name text,
#                 address text,
#                 city text,
#                 state text,
#                 zipcode integer
#             )
#             """)

def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("DELETE FROM addresses WHERE oid = "+ delete_box.get())

    conn.commit()
    conn.close()


def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode )",
            {
                'f_name':f_name.get(),
                'l_name':l_name.get(),
                'address':address.get(),
                'city':city.get(),
                'state':state.get(),
                'zipcode':zipcode.get()
            })
    
    conn.commit()
    conn.close()


    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)

    print_records=''
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6])+"\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    conn.commit()
    conn.close()

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1,padx=20, pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1,padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1,padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1,padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1,padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1,padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

f_name_label = Label(root, text="first name")
f_name_label.grid(row=0, column=0, pady=(10,0))
l_name_label = Label(root, text="last name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="city")
city_label.grid(row=3, column=0)
state_label = Label(root, text="state")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root,text="Delete ID")
delete_box_label.grid(row=9, column=0)


submit_btn = Button(root, text="ajouter un enregistrement a la base", command=submit)
submit_btn.grid(row=6,column=0, columnspan=2, pady=20, padx=20, ipadx=80)

query_btn = Button(root, text="show records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

delete_btn = Button(root, text="select record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

update_btn = Button(root, text="update record", command=delete)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=145)




conn.commit()
conn.close()


mainloop()