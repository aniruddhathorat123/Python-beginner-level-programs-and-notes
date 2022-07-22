# It’s...not really an adventure game...#Ver 1.0
# Your village is being attacked by 'a germanic tribe' and you need to run to the 
# stores and get the right things to save your village, and probably some good looking 
# girl or boy you want to marry. All prices in gold pieces excl.
# VAT... chop chop!! ze germanz are coming!
# The code should allow you to get 1 thing from each store and each item you get should
# be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have 
# to pay for stuff or add it up

# ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', 
# and to exit if a nonexistant item is bought(typed)
# Add purse with 1000 gold pieces and payment for the items during or at end of code and 
# show a message about total cost and how much gold you have left

# ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy
# ..stop scrolling TikTok/Facebook! ;-)

# Ver 1.5 print inventory before and after purchases as one department_store of stuff
# (combine inventories from all stores into one...pretend Big Biz bought all the local stores,
# and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the 
# problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

# stores:
freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 
'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 
'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

# Version 1.5
cart = {}
tot_items1 = ""
purse = 1000

# All inventory before purchase
dept_Store = {}
for dept in (freelancers, antiques, pet_shop):
    dept_Store.update(dept)
    # remove name of store.
    dept_Store.pop("name")
print("Inventory before purchse:")
print(sorted(dept_Store.items()))
print("----------------------------------------------------------")

for store in (freelancers, antiques, pet_shop):
    # get the store name.
    name = str(store.get("name"))
    # get the string of available items.
    items = ", ".join(list(store.keys())[1:])
    purchase = input(f'''Welcome to {name.capitalize()}, 
    Available items: {items}
     - Available gold pieces: {purse}
     - Enter 'exit' to leave store
    Enter item name to purchase:''')
    # exit if user input "exit" or item which is not in store.
    if (purchase.lower() == "exit" or purchase not in store):
        print(f"You exit from {name.capitalize()}.")
        continue
    # Add selected item to cart and remove it from store.
    tot_items1 = tot_items1 + f"{purchase} : {store.get(purchase)} Gp, "
    cart.update({purchase : store.pop(purchase)})
    # Reduced the cost of purchased item from current purse.
    purse -= cart.get(purchase)

tot_items = ", ".join(list(cart.keys()))
# calculate total sum of all purchased items.
tot_sum = sum(cart.values())
print("----------------------------------------------------------")
print(f'''Your purchase: {tot_items1}.
Your total is {tot_sum} Gp.
Remaining gold coins: {purse} Gp.
Have a nice day of mayhem!''')

# All remaining items after purchase.
dept_store_after = {**freelancers, **antiques, **pet_shop} #avail after python 3.5
# remove name of store.
dept_store_after.pop("name")
print("----------------------------------------------------------")
print("Remaining inventory after purchase:")
print(sorted(dept_store_after.items()))


# Inventory before purchse:
# [('biccus diccus', 100), ('black knight', 20), ('blue parrot', 10), ('brian', 70), 
# ('catapult', 75), ('french castle', 400), ('german joke', 5), ('grim reaper', 500),
# ('minstrel', -15), ('newt', 2), ('scythe', 150), ('white rabbit', 5), ('wooden grail', 3)]
# ----------------------------------------------------------
# Welcome to Freelancing shop,
#     Available items: brian, black knight, biccus diccus, grim reaper, minstrel
#      - Available gold pieces: 1000
#      - Enter 'exit' to leave store
#     Enter item name to purchase:brian
# Welcome to Antique shop, 
#     Available items: french castle, wooden grail, scythe, catapult, german joke
#      - Available gold pieces: 930
#      - Enter 'exit' to leave store
#     Enter item name to purchase:french castle
# Welcome to Pet shop, 
#     Available items: blue parrot, white rabbit, newt
#      - Available gold pieces: 530
#      - Enter 'exit' to leave store
#     Enter item name to purchase:white rabbit
# ----------------------------------------------------------
# Your purchase: brian : 70 Gp, french castle : 400 Gp, white rabbit : 5 Gp, .
# Your total is 475 Gp.
# Remaining gold coins: 525 Gp.
# Have a nice day of mayhem!
# ----------------------------------------------------------
# Remaining inventory after purchase:
# [('biccus diccus', 100), ('black knight', 20), ('blue parrot', 10),
#  ('catapult', 75), ('german joke', 5), ('grim reaper', 500), ('minstrel', -15),
#  ('newt', 2), ('scythe', 150), ('wooden grail', 3)]
