
# with open("friends.csv", "r") as f:
#     friends = f.read().splitlines()
#     print(friends)
#     #OP: ['John, 1939', 'Eric, 1943', 'Michael, 1943', 'Graham, 1941', 'TerryG, 1940', 'TerryJ, 1942']
#     for friend in friends:
#         friend = friend.split(",")
#         name = friend[0]
#         # strip(): remove extra space after the comma.
#         year = int(friend[1].strip())
#         print(name, year)
# #OP:
# # John 1939
# # Eric 1943
# # Michael 1943
# # Graham 1941
# # TerryG 1940
# # TerryJ 1942


# read and print line by line.
# with open("movies.txt", "r") as f:
#     for line in f:
#     #OR: for line in f.readlines():
#         print(line)

#OP:
# life of pi, 2010
# The peacemaker, 1999
# Guru, 2001

import string, random
# `string.ascii_letters` contains both upper and lowe case letters.
letter_nums = string.ascii_letters + string.digits
word = "".join(random.choices(letter_nums, k=7))  
print(word) #e.g. : qmwAWYC

