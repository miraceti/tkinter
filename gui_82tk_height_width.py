from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("500x500")

def info():
    dimension_label = Label(root, text=root.winfo_geometry())
    dimension_label.pack(pady=10)

    height_label = Label(root, text="Height: "+ str(root.winfo_height()))
    height_label.pack(pady=10)

    width_label = Label(root, text="Width: "+ str(root.winfo_width()))
    width_label.pack(pady=10)

    x_label = Label(root, text="X: "+ str(root.winfo_x()))
    x_label.pack(pady=10)

    y_label = Label(root, text="Y: "+ str(root.winfo_y()))
    y_label.pack(pady=10)



my_button = Button(root, text="clickhere", command=info)
my_button.pack(pady=20)



root.mainloop()