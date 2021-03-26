from tkinter import *
import PyPDF2
from tkinter import filedialog

root=Tk()
root.title('READ PDF!!')
root.geometry('500x500')

# create textbox
my_text = Text(root, height=30, width=60)
my_text.pack(pady=10)

def clear_text_box():
    my_text.delete(1.0, END)

def open_pdf():
    # grab the filename
    open_file = filedialog.askopenfilename(
        initialdir="D:\eric\python\perso\gui",
        title="Open PDF file",
        filetypes=(
            ("PDF files", "*.pdf"),
            ("All Files","*.*"))
        )
    #  check to see if there is a file
    if open_file:
        # open the pdf file
        pdf_file = PyPDF2.PdfFileReader(open_file)
        # set the page to read
        page = pdf_file.getPage(0)
        # extract the text from the pdf file
        page_stuff = page.extractText()
        # add text to textbox
        my_text.insert(1.0, page_stuff)

# create a menu
my_menu = Menu(root)
root.config(menu=my_menu)

# ajout option menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_pdf)
file_menu.add_command(label="Clear", command=clear_text_box)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

mainloop()