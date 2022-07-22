# classes and objects:

#Classes are blueprints
#Objects are the actual things you built
#variables => attributes
#functions => methods

class Movie:
    # to initialise the object and passed arguments
    # The keyword self represents the instance of a class 
    # and binds the attributes with the given arguments
    # equilvant ot C++ constructor.
    def __init__(self, name, year, imdb):
        self.name = name
        self.year = year
        self.imdb = imdb
        
    # function to access and print object values.
    def get_details(self):
        print("Title: ", self.name)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.imdb)
        
# calling class and creating object
movie_obj = Movie("life of pi", 2010, 8.7)
# Accessing memebers of class
print(movie_obj.name, movie_obj.year, movie_obj.imdb)
    #OP: life of pi 2010 8.7
    
# Access members using class function.
# here we implicitely passing current object for function
movie_obj.get_details()
# OR: We can pass object explicitely as follows,
# Both givess same result.
Movie.get_details(movie_obj)
#OP : both has same output
# Title: life of pi
# Year of production: 2010
# IMDB Score: 8.7


# can create list of objects.
obj2 = Movie("Guru", 2001, 8.1)
movie_details = [movie_obj, obj2]
# print some details:
print(movie_details[0].name, movie_details[1].name) #OP: life of pi Guru
# print using class methods.
movie_details[1].get_details()
#OP: 
# Title: Guru
# Year of production: 2001
# IMDB Score: 8.1


# Inheritance
print ("----------- Inheritance ------------")

# Base class
class Person:
    def move(self):
        print("Move 4 paces")
    def rest(self):
        print("gain 4 health point")

# Doctor inherit Person class.        
class Doctor(Person):
    def heal(self):
        print("Heal 10 health points")

# Figher inherit Person class.        
class Figher(Person):
    def fight(self):
        print("Do 10 point damage")
    # Person.move is overrride here.
    def move(self):
        print("Move 6 paces")
    
class Wizard(Doctor, Figher):
    def cast_spell(self):
        print("becomes invisible for 10 sec")
    # Override `Doctor.heal`
    def heal(self):
        print("Heal 15 health points")
    
character1 = Wizard()
character1.heal()   #OP: Heal 15 health points
# here uses Fgher.move because it is closer in inheritance.
character1.move()   #OP: Move 6 paces
# both Doctor and Fighet has rest method.
# but it uses Doctor here because Doctor inherited first before
# Figher in Wizard class defination: `class Wizard(Doctor, Figher)`
character1.rest()   #OP: gain 4 health point
        
        
    