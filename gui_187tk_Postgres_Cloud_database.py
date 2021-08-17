from tkinter import *
import psycopg2

root = Tk()
root.title('postgres cloud database')
root.iconbitmap('ergo64.ico')
root.geometry('600x600')

def clear():
    f_name.delete(0, END)
    l_name.delete(0, END)

def query():
    conn = psycopg2.connect(
        host= "127.0.0.1",
        database= "postgresexemple",
        user= "postgres",
        password= "titan",
        port= "5432"
        
    )
    
    c = conn.cursor()
    
    # create tbl
    c.execute('''
              CREATE TABLE IF NOT EXISTS customers (
                  first_name TEXT,
                  last_name TEXT
              )
              
              ''')
    
    conn.commit()
    
    conn.close()

def submit():
    conn = psycopg2.connect(
        host= "127.0.0.1",
        database= "postgresexemple",
        user= "postgres",
        password= "titan",
        port= "5432"
        
    )
    
    c = conn.cursor()
    
    thing1 = f_name.get()
    thing2 = l_name.get()
    c.execute('''
              INSERT INTO customers(first_name, last_name)
              VALUES
              (%s, %s)''', (thing1, thing2)
              )

    conn.commit()
    
    conn.close()
    
    update()
    clear()

def update():
    conn = psycopg2.connect(
        host= "127.0.0.1",
        database= "postgresexemple",
        user= "postgres",
        password= "titan",
        port= "5432"
        
    )
    
    c = conn.cursor()
    
    c.execute(" SELECT * FROM customers")
    records = c.fetchall()
    
    output = ''
    
    for record in records :
        output_label.config(text=f'{output}\n{record[0]} {record[1]}') 
        output = output_label['text']
        
    conn.close()

my_frame = LabelFrame(root, text="postgres exemple")
my_frame.pack(pady=20)

f_label = Label(my_frame, text="first Name:")
f_label.grid(row=0, column=0, padx=10, pady=10)

f_name = Entry(my_frame, font=("helvetica, 18"))
f_name.grid(row=0, column=1, padx=10, pady=10)

l_label = Label(my_frame, text="last Name:")
l_label.grid(row=1, column=0, padx=10, pady=10)

l_name = Entry(my_frame, font=("helvetica, 18"))
l_name.grid(row=1, column=1, padx=10, pady=10)

submit_button = Button(my_frame, text="Submit", command=submit)
submit_button.grid(row=2, column=0, padx=10, pady=10)

update_button = Button(my_frame, text="Update", command=update)
update_button.grid(row=2, column=1, padx=10, pady=10)

output_label = Label(root, text="")
output_label.pack(pady=50)


query()

root.mainloop()
