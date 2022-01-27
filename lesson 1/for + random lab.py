from random import randint
from time import sleep
num1=0
print("welcome to the cubes game,read below for the rules: \neach game costs 3 shekels, in each turn two cubes will give us two random numbers,"
        "if the numbers are standing by one of the rules below you will win the prize: \n1.matched number = 100 shekels \n2.matched number and it equles to 6 = 1000 shekels"
        "\n3.first cube equels to 1 = 20 shekels \n4.second cube equels to 2 = 40 shekels \nat the end of the game you will see your pay check which will include your prize money and change"
        "\nG00000D LUCK!!!")
sleep(3)
m=input("please enter how much money you want to spend")
change=int(m)%3
games=int(m)//3
print("ok, you have " + str(games) +" turns, lets start")
sleep(1)
for num in range(int(games)):
    c1 = int(randint(1, 6))
    c2 = int(randint(1, 6))
    print("game is loading just a second")
    sleep(2)
    if (c1 == c2 & c1 == 6):
        print("mazal tov, you just won the big pot - 1000 shekels!!")
        print(str(c1) + " " + str(c2))
        num1 = num1 + 1000
    elif(c1==c2):
        print("mazal tov, you just won 100 shekels!")
        print(str(c1) + " " + str(c2))
        num1=num1+100
    elif(c2==2):
        print("mazal tov, you just won 40 shekels!")
        print(str(c1) + " " + str(c2))
        num1=num1+40
    elif(c1==1):
        print("mazal tov, you just won 20 shekels!")
        print(str(c1) + " " + str(c2))
        num1=num1+20
    else:
        print("this turn you got nothing")
        print(str(c1) + " " + str(c2))
print("\n\n")
print("amount of money you have won:" + str(num1) + "\nyour change: " + str(change))