from tkinter import *
from PIL import ImageTk, Image
import requests 
import json

root = Tk()
root.geometry("400x400")

url="http://www.infoclimat.fr/public-api/gfs/json?_ll=48.85341,2.3488&_auth=BhxSRQB%2BUHIFKFptAHZWfwVtU2ZbLVdwUS1SMQFkAH1ROgVkVTVcOgBuVyoCLVFnUn9UNw80VGRROlIqWihfPgZsUj4Aa1A3BWpaPwAvVn0FK1MyW3tXcFE7UjQBcgBiUTQFYVUoXD8AaFcyAixRbVJkVCsPL1RtUTdSPVo%2FXz4GYFI0AGFQMgVpWicAL1ZnBWNTYls1VzxRZ1I3AT4AZ1E6BWlVY1w6AGZXKwI0UWJSZ1QyDzVUbVEyUjBaKF8jBhxSRQB%2BUHIFKFptAHZWfwVjU21bMA%3D%3D&_c=fef155e5cf06c38cdb0f0aa6a97d9239"


try:
    api_requests = requests.get(url)
    api = json.loads(api_requests.content)
except Exception as e:
    api = "error ..."

print(api)

mylabel0 =  Label(root, text="PRESSION").pack()
mylabel = Label(root, text=str(api["2020-04-29 17:00:00"]["pression"])+'\n' + str(api["2020-04-29 20:00:00"]["pression"]))
mylabel.pack()

mylabel1= Label(root, text=str(api["2020-04-29 23:00:00"]["pression"]['niveau_de_la_mer'])+'\n' + str(api["2020-04-30 02:00:00"]["pression"]))
mylabel1.pack()
print("*********************************************************************************")
for item in api.items():
 
    print("date : " + str(item[0]) + " - " + str(item[1]) )
    print("*************************************************")
    print("2nd : " + str(item[1]))
    d2nd = item[1]
    print(d2nd)
    temp = type(d2nd)
    print(temp)
    #print(str(item[0])[0:3])
    if str(item[0])[0:4]=="2020":
        t1 = d2nd["temperature"]
        t2 = d2nd["pression"]
        print(t1['sol'])
        print(t2)
    print("*************************************************")
mainloop()