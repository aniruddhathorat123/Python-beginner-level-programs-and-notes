### Enumerate 
# can used numbered the print statments in loop, like show below
print('python101 - Enumerate')
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']
efriends = [(51,'Brian'), (52,'Judith'), (53,'Reg'), (54,'Loretta'), (55,'Colin')]

# i = 51
# for friend in friends:
#     print(i, friend)
#     i = i +1 # += 1

# enumerate print from 51 upto end of list.
# e.g. of modified list:
# [(51,'Brian'), (52,'Judith'), (53,'Reg'), (54,'Loretta'), (55,'Colin')]
for num, friend in enumerate(friends,51):
    print(num, friend)
#OP:
# 51 Brian
# 52 Judith
# 53 Reg
# 54 Loretta
# 55 Colin

print(type(enumerate(friends))) #OP: <class 'enumerate'>
print(list(enumerate(friends)))
    #OP: [(0, 'Brian'), (1, 'Judith'), (2, 'Reg'), (3, 'Loretta'), (4, 'Colin')]
    
# another e.g.:
for friend in enumerate(friends, start = 1):
    print(friend)
#OP: it just print each enumerated element.
# (1, 'Brian')
# (2, 'Judith')
# (3, 'Reg')
# (4, 'Loretta')
# (5, 'Colin')


