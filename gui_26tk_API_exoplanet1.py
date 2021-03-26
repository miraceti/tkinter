from tkinter import *
from PIL import ImageTk, Image
import requests 
import json

root = Tk()
root.geometry("400x400")

url="https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&format=json"

def starlookup():
       
    api_requests = requests.get(url)
    api = json.loads(api_requests.content)
    mylabel1= Label(root, text="PLANETES TOTALES").pack()
    mylabel2= Label(root, text=str(len(api))).pack()

    starLabel = Label(root, text="ETOILE : " + str(star.get()))
    starLabel.pack()
    starN = star.get()
    print(starN)
    mylabel3= Label(root, text="PLANETES DE L'ETOILE").pack()
    for planete in api:
        if str(planete['pl_hostname']) == starN:
            mylabel4= Label(root, text=str(planete['pl_name']) + " ==>  RADJ  : " + str(planete['pl_radj'])).pack()

star = Entry(root)
star.pack()

starButton = Button(root, text="chercher étoile", command=starlookup)
starButton.pack()

mainloop()