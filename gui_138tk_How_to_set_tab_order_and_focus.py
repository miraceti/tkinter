from tkinter import *

root = Tk()
root.title('ERIC PY PROGRAM')
root.geometry('500x500')

red = Entry(root, bg="red", font=("Helvetica,20"))
white=Entry(root, bg="white", font=("Helvetica,20"))
blue=Entry(root, bg="blue", font=("Helvetica,20"))

red.pack(pady=20)
white.pack(pady=20)
blue.pack(pady=20)

#focus
red.focus()

# change tab order
def change_tab_order():
    blue.focus()
    widgets = [blue,white,red]
    for w in widgets:
        w.lift()

my_button = Button(root, text="tab order", command=change_tab_order)
my_button.pack(pady=20)

root.mainloop()