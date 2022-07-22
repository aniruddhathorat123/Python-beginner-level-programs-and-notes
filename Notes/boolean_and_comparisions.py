a=7
b=3
print('a == b is', a == b)
print('a != b is', a != b)
print('a > b is', a > b)
print('a < b is', a < b)
print('a >= b is', a >= b)
print('a <= b is', a <= b)
print('o in John is ','o' in 'John') #membership
print('o in John is ','o' not in 'John') #non membership
print('John is John ','John' is 'John') #identity
print('John is not John is ','John' is not 'John') # negative identity
### OP ###
# a == b is False
# a != b is True
# a > b is True
# a < b is False
# a >= b is True
# a <= b is False
# o in John is True
# o in John is False
# John is John True
# John is not John is False

# check if both occuping same memory location.
# id(): returns a unique id for the specified object.
# All objects in Python has its own unique id. 
a = {2,4,5}
b = a
print(id(a), id(b))   #OP: 2 2
b= {2,4,5}
print(id(a), id(b))   #OP: 2 3

print("#######")
print(int(True), float(True))   #OP: 1, 1.0
print(int(False), float(False)) #OP: 0, 0.0

print(bool(10)) #OP: True
print(bool(0))  #OP: False
print(bool("")) #OP: False
print(bool(" "))#OP: True
print(bool([])) #OP: False
print(bool("HI"))   #OP: True

print(34 + True)    #OP: 35
print(34 + False)   #OP: 34 
