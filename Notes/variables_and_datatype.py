# progrma run from top to bottom and left to rigth.
print("Create nails")
print("Create hammer")
print("Use hammer and nails")

#variables
# varaible names are case sensitive.
# must start with letter or underscore.
# Rather than using camel case we should use standard way of 
# using underscore between tow words in variable (e.g.:is_going)
Name = "abc"
age = 23
print("hello " + Name + "age :" + str(age))
# type(): to return the type of varible.
print(type(Name))   # OP: <class 'str'>
print(type(age))    # OP: <class 'int'>

#typecasting
a = int(1)        # a will be 1
b = int(2.5)      # b will be 2
c = int("3")      # c will be 3
#c1 = int("3.4")   # ERROR ,
c1 = int(float(3.4)) # c1 will be 3
d = float(1)      # d will be 1.0
e = float(2.5)    # e will be 2.5
f = float("3")    # f will be 3.0
g = float("4.23") # g will be 4.23
h = str("80s")    # h will be '80s'
i = str(22)       # i will be '22'
j = str(3.01)     # j will be '3.01'
print([a,b,c,c1,d,e,f,g,h,i,j])

# multiline comment
'''
This is 
multiline comment.
'''

# eacaping 
esc = 'it\'s morning'