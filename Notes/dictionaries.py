# Dictionary: key-value paired datatype.
# can have duplicate values but not duplicate keys.
movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}
print(movie)
    #OP: {'title': 'Life of Brian', 'year': 1979,
    # 'cast': ['John', 'Eric', 'Michael', 'George', 'Terry']}
print(movie["year"])    #OP: 1979


# if key is not exist in dictionary then this print throw error.
#print(movie['budget'])  #OP:  KeyError: budget
# to avoid above error use .get(key) method instead.
print(movie.get("budget"))  #OP: None

# get default values for `None` return.
print(movie.get("bidget", "Not found")) #OP: Not found

# Update specific key's value.
movie["title"] = "Terminator"
# Add new key-value
movie["budget"] = 23000
print(movie)
    #OP: {'title': 'Terminator', 'year': 1979, 
    # 'cast': ['John', 'Eric', 'Michael', 'George', 'Terry'], 'budget': 23000}
    
# Update whole dictionary.
movie.update({
    'title' : 'Life of Pi',
    'year' : 2010,
    'cast' : ['John','Eric','Michael']
})
print(movie)
    #OP: {'title': 'Life of Pi', 'year': 2010, 
    # 'cast': ['John', 'Eric', 'Michael'], 'budget': 23000}
    
# delete key-value
del movie["budget"]
print(movie)
    #OP: {'title': 'Life of Pi', 'year': 2010, 
    # 'cast': ['John', 'Eric', 'Michael']}
# delete using pop().
movie["budget"] = 23000
del_budget = movie.pop("budget")
print(movie)   
    #OP: {'title': 'Life of Pi', 'year': 2010, 
    # 'cast': ['John', 'Eric', 'Michael']}
print(del_budget)   #OP: 23000

# length of dictionary:
print(len(movie))   #OP: 3
# keys:
print(movie.keys()) #OP: dict_keys(['title','year','cast'])
# values:
print(movie.values())
    #OP: dict_values(['Life of Pi',2010,['John', 'Eric', 'Michael']])

#dict.items(): return list of tuples of key-value pair of dictionary.
print(movie.items())
    #OP: dict_items([('title', 'Life of Pi'),('year', 2010),
    # ('cast', ['John', 'Eric', 'Michael'])])

# travese through key or value.
for key in movie:
    print(key)  #OP: title year cast

# traverse through ket and value both.
for key, value in movie.items():
    print(key, value)
#OP:
# title Life of Pi
# year 2010
# cast ['John', 'Eric', 'Michael']




