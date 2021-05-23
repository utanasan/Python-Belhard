
from random import randint
import datetime
import time
year=int(input("Введите год:"))
month=int(input("Введите месяц:"))
day=int(input("Введите число месяца:"))
h=int(input("Введите час:"))
m=int(input("Введите минуту:"))
s=int(input("Введите секунду:"))
x=datetime.datetime(year,month,day,h,m,s)
now=datetime.datetime.now()
d=x-now
t=True
try:
 assert d.total_seconds()>0
#if d.total_seconds() > 0:
 while t:
    now=datetime.datetime.now()
    time.sleep(1)
    print('\r', now.strftime("%H:%M:%S"), end='')
    dif=x-now
    seconds=dif.total_seconds()
    seconds+=1
    if int(seconds)!=0:
        t=True
    elif int(seconds)==0:
        print("\t", "Звонок!") 
        t=False
except:
 print("Вы ввели прошедшее время!")         



        