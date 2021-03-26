from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("400x400")



my_label = Label(root, text='41' + u'\u00b0' , font=("helvetica",32)).pack(pady=10)

my_button = Button(root, text=u'\u00BB', font=("helvetica",32)).pack(pady=10)


root.mainloop()