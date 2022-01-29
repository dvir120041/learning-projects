import os
adds={"www.google.com":"1.1.1.1","www.facebook.com":"2.2.2.2","www.instagram.com":"3.3.3.3"}
def menu():
    first_menu=input("welcome to my final project! \nplease choose between the two options: \n1.IP system \n2.dns system")
    if first_menu=="1":
        ip_system=input("welcome to the ip system, here are the options for you: \n1.search for ip address in a list"
                        "\n2.add ip address to a list \n3.delete ip address from the list \n4. print all the ip addresses to the screen")
        if ip_system=="1":
            ip_check()
        if ip_system=="2":
            ip_add()
        if ip_system=="3":
            ip_del()
        if ip_system=="4":
            ip_show()
    elif first_menu=="2":
        dns_system=input("welccome to the dns system, here are the options for you: \n1.search for a url in a dictionary \n2.add url + ip address to a dictionary"
                         "\n3.delete url from the dictionary \n4.update ip of a specific url \n5.print all the url:ip to the screen")
        if dns_system=="1":
            url_search()
        elif dns_system=="2":
            url_ip_add()



def ip_check():
    boolean="true"
    ip_path=("C:/Users/Own/OneDrive/שולחן העבודה/קורס סייבר/קוד לפתיחת קובץ/ip addresses for project.txt")
    ip_read = open(ip_path,"r")
    string=ip_read.read().splitlines()
    print(len(string))
    ip_in=input("please ip address")
    for i in range(len(string)):
        c=string[i]
        if ip_in==c:
            boolean="false"
            break
    if boolean=="true":
        print("the IP is not in the list!")
    else:
        print("the IP is in the list!")
    ip_read.close()
def ip_add():
    ip_path = ("C:/Users/Own/OneDrive/שולחן העבודה/קורס סייבר/קוד לפתיחת קובץ/ip addresses for project.txt")
    ip_read = open(ip_path, "a+")
    ip_add=input("please enter the IP address you want to add")
    ip_read.write("\n" + ip_add)
    ip_read.close()
def ip_del():
    print("?")
def ip_show():
    ip_path = ("C:/Users/Own/OneDrive/שולחן העבודה/קורס סייבר/קוד לפתיחת קובץ/ip addresses for project.txt")
    ip_read = open(ip_path, "r")
    print(ip_read.read())
def url_search():
    boolean="true"
    url_ser=input("please enter the url you want to search for")
    if url_ser in adds == True:
        print("the url is in the list!")
    else:
        print("the url is not in the list")
def url_ip_add():
    url=input("please enter the url you want to add")
    ip=input("please enter the ip you want to add")
    adds.update({url:ip})







menu()