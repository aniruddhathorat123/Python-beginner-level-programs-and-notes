# convert the given functions into lambda functions.
# 1:
# def f(x): return x + 5
fun1 = lambda x: x + 5
print(fun1(2))  #OP: 7
# OR:
print((lambda x: x + 5)(2)) #OP: 7


# 2:
# def strip_spaces(str):
#    return ''.join(str.split(' '))
# IP: 'Monty Pythons Flying Circus'

func2 = lambda str: "".join(str.split(" "))
print((lambda str: "".join(str.split(" ")))('Monty Pythons Flying Circus'))
    #OP: MontyPythonsFlyingCircus
    # OR can call print(func2('Monty Pythons Flying Circus'))


# 3:
# def join_list_no_duplicates(list_a,list_b):
#    return list(set(list_a + list_b))
list_a = [1,2,3,4]
list_b = [3,4,5,6,7]
# set() does not contain the duplicate elements, it remove the duplicate elements.
print((lambda list1, list2: list(set(list1 + list2)))(list_a, list_b))
    #OP: [1, 2, 3, 4, 5, 6, 7]
# OR using unpacking:
print((lambda *args: list(set(args[0] + args[1])))(list_a, list_b))
    #OP: [1, 2, 3, 4, 5, 6, 7]


# 4:
# Complete the function so it returns a function
# def create_quad_func(a,b,c):
#     '''return function f(x) = ax^2 + bx + c'''
#     return lambda x: ???

def create_quad_func(a,b,c):
    # `**` represent the power(^) operator in python.
    return lambda x: a * x ** 2 + b * x + c
print((create_quad_func(2,4,6))(2)) #OP: 22


#5: 
# sort the elements in list as per integers value inside them.
signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']

# split the items as per string and int part.
# then gets the last part which is int number.
# comvert the int number from string to int and return.
signups.sort(key = lambda item: int(item.split("F")[-1]))
print(signups)
#OP: ['MPF2', 'MPF3', 'MPF17', 'MPF20', 'MPF45', 'MPF104']

# OR : best way , yusing slicing 
# slice from 3 to end of string which gives us int part.
signups.sort(key = lambda item: int(item[3:]))
print(signups)
#OP: ['MPF2', 'MPF3', 'MPF17', 'MPF20', 'MPF45', 'MPF104']


#6: Sort `player_list` by score using lambda!
class Player:
   def __init__(self, name, score):
       self.name = name
       self.score =  score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]

player_list.sort(key= lambda player: player.score)
print([f"{player.name} : {player.score}" for player in player_list])
#OP: ['John : 24327', 'Eric : 116700', 'Terry : 150000']

# Sort in reverse order:
player_list.sort(key= lambda player: player.score, reverse=True)
print([f"{player.name} : {player.score}" for player in player_list])
#OP: ['Terry : 150000', 'Eric : 116700', 'John : 24327']

