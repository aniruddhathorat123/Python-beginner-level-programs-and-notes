# Sets - blazingly fast unordered Lists.
# Unordered list. i.e. 'set' object is not subscriptable 
# i.e. set[2] : this operation is not supported.
# remove duplicate elements.

friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
print(friends_set)  #OP: {'John', 'Michael', 'Terry', 'Eric', 'Graham'}

# SOme operations:
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}
print(friends_set.intersection(my_friends_set)) #OP: {'Eric', 'Graham'}

#empty Lists
empty_list = []
empyt_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
empty_set = {} # this is wrong, this is a dictionary
empty_set = set()



