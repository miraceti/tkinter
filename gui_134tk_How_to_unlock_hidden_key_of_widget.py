from tkinter import *

root = Tk()
root.title('ERIC PY PROGRAM')
root.geometry('500x500')

def bla():
    pass

my_button = Button(root, text="click", command=bla)
my_button.pack()

my_entry = Entry(root)
my_entry.pack()

my_label = Label(root,
           text = "My Label",
           font = ("Helvetica",18),
           bd = 1, relief="sunken")
my_label.pack(pady=20, ipady=10, ipadx=10)

print("\nLabel\n")
for key in my_label.keys():
    print(key)
    
print(my_label["relief"])

print("\nEntry\n")
for key in my_entry.keys():
    print(key)
    
    
print("\nButton\n")
for key in my_button.keys():
    print(key)



root.mainloop()