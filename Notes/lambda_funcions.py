# Lambda function:
# implicit function, always return some value.
# throw-away function.
# can call function immediately after creating it.
# syntax : #name = lambda parameter(s): expression
def square(x):
    return x*x
square1 = lambda x: x*x
print(square1(3))

# create lambda for following function:
# def name_and_alias(name,alias):
#     return name.strip().title() + ':' + alias.strip().title()
name_alias = lambda name,alias: name.strip().title() + ":" + alias.strip().title()
print(name_alias(" harsh kumar " , "hari")) #OP: Harsh Kumar:Hari


monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']

# sort list by first name of persons in list.
# lambda split the each string of list and gives back first name 
# or first word from the stirng.
monty_python.sort(key = lambda name:name.split())
print(monty_python)
#OP: ['Eric Idle', 'Graham Arthur Chapman', 'John Marwood Cleese', 'Michael Edward Palin', 'Terrence Vance Gilliam', 'Terry Graham Perry Jones']


# sort list by last name of persons in list.
# here [-1] at end gives the list word in splitted string.
monty_python.sort(key = lambda name:name.split()[-1])
print(monty_python)
#OP: ['Graham Arthur Chapman', 'John Marwood Cleese', 'Terrence Vance Gilliam', 'Eric Idle', 'Terry Graham Perry Jones', 'Michael Edward Palin']


def func(n):
    return lambda a: a*n
# function outputting or returning the lambda function
# i.e. returns a*2
print((func(3)))    #OP: <function <lambda>>

# Pass the value to lambda inside the funtion
dubler = func(3)
print(dubler(4))    #OP: 12
# OR
# using positional arguments
print(func(3)(4))   #OP: 12


# BEST e.g.:
# charged the person based on start cost and cose per hour.
# 2 types of person : normal and premium.
def price_cal(start, hourly_cost):
    return lambda hours: start + hourly_cost * hours
    
# normal person
nor_person = price_cal(10, 30)
# premium customer
premium_cost = price_cal(12, 40)

# cost for normal person for 2 hrs
print(nor_person(2))    #OP: 70
# cost for premium person for 2 hrs
print(premium_cost(2))  #OP: 92

# e.g. for positional arguments:
print((lambda a,b,c: a+b+c)(2,3,4)) #OP: 9

# lambda function using default values.
# always put default values at the end of fuction paramers in lambda.
print((lambda a,b,c=3: a+b+c)(2,10))    #OP: 15

# lambda function using named arguments.
print((lambda a,b,c: a+b+c)(2,c=10, b=4))   #OP: 16

# unpacking arguments in lambda.
print((lambda *args: sum(args))(2, 4, 7))   #OP: 13
    # can send any number of arguements
print((lambda *args: args[0] + args[2])(2, 4, 7))   #OP: 9

