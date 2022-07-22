#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

print("1: " + str("Eric" in friends and "John" in friends))
print("2: " + str(friends.union(my_friends))) 
    #OR (friends | my_friends)

print("3: " + str(friends.intersection(my_friends)))  
    #OR (friends & my_friends)

print("4: " + str(friends.difference(my_friends)))    
    #OR : friends - my_friends

print("5: " + str(friends.symmetric_difference(my_friends)))
    # OR : (friends.union(my_friends)).difference(friends.intersection(my_friends)))
    # OR : (my_friends ^ friends)

new_cars = list(set(cars))
print("6: " + str(new_cars))

######## OP #########
# 1: True
# 2: {'John', 'Terry', 'Eric', 'Graham', 'Michael', 'Loretta', 'Reg', 'Colin'}
# 3: {'John', 'Graham'}
# 4: {'Eric', 'Terry', 'Michael'}
# 5: {'Loretta', 'Michael', 'Terry', 'Reg', 'Eric', 'Colin'}
# 6: ['996', '420', 'V90', 'S', '911', 'V70', '900', '328']