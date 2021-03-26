from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("400x400")

#1er panneau
panel_1 = PanedWindow(bd=6, relief="raised", bg="red")
panel_1.pack(fill=BOTH, expand=1)

left_label = Label(panel_1, text="left panel")
panel_1.add(left_label)


#second panneau
panel_2 = PanedWindow(panel_1, orient=VERTICAL, bd=6, relief="raised", bg="blue")
panel_1.add(panel_2)

top = Label(panel_2, text="top panel")
panel_2.add(top)

middle = Label(panel_2, text="middle panel")
panel_2.add(middle)

bottom = Label(panel_2, text="bottom panel")
panel_2.add(bottom)

root.mainloop()