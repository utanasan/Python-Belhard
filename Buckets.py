print ("Suppose you have a 3 & 5 liter buckets. How could you measure exactly 4 liter using only those buckets and as much extra water as you need?")
is_work=True
n=0
b3=0
b5=0

while is_work:
  if b3==4 or b5==4:
        print(f"bucket#3: {b3}. bucket#5: {b5}.")
        print (f"You solved the task in {n} moves")
        break
  else:
        print(f"bucket#3: {b3}. bucket#5: {b5}.")
        user_inp=input("Enter your step: ")
        n+=1

        if user_inp in ('exit', 'q'):
            is_work=False

        elif b3==4 or b5==4:
          print (f"You solved the task in {n} moves")
         

        elif user_inp=='3_up' and b3<3:
            b3=3

        elif user_inp=='3_out' and b3>0:
            b3=0

        elif user_inp== '5_up' and b5<5:
            b5=5

        elif user_inp=='5_out' and b5>0:
           b5=0
  
        elif user_inp=='b5 to b3' and 0<(b3+b5)>=3: 
           b5=b5-(3-b3)
           b3=3
       
        elif user_inp=='b3 to b5' and 0<(b3+b5)>=5:
           b3=b3-(5-b5)
           b5=5

        elif user_inp=='b5 to b3' and 0<(b3+b5)<=3:
           b3=b3+b5
           b5=0

        elif user_inp=='b3 to b5' and 0<(b3+b5)<=5:
           b5=b3+b5
           b3=0