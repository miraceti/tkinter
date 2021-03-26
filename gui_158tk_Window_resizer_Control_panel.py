from tkinter import *
from tkinter import ttk

root=Tk()
root.title('Liste déroulante!')
root.geometry('600x600')

def launch():
    global second
    second = Toplevel()
    second.geometry("200x200")

def width_slide(x):
    
    second.geometry(f"{int(width_slider.get())}x{int(height_slider.get())}")

def height_slide(y):
    second.geometry(f"{int(width_slider.get())}x{int(height_slider.get())}")

def both_slide(x):
    second.geometry(f"{int(both_slider.get())}x{int(both_slider.get())}")

# create a launch window
launch_button = Button(root, text="Launch Window", command= launch)
launch_button.pack(pady=20)

width_frame = LabelFrame(root, text="Width")
width_frame.pack(pady=20)

height_frame = LabelFrame(root, text="Height")
height_frame.pack(pady=20)

both_frame = LabelFrame(root, text="Both")
both_frame.pack(pady=20)

width_slider = ttk.Scale(width_frame, from_=100, to=500, orient=HORIZONTAL, length=200, command=width_slide, value=100)
width_slider.pack(pady=20, padx=20)

height_slider = ttk.Scale(height_frame, from_=100, to=500, orient= VERTICAL, length=200, command= height_slide, value=100)
height_slider.pack(pady=20, padx=20)

both_slider = ttk.Scale(both_frame, from_=100, to=500, orient=HORIZONTAL, length=200, command=both_slide, value=100 )
both_slider.pack(pady=20, padx=20)

mainloop()