from tkinter import *

root = Tk()
root.title('Mortgage Calculator')
root.iconbitmap('ergo64.ico')
root.geometry('500x400')

def payment():
    if amount_entry.get() and interest_entry.get() and term_entry.get():
        years = int(term_entry.get())
        months = years * 12
        rate = float(interest_entry.get())
        loan = int(amount_entry.get())
        
        # calculate
        # monthly interest rate
        monthly_rate = rate / 100 / 12
        
        payment = (monthly_rate / (1 - (1+ monthly_rate)**(-months))) * loan 
        
        # format payment
        payment = f"{payment:,.2f}"
        
        # output payment to the screen
        payment_label.config(text=f"Monthly payment : ${payment}")
                
    else:
        payment_label.config(text="Hey! You forgot to Enter Something !")

my_label_frame = LabelFrame(root, text="Mortgage Calculator")
my_label_frame.pack(pady=30)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=10, padx=20)

#define label and entry boxes
amount_label = Label(my_frame, text="Loan Amount")
amount_entry = Entry(my_frame, font=("helvetica", 18))

interest_label = Label(my_frame, text="Interest Rate")
interest_entry = Entry(my_frame, font=("helvetica", 18))

term_label = Label(my_frame, text="Term (years)")
term_entry = Entry(my_frame, font=("helvetica", 18))


#put label and entry boxes on the screen
amount_label.grid(row=0, column=0)
amount_entry.grid(row=0, column=1)
interest_label.grid(row=1, column=0)
interest_entry.grid(row=1, column=1, pady=20)
term_label.grid(row=2, column=0)
term_entry.grid(row=2, column=1)

my_button = Button(my_label_frame, text="Calculate Payment", command=payment)
my_button.pack(pady=20)

payment_label = Label(root, text="", font=("helvetica", 18))
payment_label.pack(pady =20)

root.mainloop()
