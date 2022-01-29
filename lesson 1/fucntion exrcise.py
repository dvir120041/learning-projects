from time import sleep
from random import randint
def menu(a):
    if a=="1":
        dog()
    elif a=="2":
        friends()
    elif a=="3":
        n_azzeret()
    else:
        print("your entered a wrong number!")
def dog():
    n = input("please enter the dog's name: ")
    a = input("please enter the dog's age: ")
    ha=int(a)*7
    print("the dog's name is: " + n + "\nthe dog's age in human years is: " + str(ha))
def friends():
    name1=input("enter friend number 1 name")
    name2 = input("enter friend number 2 name")
    name3=input("enter friend number 3 name")
    name4 = input("enter friend number 4 name")
    name=input("please enter a friends name")
    if (name==name1 or name==name2 or name==name3 or name==name4):
        print("your friends name is in the list")
    else:
        print("the name is out of the list")
def n_azzeret():
    c1=randint(1,7)
    print("the number that we got on the lottery is: " + str(c1))
    sleep(1)
    c2=1
    for i in range (1,c1+1):
        c2=c2*i
    print("the n azzeret for this number is:" + str(c2))
while(1==1):
    choice=input("welcome to the menu, please pick one of the options: \n.1dogs details \n2.friends list \n3.n azzeret")
    menu(choice)
    q=input("do you want onther round? y/n")
    if q=="n":
        print("ok goodbye")
        break