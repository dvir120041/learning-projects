"""
מלפפון = 2 שקלים
עגבנייה = 3 שקלים
קולה = 5 שקלים
עוף = 20 שח לקילו
התוכנית תחשב את המחיר לתשלום אחרי מעמ (17%) ללא שארית.
"""
a=input("please enter how many cucummbers did you buy")
a2 = int(a) * 2
b=input("please enter how many tommatos did you buy")
b2 = int(b) * 3
c=input("please enter how many coca colas did you buy")
c2 = int(c) * 5
d=input("please enter how many kilograms of chiken did you buy")
d2 = int(d) * 20
totalprice = (a2+b2+c2+d2)/100*87
lp = totalprice//1
print("your total price is: " + (str(lp)))