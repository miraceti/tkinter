from tkinter import *
from PIL import ImageTk, Image
import requests 
import json

root = Tk()
root.geometry("400x400")

url="https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&format=json"


try:
    api_requests = requests.get(url)
    api = json.loads(api_requests.content)
except Exception as e:
    api = "error ..."

#print(api)

mylabel1=  Label(root, text="PLANETES").pack()
mylabel2= Label(root, text=str(len(api))).pack()

print("*********************************************************************************")

tmp = type(api)
print(tmp)
# print(str(api[0]['pl_hostname']) + ' - ' + str(api[0]['pl_name']))
# print(str(api[1]['pl_hostname']) + ' - ' + str(api[1]['pl_name']))
# print(str(api[2]['pl_hostname']) + ' - ' + str(api[2]['pl_name']))
print("*********************************************************************************")
print("Nombre de planetes : " + str(len(api)))
print("*********************************************************************************")
dt2 = '01/01/1990'
for planete in api:
    #print(str(api[i]['pl_hostname']) + ' - ' + str(api[i]['pl_name']))
    # print("Etoile : " + str(planete['pl_hostname']) + " ==>  PLANETES  : " + str(planete['pl_name'] + " ==>  RADJ  : " + str(planete['pl_radj'])) )
    dt1 = planete['rowupdate']
    diam = (planete['pl_radj'])
    temp = (planete['st_teff'])

    if diam==None:
        diam = 555.0

    if temp==None:
        temp = 0.0

    #diam = float((planete['pl_radj']))

    if dt1 > dt2:
        dt2 = dt1

    if diam < 0.1 and diam > 0.08 and temp > 6000.0 :
        print(
            "Etoile : " + str(planete['pl_hostname']) 
        + " ==>  PLANETES  : "  + str(planete['pl_name']) 
        + " ==>  RADJ  : " + str(planete['pl_radj']) 
        + " ==>  TEMP  : " + str(planete['st_teff']) 
        + " ==>  DIST  : " + str(planete['st_dist']) 
        )
        mylabel4= Label(root, text=str(planete['pl_name']) + " ==>  RADJ  : " + str(planete['pl_radj'])).pack()


print("*********************************************************************************")    
print(str(dt2))
mylabel3= Label(root, text= str(planete['pl_name'] + " : " + str(planete['pl_radj'])) ).pack()

mainloop()