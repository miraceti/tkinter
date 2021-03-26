from tkinter import *
# from tkinter import messagebox

root = Tk()
root.title('ERIC PY PROGRAM')

# designate height and width of our app
app_width = 500
app_height = 500

#find the screen width
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

#  largeur X hauteur X position x X position y de la fenetre
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
# messagebox.showinfo("Showinfo", "Information")


my_label = Label(root, text=f'width:{screen_width}  Height:{screen_height}')
my_label.pack(pady=20)








root.mainloop()