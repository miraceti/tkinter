from tkinter import *
import pickle

root=Tk()
root.title('Liste déroulante!')
root.geometry('500x600')

#liste de tailles
sizes = ["Small", "Medium", "Large"]

my_text = Text(root, width=40, height=10)
my_text.pack(pady=10)

my_list = Listbox(root)
my_list.pack(pady=5)

for item in sizes:
    my_list.insert(END, item)

def save_file():
    #grab stuf from the text box
    stuff = my_text.get(1.0, END)
    
    #define a filename
    filename =  "dat_stuff"
    
    #open the file
    output_file = open(filename, 'wb')
    
    #add data to the file
    pickle.dump(stuff, output_file)
        

def open_file():
    #define a filename
    filename =  "dat_stuff"
    
    #open the file
    input_file = open(filename, 'rb')
    
    #load the data from the file into a variable
    stuff = pickle.load(input_file)
    
    print (stuff)
    #output to text box
    my_text.insert(1.0, stuff)
    
def save_list():
    #grab stuf from the list box
    stuff = my_list.get(0, END)
    
    #define a filename
    filename =  "dat_stuff"
    
    #open the file
    output_file = open(filename, 'wb')
    
    #add data to the file
    pickle.dump(stuff, output_file)
        

def open_list():
    #define a filename
    filename =  "dat_stuff"
    
    #open the file
    input_file = open(filename, 'rb')
    
    #load the data from the file into a variable
    stuff = pickle.load(input_file)
    
    print (stuff)
    #output to list box
    for item in stuff:
        my_list.insert(END, item)


def delete_items():
    my_list.delete(0, END)

my_button1 = Button(root, text = "save File", command = save_file)
my_button1.pack(pady=5)
my_button2 = Button(root, text = "open File", command = open_file)
my_button2.pack(pady=5)
my_button11 = Button(root, text = "save list", command = save_list)
my_button11.pack(pady=5)
my_button21 = Button(root, text = "open list", command = open_list)
my_button21.pack(pady=5)
my_button3 = Button(root, text = "delete_items", command = delete_items)
my_button3.pack(pady=5)



mainloop()