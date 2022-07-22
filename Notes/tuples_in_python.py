# Tuples - faster Lists you can't change.
# immutable datatype.
# faster for searching and travesing.
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
print(friends)      #OP: ['John', 'Michael', 'Terry', 'Eric', 'Graham']
print(friends_tuple)    #OP: ('John', 'Michael', 'Terry', 'Eric', 'Graham')
print(friends[2:4])     #OP: ['Terry', 'Eric']
print(friends_tuple[2:4])   #OP: ('Terry', 'Eric')
