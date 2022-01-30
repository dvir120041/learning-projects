from lesson1.finalProject_def  import *
def menu():
    while(True):
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
            elif dns_system=="3":
                url_del()
            elif dns_system=="4":
                ip_change()
            elif dns_system=="5":
                url_print()
            else:
                print("you entered a wrong number, please try again!")
        else:
            print("you entered a wrong number, please try again!")
        repeat=input("do you want to go again?y/n")
        if repeat == "n" or repeat == "no":
            print("ok, goodbye!")
            break
menu()