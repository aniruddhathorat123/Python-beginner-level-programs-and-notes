# Zip/Unzip
nums = [1,2,3,4] 
letters = ['a','b','c','d']
names =['John','Eric','Michael','Graham','Joe']

# match first nums with first letters and so on.
combo = list(zip(nums,letters))
print(combo)    #OP: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# can work with string
str1 = "ABCD"
str_combo = dict(zip(str1, letters))
print(str_combo)    #OP: {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}

combo2 = list(zip(nums,letters,names))
print(combo2)
#OP: [(1, 'a', 'John'), (2, 'b', 'Eric'), (3, 'c', 'Michael'), (4, 'd', 'Graham')]

# Unzipping : zip(*<zip-object>)
num,let,nam = zip(*combo2)
print(num, let ,nam) 
#OP: (1, 2, 3, 4) ('a', 'b', 'c', 'd') ('John', 'Eric', 'Michael', 'Graham')

# create dictionary for :
keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'
# create list first
keys = keys.split()
values = values.split()

# method 1:
en_sv_dict = dict(zip(keys,values))
print(en_sv_dict)
#OP: {'this': 'denna', 'parrot': 'papegojan', 'is': 'är', 'deceased': 'avliden'}

# method 2: dictionary comprehension
new_dict = {key:value for key,value in zip(keys,values)}
print(new_dict)
#OP: {'this': 'denna', 'parrot': 'papegojan', 'is': 'är', 'deceased': 'avliden'}

# Unzip the dictionary 
# Method 1:
en,sv = list(en_sv_dict.keys()), list(en_sv_dict.values())
print(en, sv)
#OP: ['this', 'parrot', 'is', 'deceased'] ['denna', 'papegojan', 'är', 'avliden']

# Method 2: using zip(*)
# items() : returns object contains the key-value pairs 
# of the dictionary, as tuples in a list.
en1,sv1 = zip(*en_sv_dict.items())
print(en1, sv1)
#OP: ('this', 'parrot', 'is', 'deceased') ('denna', 'papegojan', 'är', 'avliden')