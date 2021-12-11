from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox
import pyttsx3

root = Tk()
root.title('translator')
root.iconbitmap('ergo64.ico')
root.geometry('880x300')

# language_list=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)
# grab language list from googletrans
languages = googletrans.LANGUAGES
print(languages)

# convert to list
language_list = list(languages.values())
print(language_list)

def translate_it():
    # delete any previous translations
    translated_text.delete(1.0, END)
    try:
        # get languages from dict keys
        # get from language key
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_language_key = key
        
        # get to language key
        for key, value in languages.items():
            if (value == translated_combo.get()):
                to_language_key = key
        # turn original text into a textblob
        words = textblob.TextBlob(original_text.get(1.0, END))
        
        # translate text
        words = words.translate(from_lang= from_language_key , to=to_language_key)
        
        # output translated text to screen
        translated_text.insert(1.0, words)
        
        # initialize the speech engine
        engine = pyttsx3.init()
       
        # play with voices
        # voices = engine.getProperty("voices")
        # for voice in voices:
        #     engine.setProperty('voice', voice.id)
        #     engine.say(words)
        #     print(voice.id)
       
        # pass text to speech engine
        engine.say(words)
        
        # run the engine
        engine.runAndWait()
        
    except Exception as e:
        messagebox.showerror("Translator",e)

def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)
    
# text boxes
original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(root, text="Translate!", font=("helvetica,24"), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, pady=20, padx=10)

# combo boxes
original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21) #21 english
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(26) #26 french
translated_combo.grid(row=1, column=2)

# clear button
clear_button = Button(root, text="clear", command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()
