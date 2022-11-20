from tkinter import *
import random
from tkinter import messagebox, Label
from playsound import playsound

def play():
    playsound("sound1.mp3")


def clicked():
    rand1 = random.randint(1, 26)
    rand2 = random.randint(1, 26)
    code=''
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    code += str(min(rand1, rand2)) + ' '
    for i in range(min(rand1, rand2)-1, max(rand1, rand2)):
        code += letters[i]
    code += ' ' + str(max(rand1, rand2))

    play()
    messagebox.showinfo(title=None, message=code)

window = Tk()
window.title("Добро пожаловать в самое креативное приложение")
window.geometry('1280x720')
window.image = PhotoImage(file='csg')
bg_logo: Label = Label(window,image=window.image)
bg_logo.grid(row = 0,column = 0)
txt = Entry(window, width = 10)
txt.grid(column = 1, row=0)
txt.place(relx =.5, rely =.1, anchor = "c")
btn = Button(window, text="Cоздать ключ", bg = 'yellow', command=clicked)
btn.grid(column=2, row=0)
btn.place(relx=.5, rely=.5, anchor="c")
window.mainloop()

