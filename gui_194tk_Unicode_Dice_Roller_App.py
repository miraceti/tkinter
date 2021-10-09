from tkinter import *
import random

root = Tk()
root.title('Roll the Dice')
root.iconbitmap('ergo64.ico')
root.geometry('500x500')


# get the dice number
def get_number(x):
    if x == '\u2680':
        return (1)
    elif x == '\u2681':
        return(2)
    elif x == '\u2682':
        return(3)
    elif x == '\u2683':
        return(4)
    elif x == '\u2684':
        return(5)
    elif x == '\u2685':
        return(6)
    
    

# roll the dice
def roll_dice():
    # roll random dice
    d1 = random.choice(my_dice)
    d2 = random.choice(my_dice)
    
    # determine dice number
    sd1 = get_number(d1)
    sd2 = get_number(d2)
    
    # update label
    dice_label1.config(text=d1)
    dice_label2.config(text=d2)
    
    # update sub_labels
    sub_dice_label1.config(text=sd1)
    sub_dice_label2.config(text=sd2)
    
    # update total label
    total = sd1 + sd2
    total_label.config(text=f"You rolled: {total}")

# create liste dice (liste de dés)
my_dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']

# create a frame
my_frame = Frame(root)
my_frame.pack(pady = 20)

# create dice labels
dice_label1 = Label(my_frame, text='', font=("helvetica", 100), fg="blue")
dice_label1.grid(row=0, column=0, padx=5)

sub_dice_label1 = Label(my_frame, text="")
sub_dice_label1.grid(row=1, column=0)

dice_label2 = Label(my_frame, text='', font=("helvetica", 100), fg="red")
dice_label2.grid(row=0, column=1, padx=5)

sub_dice_label2= Label(my_frame, text="")
sub_dice_label2.grid(row=1, column=1)

# create a button
my_button = Button(root, text = "roll dice", command=roll_dice , font=("helvetica",24))
my_button.pack(pady=20)

# create totals
total_label = Label(root, text="", font=("helvetica",24), fg="grey")
total_label.pack(pady=40)


# roll the dices
roll_dice()

root.mainloop()
