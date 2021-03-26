from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("700x500")


my_canvas = Canvas(root, width=300, height=300, bg="white")
my_canvas.pack(pady=20)



#rectangle avant la ligne donc au dessous
# my_canvas.create_rectangle(x1, y1, x2, y2, fill="pink")
# x1 et y1 :  en haut a gauche
# x2 et y2 : en bas a droite
my_canvas.create_rectangle(50, 150, 250, 50, fill="pink")



#ellipse ou ovale
# x1 et y1 :  en haut a gauche
# x2 et y2 : en bas a droite
my_canvas.create_oval(50,150,250,50, fill="cyan")

#line
# my_canvas.create_line(x1, y1, x2, y2, fill="color")
my_canvas.create_line(0, 100, 300, 100, fill="red")
my_canvas.create_line(150, 0, 150, 200, fill="red")








root.mainloop()