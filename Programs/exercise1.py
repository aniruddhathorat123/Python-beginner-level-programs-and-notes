# 1: 
item_name = "item1"
price = 34.45
quantity  = 23
is_in_inventory = True
print(item_name, price, quantity, is_in_inventory)
print("########## END 1 ###############")

#2 : 
#extract the text and create new string that says 
    # 1- "Welcome Ring To Tyler"
    # 2- Print same string in backword.

msg = "Welcome to python 101:Strings"
 #     0123456789

SPACE = " "
new_string = msg[18] + SPACE + msg[0:7] + SPACE + msg[-5:-1] + msg[7:11] + msg[8] + msg[12] + msg[2] + msg[1] + msg[-5] 
print(new_string.title())
#reverse
print((new_string.title())[::-1])
print("######### END 2 ##############")


## E : 3
# User input exercise.
# Take user name and distance in km
# greet the user and show the km and miles value.
# 1 mile = 1.609km
# capitalize the user name.
name = input("Enter your name: ")
kms = input("Enter the distance in km: ")
miles = round((float(kms)/ 1.609), 2);
print(f"Hello {name.capitalize()}!, the distance is {kms}km equilvant to {str(miles)} miles")
# OP : Hello Aniruddha!, the distance is 23km equilvant to 14.29 miles




