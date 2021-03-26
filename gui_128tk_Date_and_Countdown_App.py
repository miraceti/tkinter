from tkinter import *
from datetime import date

##################################################
'''
import locale
loc = locale.getlocale(locale.LC_ALL) # get current locale
locale.setlocale(locale.LC_ALL, 'de_DE') # use German locale; name might vary with platform
locale.strcoll('f\xe4n', 'foo') # compare a string containing an umlaut 
locale.setlocale(locale.LC_ALL, '') # use user's preferred locale
locale.setlocale(locale.LC_ALL, 'C') # use default (C) locale
locale.setlocale(locale.LC_ALL, loc) # restore saved locale

LANGUAGES = {
    'bg_BG': 'Bulgarian',
    'cs_CZ': 'Czech',
    'da_DK': 'Danish',
    'de_DE': 'German',
    'el_GR': 'Greek',
    'en_US': 'English',
    'es_ES': 'Spanish',
    'et_EE': 'Estonian',
    'fi_FI': 'Finnish',
    'fr_FR': 'French',
    'hr_HR': 'Croatian',
    'hu_HU': 'Hungarian',
    'it_IT': 'Italian',
    'lt_LT': 'Lithuanian',
    'lv_LV': 'Latvian',
    'nl_NL': 'Dutch',
    'no_NO': 'Norwegian',
    'pl_PL': 'Polish',
    'pt_PT': 'Portuguese',
    'ro_RO': 'Romanian',
    'ru_RU': 'Russian',
    'sk_SK': 'Slovak',
    'sl_SI': 'Slovenian',
    'sv_SE': 'Swedish',
    'tr_TR': 'Turkish',
    'zh_CN': 'Chinese',
}
'''

import locale
locale.setlocale(locale.LC_TIME,'')
 
import time
print (time.strftime('%A %d/%m/%Y %H:%M:%S'))

print(locale.setlocale(locale.LC_ALL, ''))
###################################################

root = Tk()
root.title('ERIC PY PROGRAM')
root.geometry('500x500')


panic = Label(root, text = "DON'T PANIC", font=("Helvetica",30),bg="black", fg="red")
panic.pack(pady=20, ipadx=10, ipady=10)

#get date
today = date.today()
print(today)

#format date
f_today = today.strftime("%A  -  %d/%m/%Y")
print(f_today)

#output date
today_label = Label(root, text=f'Today is the {f_today}')
today_label.pack(pady=20)

#count down
days_in_year = 365
todays_day_number = int(today.strftime("%j"))

#calculate day left in year
days_left = days_in_year - todays_day_number

#output days left
countdown_label = Label(root, text=f"Il ne reste que\n {days_left} jour(s) \ndans l'année en cours", font=("Helvetica", 20))
countdown_label.pack(pady=20)

root.mainloop()