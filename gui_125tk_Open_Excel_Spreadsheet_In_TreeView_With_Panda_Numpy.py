from tkinter import *
import pandas as pd
from tkinter import ttk, filedialog
# from tkinter import messagebox

root = Tk()
root.title('ERIC PY PROGRAM')
root.geometry("600x400")
# messagebox.showinfo("Showinfo", "Information")

# create file_open function
def file_open():
    filename = filedialog.askopenfilename(
        initialdir = "D:/eric/python/perso/gui/",
        title = "Open a Excel file",
        filetype = (("xlsx files","*.xlsx"),("All files","*.*"))
    )

    if filename:
        try:
            filename = r"{}".format(filename)
            df = pd.read_excel(filename)
        except ValueError:
            my_label.config(text="file could not be open ...try again")
        except FileNotFoundError:
            my_label.config(text="file could not be found ...try again")    
    
    # clear old treeview
    clear_tree()        
                
    #maj new treeview
    my_tree["column"]= list(df.columns)           
    my_tree["show"] = "headings"
    
    # loop thru column list pour entete
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)
    
    # put data in treeview
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)
 
    # pack the treeview finally
    my_tree.pack()
 
               
def clear_tree():
    my_tree.delete(*my_tree.get_children()) 
            
# creation frame
my_frame = Frame(root)
my_frame.pack(pady=20)

# create treeview
my_tree = ttk.Treeview(my_frame)

# add a menu
my_menu = Menu(root)
root.config(menu=my_menu)

# add menu drop down
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Spreadsheets", menu=file_menu)
file_menu.add_command(label="Open", command=file_open)


my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()