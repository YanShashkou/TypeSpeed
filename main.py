import threading
import tkinter as tk
import random
import time
from threading import Thread
with open('russian_nouns.txt',encoding='utf-8') as file:
    data = file.readlines()
    words = [word.rstrip() for word in data]

screen = tk.Tk()
str =''
str_len = 0
while str_len < 2:
    str+=random.choice(words).lower()
    str+=' '
    str_len +=1

seconds = 0


def seconds_counter():
    global seconds
    while True:
        seconds += 1
        time.sleep(1)

thread = Thread(target=seconds_counter)
thread.start()
def check(text):
    global str
    if text == str:
        result = (len(str)*(60/seconds))/5
        print(result)
        label.config(text='dddd')
    return True
wrapper = (screen.register(check),'%P')

label = tk.Label(screen,text=str,background='Black',font=('Arial',12,'bold'),foreground='White',width=600)
label.pack()
entry = tk.Entry(screen,font=('Arial',12,'bold'),validate='key',validatecommand=wrapper)
entry.pack()
screen.title('TypeSpeed')
screen.configure(background='Black')
screen.geometry('1000x400')

screen.mainloop()
