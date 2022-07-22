# Lists: 
# Mutable datatype.
friends = ['John','Michael','Terry','Eric','Graham']
# position :  0      1         2       3      4
list2 = [10, "abc", 34.5]
print(list2)    #OP: [10, 'abc', 34.5]
print(list2[0]) #OP: 10

print(friends[1],friends[4])    #OP: Michael Graham
print(len(friends))             #OP: 5
print(friends.count('Eric'))    #OP: 1

# index(obj) return position of obj in the list.
print(friends.index("Terry"))   #OP: 2

# Slicing:
print(friends[-1])  #OP: Graham
print(friends[:3])  #OP: ['John', 'Michael', 'Terry']
print(friends[1:4]) #OP: ['Michael', 'Terry', 'Eric']

# sorting
marks = [45, 56, 8, 100, 23, 44, 11]

friends.sort()
print(friends)  #OP: ['Eric', 'Graham', 'John', 'Michael', 'Terry']
# reverse
friends.sort(reverse = True)
print(friends)  #OP: ['Terry', 'Michael', 'John', 'Graham', 'Eric']
#OR
friends.reverse()
print(friends)  #OP: ['Eric', 'Graham', 'John', 'Michael', 'Terry']

# min 
print(min(marks))   #OP: 8
# for string list, not sure but it gives first element in asc-sorted list.
print(min(friends)) #OP: Eric

# max
# for string list, not sure but it gives last element in asc-sorted list.
print(max(friends)) #OP: Terry

# sum : sum of all elements in list.
print(sum(marks))   #OP: 287

# Append(ele):
# Add given element at end of list.
friends.append("Ronak")
print(friends)  #OP: ['Eric', 'Graham', 'John', 'Michael', 'Terry', 'Ronak']

# Insert(Loc, ele): insert the element at given location.
# element at current location will be shifted to next location.
friends.insert(1, "Veru")
print(friends)  
    #OP: ['Eric', 'Veru', 'Graham', 'John', 'Michael', 'Terry', 'Ronak'] 
    
# index insert: replace the element with given element in list
friends[1] = "Chandler"
print(friends)
    #OP: ['Eric', 'Chandler', 'Graham', 'John', 'Michael', 'Terry', 'Ronak']

# extend(): Append 2 dieerent list together.
friends.extend(marks)
print(friends)
    #OP: ['Eric', 'Chandler', 'Graham', 'John', 'Michael',
    #     'Terry', 'Ronak', 45, 56, 8, 100, 23, 44, 11]
#OR : friends = friends + marks 
    
# remove(ele): remove element from the list
new_friend = ['Eric', 'Chandler', 'Graham', 'John', 'Michael', 'Terry', 'Ronak']
new_friend.remove("Ronak")
print(new_friend)
    # OP : ['Eric', 'Chandler', 'Graham', 'John', 'Michael', 'Terry']

# pop() : remove last element from the list and return.
removed = new_friend.pop()
print(removed)  #OP: Terry
# can specify location of element to pop // pop(-1): pop last element.
removed = new_friend.pop(2)
print(removed)  #OP: Graham

#del list[loc] : delete element in given location in list.
del new_friend[3]
print(new_friend)   #OP: ['Eric', 'Chandler', 'John']

# clear the list
new_friend.clear()  
print(new_friend)   #OP: []

# delete the list completely.
del friends
# print(friends)  // ERROR: undefiend `friends`

# copy the list.
friends = ['John','Michael','Terry','Eric','Graham']
# first way:
new_friends = friends[:]
# second way:
new_friends = friends.copy()
# third way
new_friends = list(friends)
print(new_friends)  #OP: ['John', 'Michael', 'Terry', 'Eric', 'Graham']
