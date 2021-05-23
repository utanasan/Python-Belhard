import tkinter as tk 
import datetime
from random import randint

def rnd():
    now=datetime.datetime.now()
    random_date=datetime.datetime(randint(2022,2100), randint(1,12),randint(1,31),randint(0,23),randint(0,59),randint(0,59))
    life_dif=random_date-now
    life_seconds=int(life_dif.total_seconds())
    yourData="Вы умрете: "+str(random_date)
    yourData1="Вам осталось жить: "+str(life_seconds)+" секунд"
    label1=tk.Label(text=yourData, font=("Comic Sans MS", 10, "bold"), fg="DarkOrchid3")
    label2=tk.Label(text=yourData1, font=("Comic Sans MS", 10, "bold"), fg="MediumPurple3")
    label1.pack()
    label2.pack()


window = tk.Tk()
window.title("Скажи, кукушка")
window.geometry("350x350")
window.iconbitmap("cuckoo.ico")



button2 = tk.Button(
    text="Сколько? Скажи, кукушка!",
    width=25,
    height=3,
    bg="SlateGray1",
    fg="purple1",
    font=("Verdana", 13, "bold"),
    activebackground="plum1",
    bd=5,
    command=rnd
)



button2.pack()


window.mainloop()