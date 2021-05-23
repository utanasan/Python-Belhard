from random import randint
import time
import os
t=True
n=0
now=int(time.time())
x=now+randint(60,300) 
while t:
     if int(time.time())==x:
         n+=1
         print('Drink up!')
         time.sleep(5)
         os.system('cls')
         now=int(time.time())
         x=now+randint(60,300)
         if n<5:
             print(f"You drank {n} glasses ")
             print(time.strftime("%H:%M:%S"))
             continue
         elif n>=5:
             print("It's time to go home!")
             print(f"You have already drunk  {n} glasses")
             print(time.strftime("%H:%M:%S"))
             t=False
