from tkinter import *
from tkcalendar import *

root = Tk()
root.title('ERIC PY')
root.geometry("600x400")


cal = Calendar(root,selectmode="day", year=2020, month=5, day=21 )
cal.pack(pady=20, fill="both", expand=True )

def grab_date():
    my_label.config(text="aujourd'hui nous sommes le " + cal.get_date())


my_button = Button(root, text="get date", command=grab_date)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()