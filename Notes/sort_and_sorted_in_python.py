
my_list = [1,5,3,7,2]
another_list = [34, 55, 1, 33, 60, 21]
my_dict = {'car':4,'dog':2,'add':3,'bee':1}
my_tuple = ('d','c','e','a','b')
my_string = 'python'

# sort(): 
# - for list and disctionary which is mutable, it sort
# the list or dictionary. 
my_list.sort()
print(my_list)  #OP: [1, 2, 3, 5, 7]

# sorted(obj) : return the noew sorted `obj` 
# it does not sort the actual given obt, it return new 
# sorted `list` instead.
# obj can be list, dictionary or tuple.
print(sorted(another_list)) #OP: [1, 21, 33, 34, 55, 60]
print(another_list)     #OP: [34, 55, 1, 33, 60, 21]

print(sorted(my_tuple)) #OP: ['a', 'b', 'c', 'd', 'e']

# sort dictionary as per key values.
print(sorted(my_dict))  #OP: ['add', 'bee', 'car', 'dog']
# sort dictionary as per values in reverse order.
print(sorted(my_dict.values(), reverse= True)) #OP: [4, 3, 2, 1]

# reversed() : reverse the list.
print(reversed(my_list))    #OP: <reversed object>
print(list(reversed(my_list)))  #OP: [7, 5, 3, 2, 1]


my_list = [1,5,-3,7,-2]
my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
# `key = abs`: sort regardless of +ve or -ve
print(sorted(my_list, key = abs))   #OP: [1, -2, -3, 5, 7]
# sort as per first element in sublist
print(sorted(my_llist)) 
    #OP: [['add', 3, 10], ['bee', 1, 24], ['car', 4, 65], ['dog', 2, 30]]
    
# sort using lambda function on sublist.
# `item :item[1]` we specified the key of sublist and as per key
# sort will be performed, i.e. key = index 1 in sublist
print(sorted(my_llist, key = lambda item :item[1]))
    #OP: [['bee', 1, 24], ['dog', 2, 30], ['add', 3, 10], ['car', 4, 65]]



