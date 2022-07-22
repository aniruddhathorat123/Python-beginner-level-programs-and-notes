# Functions: 
# Anything under `def` will consider as function body,
# as long as it is indened with fucntion.
# Can use default parameter.
def greeting(name, age=12):
    print(f"Hello {name} you'r age is : {age}")
    
greeting("ABC", 33)  #OP: Hello ABC you'r age is : 33
greeting("PQR")     #OP: Hello PQR you'r age is : 12


# Named notations:
# we can provide the names to the fucntion's parameter so that
# we did not need to match the order of fucntion parameter. 
# increase readability of code.
# Either none of parameter has named notation OR all paramers 
# will have named notation.
def greeting(name, age=28, color="red"):
 #Greets user with “name” from “input box” and “age”, if unavailable, default age is used   
   
   print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
   print(f"We hear you like the color {color.lower()}!")
   
greeting("PQR", 34, "Blue")
## named notation
greeting(age=23, name="ABC", color="Blue")
# OP:
# Hello Abc, you will be 24 next birthday!
# We hear you like the color blue!


###### Fucntion return

def value_added_tax(amount):
    tax = amount * 0.25
    return tax
        
print(value_added_tax(125)) #OP: 31.25


# return multiple values.
# by default it returns tuple for multiple values.
# can return set or list
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return [amount, tax, total_amount]
    
price = value_added_tax(100)    
print(price, type(price))   #OP: [100, 25.0, 125.0] <class 'list'>



