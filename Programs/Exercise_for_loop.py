
# - Need to invite firends for your party
# - print all invitation for party for each friend using loop.
# - names are in below 2 lists.
# - Also add 2 extra names into the list using input box.
# - Print one invitation for each friend per line.
# - e.g.: `John Clees! You are invited to the party saturday`
# - Hint: you may need 2 for loops.


names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
comm_str = 'You are invited to the party saturday.'

for i in range(2):
    more_name = input("Enter one more friend: ")
    names1.append(more_name)

# extend the names list with names1 list.
names += names1

for name in names:
    print(f'{name.title()}! {comm_str}')

#### OP #####
# Enter one more friend: eshwar modi
# Enter one more friend: rajesh m. adani
# John Cleese! You are invited to the party saturday.
# Eric Idle! You are invited to the party saturday.
# Michael! You are invited to the party saturday.
# Graham Chapman! You are invited to the party saturday.
# Terry! You are invited to the party saturday.
# Terry Jones! You are invited to the party saturday.
# Eshwar Modi! You are invited to the party saturday.
# Rajesh M. Adani! You are invited to the party saturday.
