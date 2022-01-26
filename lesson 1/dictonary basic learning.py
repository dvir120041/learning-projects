my_dict={"dvir":1000,"ben":100,"aron":200,"dudu":300,"moshe":400}
sum = my_dict["dvir"] + my_dict["moshe"]
print("dvir's and moshe's worth is: " + str(sum))
my_dict.update({"ronen":sum})
print("the amount of names are: " + str(len(my_dict)))
print("idan" in my_dict)