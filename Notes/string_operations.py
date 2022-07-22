# string are immutable in python
msg = "hello guys"
#pos   0123..
#         ...-2-1

print(msg)
print(msg+msg)  #OP: hello guyshello guys
print(msg*2)    #OP: hello guyshello guys
print(msg,msg)  #OP: hello guys hello guys, here comma added one space char between 2 strings.

# upper case
print(msg.upper())  #OP: HELLO GUYS
#lower case
print(msg.lower())  #OP: hello guys
# Capitalize first letter of sentnece.
print(msg.capitalize()) #OP: Hello guys
# Capitalize first letter of every word in string.
print(msg.title())  #OP: Hello Guys
#problem : 
print("hello it's abc".title()) #OP: Hello It'S Abc

# length of string
print(len(msg)) #OP: 10
# count occurence of char or string in given string.
# count() is case sensitive.
print(msg.count("guys"))    #OP: 1


#Slicing of sting 
print(msg[3])   #OP: l
print(msg[-1])  #OP: s
print(msg[-3])  #OP: u
print(msg[2:])  #OP: llo guys // from 2 to end of string
# note: it took char from 2 to 4.
# it does not include 5th char.
print(msg[2:5]) #OP: llo //
print(msg[:7])  #OP: hello g // from 0 to 7 exclude 7th char.
# reverse the sting 
txt = "Hello World" [::-1]
print(txt)  #OP: dlroW olleH
# the slice statement [::-1] means start at the end of the string 
# and end at position 0, move with the step -1, negative one, 
# which means one step backwards.

# Multiline string
msg="""Dear Terry,,
You must cut down the mightiest 
tree in the forest with…
a herring! <3"""
print(msg)

# find : return the position of char in string 
# OR srarting position of string in the string.
msg='Welcome to Python 101: Strings'
# msg[3] = "e" // ERROR : string sre immutable in python.
print(msg.find("e"))

# replace(str, rep_str): replace str with the rep_str.
print(msg.replace("Python", "Java"))    #OP: Welcome to Java 101: Strings
# To save replaced string we need to assign to variable,
# because `msg`  string not gets changed by replace().
# e.g. : msg = msg.replace("Python", "Java")

# in : return True if char or string exist in given string.
print("W" in msg)   #OP: True
# not in : return True if char or string is NOT exist in given string.
print("Python" not in msg)  #OP: False


# String formating:
name='TERRY'
color = 'RED'
# required : [Terry] loves the color red!
str_f = f"[{name.capitalize()}] loves the color {color.lower()}!"
print(str_f)    #OP : [Terry] loves the color red!

# input(): take input from the user.
# givves user data in form of string.
name = input("enter your name:")
print("Hello " + name)


