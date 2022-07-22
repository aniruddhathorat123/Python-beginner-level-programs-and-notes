# More operation on dictionary:

python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}
#### 
# membership using `in` and `not in`
# it is case sensitive.
print('Arthur' in holy_grail)   #OP: True
print("arthur" in holy_grail)   #OP: False
print(35 in python) #OP: False

# Concatination or combinibg 2 ore mor dictionaries.
# Method 1: Using update
people1 = {}
#combine both `python` and `holy_grail` dictionaries.
people1.update(python)
people1.update(holy_grail)
people1.update(life_of_brian)
print(people1)
#OP: {'TerryG': 34, 'Graham': 37, 'Terry': 38, 'Michael': 35, 'Eric': 36, 'John': 35,
# 'Zoot': 17, 'Knight of NI': 40, 'Lancelot': 39, 'Galahad': 35, 'Arthur': 40,
# 'Biccus Diccus': 45, 'Stan/Loretta': 32, 'Reg': 35, 'Brian': 33}

# Method 2: COmprehension using for loop:
people2 = {}
# each groups contain one entire dictionary
# hence for lop executes 3 times for 3 dictionaries.
for groups in (python, holy_grail, life_of_brian):
    #print(f"Group: {groups}")
    people2.update(groups)
print(people2)
#OP: {'TerryG': 34, 'Graham': 37, 'Terry': 38, 'Michael': 35, 'Eric': 36, 'John': 35, 'Zoot': 17, 'Knight of NI': 40, 'Lancelot': 39, 'Galahad': 35, 'Arthur': 40, 'Biccus Diccus': 45, 'Stan/Loretta': 32, 'Reg': 35, 'Brian': 33}

# Method 3: Unpacking
# Note: unpacking avialable in python 3.5 or above.
people3 = {**python, **holy_grail, **life_of_brian}
print(people3)
#OP: {'John': 35, 'Eric': 36, 'Michael': 35, 'Terry': 38, 'Graham': 37, 'TerryG': 34, 'Arthur': 40, 'Galahad': 35, 'Lancelot': 39, 'Knight of NI': 40, 'Zoot': 17, 'Brian': 33, 'Reg': 35, 'Stan/Loretta': 32, 'Biccus Diccus': 45}

print(f"sum of all peoples ages : {sum(people1.values())}") 
#OP: sum of all peoples ages : 531

