# Split and join.
msg ='Welcome  to  Python'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']

# spliting from string to list
# default it based on space
print(msg.split())      #OP: ['Welcome', 'to', 'Python']
print(msg.split(' '))   #OP: ['Welcome', '', 'to', '', 'Python']
print(csv.split(","))   #OP: ['Eric', 'John', 'Michael', 'Terry', 'Graham']

# `<join-char>`Join(list) : can convert list into string.
# each element in the list will be separated by <join-char>.
print("-".join(friends_list))   #OP: Eric-John-Michael-Terry-Graham
print(" ".join(friends_list))   #OP: Eric John Michael Terry Graham

# Remove all spaes from list and convert list into the string.
print("".join(msg.split())) #OP: WelcometoPython
# OR:
print(msg.replace(" ", "")) #OP: WelcometoPython



csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise.
no_semiColon = ",".join(csv.split(";"))
print(no_semiColon) #OP: Eric,John,Michael,Terry,Graham:TerryG,Brian
no_colon = ",".join(no_semiColon.split(":"))
print(no_colon)     #OP: Eric,John,Michael,Terry,Graham,TerryG,Brian
print(no_colon.split(",")) 
     #OP: ['Eric', 'John', 'Michael', 'Terry', 'Graham', 'TerryG', 'Brian']
# NOTE : can also done with replace() funtion.      


 