import tkinter
import random
from tkinter import *
wndo = Tk()

def pk(s, s2, s3, d):
    s.config(bg="#00ff00")
    s2.config(bg="#fff")
    s3.config(bg="#fff")
    pleyr = d
    x = random.choice(["حجرة", "ورقة", "مقص"])
    l1["text"] = x
    l1.config(bg="red")

    l = "خسرت"
    k = "فوزت"
    if pleyr == x:
        l2["text"] = "تعادل"

    elif pleyr == "حجرة" and x == "ورقة":
        l2["text"] = l
    elif pleyr == "حجرة" and x == "مقص":
        l2["text"] = k

    elif pleyr == "ورقة" and x == "حجرة":
        l2["text"] = k
    elif pleyr == "ورقة" and x == "مقص":
        l2["text"] = l

    elif pleyr == "مقص" and x == "حجرة":
        l2["text"] = l
    elif pleyr == "مقص" and x == "ورقة":
        l2["text"] = k

    l2.config(bg="#000")



l1 = Label(wndo, text='', height=10 , width=20)

l2 = Label(wndo, text='', height=10 , width=20, fg="red")

l1.grid(row=1, column=1)
l2.grid(row=2, column=1)





b1 = Button(wndo, text="حجرة", height=10 , width=20, command=lambda :pk(b1, b2, b3, "حجرة"))
b2 = Button(wndo, text="ورقة", height=10 , width=20, command=lambda :pk(b2, b1, b3, "ورقة"))
b3 = Button(wndo, text="مقص", height=10 , width=20, command=lambda :pk(b3, b2, b1, "مقص"))


b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)


wndo.mainloop()