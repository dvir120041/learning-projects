from random import randint
from time import sleep
while(True):
    print("welcome to the lottery! in each game you will have to guess 7 numbers between 1 - 37,"
          "for any amount of numbers above 3 you guessed right there is a price."
          "\n3 numbers = 10 ILS \n4 numbers = 100 ILS \n5 numbers = 5000 ILS "
          "\n6 numbers = 1M ILS ")
    money = int(input("each game costs 3 shekels, please enter how much money you want to spend."))
    games = money//3
    change = money%3
    print("games:" + str(games) + "\nchange:" + str(change) + "\nlet's begin!" +"\n---------------------------------------")
    for i in range(games):
        num = 0
        number1 = input("please enter your 1 number")
        number2 = input("please enter your 2 number")
        number3 = input("please enter your 3 number")
        number4 = input("please enter your 4 number")
        number5 = input("please enter your 5 number")
        number6 = input("please enter your 6 number")
        number= input("please enter your lucky number")
        my_list = list([number1] + [number2] + [number3] + [number4] + [number5] + [number6] + [number])
        c1 = randint(1, 37)
        c2 = randint(1, 37)
        c3 = randint(1, 37)
        c4 = randint(1, 37)
        c5 = randint(1, 37)
        c6 = randint(1, 37)
        c7 = randint(1, 37)
        print("the numbers are: " + str(c1) + " " + str(c2)+ " " + str(c3) + " " + str(c4) + " " + str(c5) + " " + str(c6) + " lucky number:" + str(c7))
        print("your numbers are: " + number1 + " "  + number2 + " " + number3 + " " + number4 + " " + number5 + " " + number6 + " lucky number: " + number)
        for b in range(int(len(my_list))):
            if int(my_list[b]) == c1 or int(my_list[b]) == c2 or int(my_list[b]) == c3 or int(my_list[b]) == c4 or int(my_list[b]) == c5 or int(my_list[b]) == c6 or int(my_list[b]) == c7:
                num=num+1
        if num == 3:
            print("congrats! you won 10ILS")
        elif num == 4:
            print("congrats! you won 100ILS")
        elif num ==5:
            print("congrats! you won the second most biggest price, 5000ILS!!!")
        elif num == 6 or num == 7:
            print("congrats! you won the big prize, 1M SHEKELS!!!!!")
        else:
            print("you won nothing, maybe next time!")
    hf=input("do you want to give it another shot? y/n")
    if hf == "n" or hf == "no":
        print("ok, goodBye!")

