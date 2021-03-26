from tkinter import *
from  tkhtmlview import HTMLLabel

root=Tk()
root.title('uing HTML')
root.iconbitmap('ergo64.ico')
root.geometry('500x600')

# my_label = HTMLLabel (root, html="<a href='https://codemy.com'> LEARN TO CODE </a>")
my_label = HTMLLabel (root, html="\
    <h1>\
        <a href='https://codemy.com'> LEARN TO CODE </a>\
    </h1>\
        <ol>\
        <li>One</li>\
        <li>Two</li>\
        <li>Three</li>\
        <li>Four</li>\
        </ol>\
        <ul>\
        <li><h4>One</h4></li>\
        <li><h5>Two</h5></li>\
        <li>Three</li>\
        <li>Four</li>\
        </ul>\
        <img src='https://cdn.codemy.com/wp-content/uploads/2015/01/sp21212.png'>\
        <img src = 'C:/Users/eric/Pictures/mando2.png'>\
    <pre><h1>\
        <a href='https://codemy.com'> LEARN TO CODE </a>\
    </h1></pre>\
        ")
my_label.pack(pady=20, padx=20, fill="both", expand= True)



root.mainloop()