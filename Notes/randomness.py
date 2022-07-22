# Randomness

# need `random` module. 
import random

# random.random() generate the random number between 0-1, but not 1.
print(random.random())  #E.g.: 0.8050821549527155

# random number from 0 upto 6
print(random.random() * 6)  #E.g.: 4.76799440165858

# random number between 1 and 5:
print(random.uniform(1, 5)) # E.g. 3.092735960697436

# int random number between 1 and 5
print(random.randint(1,5))  #E.g. : 1

# 5 int randum number betwween 1 to 100 and number should be odd.
for i in range(5):
    print(random.randrange(1,100,2))
    # for even no : random.randrange(2,100,2)
    
friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']
# print single random name from the list.
print(random.choice(friends_list))  #e.g. : Eric

# print 3 random name from the list.
# sample never gives duplicate values.
# range should be <= list.length()
print(random.sample(friends_list, 3))  #e.g. : ['Michael', 'Graham', 'John']

# shuffel the list:
random.shuffle(friends_list)
print(friends_list) #OP: ['Terry', 'Graham', 'John', 'Eric', 'Michael']


# generate 7 char string contains upper or lower or digits
# require `string` module
import string
# `string.ascii_letters` contains both upper and lowe case letters.
letter_nums = string.ascii_letters + string.digits
print(letter_nums)  #OP: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
word = ""
for i in range(7):
    word += random.choice(letter_nums)
print(word)    # e.g. : N4uNL6l
# if we don't want ot repeat any word or digit:
word = "".join(random.sample(letter_nums, 7))
print(word) #OP: EnM5tXm
# OR can also use: "".join(random.choices(letter_nums, k=7))


