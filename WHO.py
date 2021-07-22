# Кто виноват?
import random
import csv
from tkinter import *
def whois():
    spis = list()
    filename = "spisok.csv"
    with open(filename,'r', encoding="windows-1251") as r_file:
        reader = csv.reader(r_file, delimiter=" ")
        for row in reader:
            spis.append(row)
    who = random.choice(spis)
    return who
root = Tk()
root.title("Кто виноват?")
root.geometry("400x300+500+500")
clik = 0
def clicked():
    global clik
    clik = clik + 1
    btntxt.set("Это {}".format(whois()))
btntxt = StringVar()
btntxt.set("Кто виноват?")
btn = Button(root, textvariable=btntxt,
             padx="20",
             pady="8",
             font="Impact 18", command=clicked)
btn.place(relx=.2, rely=.1)
btn1 = Button(root, text="Наказать",
             padx="20",
             pady="8",
             font="Impact 18")
btn1.place(relx=.25, rely=.5)


root.mainloop()