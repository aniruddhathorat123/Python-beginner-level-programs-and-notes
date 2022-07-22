# Comprehensions:
# using comprehension we can avoid use of for loop.
# for list 
numbers = [1,2,3,4,5,6,7,8,9]
# give me a list with num squared for each num in numbers
new_list = []
for num in numbers:
    new_list.append(num*num)
print(new_list) #OP: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# using comprehension:
new_list = [num*num for num in numbers]
print(new_list) #OP: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# give the even number from the list.
new_list = [num for num in numbers if num % 2 == 0]
print(new_list) #OP: [2, 4, 6, 8]

# using filter()
# filter(function, sequence)
# function: function that tests if each element of a 
# sequence true or not.
new_list = filter(lambda num: num % 2 == 0, numbers)
print(list(new_list))   #OP: [2, 4, 6, 8]

# convert following to comprehension.
# for letter in 'spam':
#    for num in range(4):
#        new_list.append((letter,num))
# print(new_list)
new_list = [(letter, num) for letter in "span" for num in range(4)]
print(new_list)
#OP: [('s', 0), ('s', 1), ('s', 2), ('s', 3), ('p', 0), ('p', 1), ('p', 2),
# ('p', 3), ('a', 0), ('a', 1), ('a', 2), ('a', 3), ('n', 0), ('n', 1), 
# ('n', 2), ('n', 3)]



# Dictionary comprehension:

movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
"Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]
year =[1971,1975,1979,1982,1983,2014]
names = ['John','Eric','Michael','Graham','Terry','TerryG']

list(zip(movies, year))
# give me a dict('movies': year) for each movies, year in zip(movies, year)
# using for loop
new_dict = dict()
for movie, yr in zip(movies,year):
    new_dict[movie] = yr
print(new_dict)
#OP: {'And Now for Something Completely Different': 1971, 'Monty Python and the Holy Grail': 1975, 
# "Monty Python's Life of Brian": 1979, 'Monty Python Live at the Hollywood Bowl': 1982,
# "Monty Python's The Meaning of Life": 1983, 'Monty Python Live (Mostly)': 2014}

# using dictionary comprehension:
new_dict = {movie:yr for movie,yr in zip(movies,year)}
print(new_dict)
#OP: {'And Now for Something Completely Different': 1971, 'Monty Python and the Holy Grail': 1975, 
# "Monty Python's Life of Brian": 1979, 'Monty Python Live at the Hollywood Bowl': 1982,
# "Monty Python's The Meaning of Life": 1983, 'Monty Python Live (Mostly)': 2014}

# get the movie before 1983 and name starts with "Monty"
new_dict = {movie:year for movie,year in zip(movies,year) if year < 1983 and movie.startswith("Monty")}
print(new_dict)
#OP: {'Monty Python and the Holy Grail': 1975, "Monty Python's Life of Brian": 1979,
# 'Monty Python Live at the Hollywood Bowl': 1982}

# print person's name with his favorite movie and year and year < 1981.
new_l1 = [[f"{person}'s favorite movie was '{movie}' from {year}"] for person,movie,year in zip(names,movies,year) if year < 1981 ]
print(new_l1)
#OP: 
# [["John's favorite movie was 'And Now for Something Completely Different' from 1971"], 
# ["Eric's favorite movie was 'Monty Python and the Holy Grail' from 1975"],
# ["Michael's favorite movie was 'Monty Python's Life of Brian' from 1979"]]



