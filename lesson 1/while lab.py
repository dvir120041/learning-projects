from random import randint
from time import sleep
while(1==1):
    a=input("welcome to the menu, please choose a number between 1 - 3")
    if(a=="1"):
        for n in range(1,101):
            print(n)
    elif(a=="2"):
        print("please enter 5 numbers and we will check if they create a fibo list")
        boolean = "true"
        b = int(input("enter first number"))
        c = int(input("enter second number"))
        d = int(input("enter third number"))
        e = int(input("enter forth number"))
        f = int(input("enter fitfh number"))
        list=[b,c,d,e,f]
        print(list)
        for i in range(2, len(list)):
            print(list[i])
            print(list[i - 1])
            print(list[i - 2])
            print("\n")
            if(list[i]!=list[i-1] + list[i-2]):
                boolean="false"
                break
        if(boolean=="true"):
            print("your list is fibo")
        else:
            print("your list is not fibo")
    elif(a=="3"):
        for i in range(10):
            boolean="true"
            c1 = randint(1, 12)
            sleep(0.5)
            print(c1)
            if(c1==12):
                print("nice, we got the right number!")
                boolean="false"
                break
            else:
                print("we got the wrong number, lets try again")
        if(boolean=="true"):
            sleep(2)
            print("we tried 10 times, game is over")