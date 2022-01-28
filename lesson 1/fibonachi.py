from time import sleep
list = [1, 2]
while(1==1):
    c=int(list[-1]) + int(list [-2])
    list=list+[c]
    print(list)
    sleep(2)
