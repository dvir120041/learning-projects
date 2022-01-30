badget=int(input("please enter your marketing budget. \nfacebook campaign = 100ILS per day."
             "\ninstagram campaign = 50ILS per day."))
fac_camp=float(input("how long do you want your facebook campaign to go?"))
inst_camp=float(input("how long do you want your instagram campaign to go?"))
price=(inst_camp*50 + fac_camp*100)*1.17
print("your total price + tax will be:" + str(price))
if(badget>price):
    print("successfull")
else:
    sum=price-badget
    print("you need to add " + str(sum) + " if you want that campaign ")