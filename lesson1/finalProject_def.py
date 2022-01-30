import os
adds={"www.google.com":"1.1.1.1","www.facebook.com":"2.2.2.2","www.instagram.com":"3.3.3.3"}

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
    url_ser=input("please enter the url you want to search for")
    if (url_ser in adds) == True:
        print("the url is in the list!")
    else:
        print("the url is not in the list")
def url_ip_add():
    url=input("please enter the url you want to add")
    ip=input("please enter the ip you want to add")
    adds.update({url:ip})
def url_del():
    url_delete=input("please enter the url you want to delete")
    if (url_delete in adds) == True:
        adds.pop(url_delete)
    else:
        print("you enterd a url that doesnt exist! please try again")
def ip_change():
    url_def=input("please enter the URL")
    ip_url=input("please enter the new IP")
    adds[url_def]=ip_url
def url_print():
    print(adds)





