from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("800x600")

def resize():
    w = width_entry.get()
    h = heigth_entry.get()
    # root.geometry(str(w)+"x"+str(h))
    root.geometry(f"{w}x{h}")
    # root.geometry("{width}x{height}".format(width=w,height=h))
    # root.geometry("%ix%i" % (w,h))

width_label = Label(root, text="Width:")
width_label.pack(pady=20)
width_entry = Entry(root)
width_entry.pack()

heigth_label = Label(root, text="Heigth:")
heigth_label.pack(pady=20)
heigth_entry = Entry(root)
heigth_entry.pack()

my_button = Button(root, text="resize", command=resize)
my_button.pack(pady=20)


root.mainloop()