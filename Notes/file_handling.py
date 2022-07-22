# File handling:

#reading from file
my_file = open('greeting.txt','r') #w, a
# `file.read()` read the complete file.
print(my_file.read())
#OP: 
# Hello,
# Welcome to Monty Pythons Flying Circus!

# read 10 chars
# Space or next line also considered as char.
print(my_file.read(10))
#OP:
# Hello,
# Wel

# read while file and break it up line-by-line
line_by_line = my_file.readlines()
line_by_line1 = my_file.read().splitlines()
# both gives same result, 
# but `splitlines()` is better
print(line_by_line)
print(line_by_line1)
#OP: ['Hello,', 'Welcome to Monty Pythons Flying Circus!']

# Always close file after opening as in above way
my_file.close()


# File handling using context manager
# here no need to close the fril explicitly.
with open("friends.csv", "r") as f:
    friends = f.read().splitlines()
    print(friends)
    #OP: ['John, 1939', 'Eric, 1943', 'Michael, 1943', 'Graham, 1941',
    # 'TerryG, 1940', 'TerryJ, 1942']
    for friend in friends:
        friend = friend.split(",")
        name = friend[0]
        # strip(): remove extra space after the comma.
        year = int(friend[1].strip())
        print(name, year)
#OP:
# John 1939
# Eric 1943
# Michael 1943
# Graham 1941
# TerryG 1940
# TerryJ 1942

# read and print line by line.
with open("movies.txt", "r") as f:
    for line in f.readlines():
    #OR: for line in f:
        print(line)

#OP:
# life of pi, 2010
# The peacemaker, 1999
# Guru, 2001





