import tkinter as tk
from tkinter import *
import speech_recognition as sr
from translate import Translator


global counter
counter = 2

window = tk.Tk()
window.title("تبدیل صدا به متن ")
window.minsize(400,400)
window.maxsize(400,400)



def widgets():
    start_label = Label(window, text=" لطفا صحبت کنید")
    start_label.config(font=("Lalezar", 22, "bold"), bg="pink", width=24)
    start_label.grid(row=0)
    
    start_button = Button(window, text="شروع", command=get_voice)
    start_button.config(font=("aviny", 20), bg="lightblue", fg="black")
    start_button.grid(row=1, pady=20)
 
 
 
r = sr.Recognizer()
 
 
def get_voice():
    try:
        with sr.Microphone() as src:
           audio = r.listen(src)
           text = r.recognize_bing(audio)
           text = text.lower()
           translator = Translator(to_lang="fa")
           text = translator.translate(text)
           show_text(text)
           
    except:
        pass

def show_text(text):
    global counter
    label_name = f"label_{counter}"
    label_name = Label(text=text)
    label_name.config(font=("aviny", 16))
    label_name.grid(row=counter)
    counter += 1
    


widgets()

window.mainloop()