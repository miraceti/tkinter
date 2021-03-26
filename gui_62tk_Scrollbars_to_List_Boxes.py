from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("400x600")


#create a frame and scrollbar
my_frame = Frame(root)
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

#listebox : SINGLE, BROWSE, MULTIPLE, EXTENDED
my_listbox = Listbox(my_frame, width=50, yscrollcommand = my_scrollbar.set, selectmode=MULTIPLE)
#configure scrollbar
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_frame.pack()

my_listbox.pack(pady=15)

#ajout item a la listbox
my_listbox.insert(END, "ceci est un item")
my_listbox.insert(END, "second item")
my_listbox.insert(0, "troisieme item")

#ajout d'une liste d'item
my_list =["un","deux","trois","quatre","un","deux","trois","quatre","un","deux","trois","quatre","un","deux","trois","quatre","un","deux","trois","quatre","un","deux","trois","quatre"]

for item in my_list:
    my_listbox.insert(END, item)

my_listbox.insert(3, "nouveau item")

def delete_all():
    my_listbox.delete(0, END)

def delete():
    my_listbox.delete(ANCHOR)
    my_label.config(text='')

def select():
    my_label.config(text=my_listbox.get(ANCHOR))

def select_all():
    result=''
    # print(my_listbox.curselection())
    for item in my_listbox.curselection():
        result = result + str(my_listbox.get(item)) + '\n'

    my_label.config(text=result)

def delete_selected():
    for item in reversed(my_listbox.curselection()):
        my_listbox.delete(item)
        my_label.config(text='')



my_button = Button(root, text="Delete", command=delete)
my_button.pack(pady=10)

my_button2 = Button(root, text="Select", command=select)
my_button2.pack(pady=10)

global my_label
my_label = Label(root, text='')
my_label.pack(pady=10)

my_button3 = Button(root, text="Delete All", command=delete_all)
my_button3.pack(pady=10)

my_button4 = Button(root, text="Select All", command=select_all)
my_button4.pack(pady=10)

my_button5 = Button(root, text="Delete Selected", command=delete_selected)
my_button5.pack(pady=10)

root.mainloop()