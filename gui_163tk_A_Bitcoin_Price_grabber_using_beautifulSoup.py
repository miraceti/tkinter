from tkinter import *
from bs4 import BeautifulSoup
import urllib
from urllib import request
from datetime import datetime

root=Tk()
root.title('Bitcoin Price grabber')
root.geometry('600x210')
root.iconbitmap('ergo64.ico')
root.config(bg="black")

global previous
previous = False

#get current time
now = datetime.now()
# current_time = now.strftime("%H:%M:%S %p") #ici on aura 13h au lieu de 1h
current_time = now.strftime("%I:%M:%S %p")


#creating frame
my_frame = Frame(root, bg="black")
my_frame.pack(pady=20)

#define logo image
logo = PhotoImage(file='images/bitcoin1.png')

logo_label = Label(my_frame, image=logo, bd=0) 
logo_label.grid(row=0, column=0, rowspan=2,sticky="W")

#add bitcoin price label
bit_label = Label(my_frame, text="Ttttttttttttttttt", font= ("helvetica", 45), bg="black", fg="green", bd=0)
bit_label.grid(row=0, column=1, padx=20, sticky="S")

#latest price up/down
latest_price = Label(my_frame, text="ddd",font= ("helvetica", 8), bg="black", fg="grey", bd=0) 
latest_price.grid(row=1, column=1, padx=20, sticky="N")

#grab the bitcoin price
def Update():
    global previous
    
    #grab bitcoin price
    page = urllib.request.urlopen("https://www.coindesk.com/price/bitcoin").read()
    html = BeautifulSoup(page, "html.parser")
    price_large = html.find(class_="price-large")
    print(price_large)
    
    #convert to string
    price_large1 = str(price_large)
    # price_large2 = "0"
    
    #grab a slice that contain the price
    price_large2 = price_large1[54:63]
    
    #update our bitcoin label
    bit_label.config(text= f'${price_large2}')

    #set timer to 1 minute
    # 1 second = 1000
    root.after(30000, Update)
    
    #get current time
    now = datetime.now()
    # current_time = now.strftime("%H:%M:%S %p") #ici on aura 13h au lieu de 1h
    current_time = now.strftime("%I:%M:%S %p")
    
    #update status bar
    status_bar.config(text = f'Last Updated : {current_time}   ')
    
    #determine price change
    current = price_large2
    
    # remove coma
    current = current.replace(',', '')
    
    if previous:
        if float(previous) > float(current):
            latest_price.config(text=f"price down{round(float(previous)-float(current),2)}", fg="red")
            
        elif float(previous) == float(current):
            latest_price.config(text="price unchanged", fg="grey")
        
        else:
            latest_price.config(text=f"price down{round(float(current)-float(previous),2)}", fg="green")
            
    else:
        previous = current
        latest_price.config(text="price unchanged", fg="grey")

#create status bar
status_bar = Label(root, text=f'lastUpdated {current_time}    ',  bd=0 , anchor=E, bg="black", fg="grey")
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

#on program start run update function
Update()

mainloop()