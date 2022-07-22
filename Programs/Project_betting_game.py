#  -------------------- Marble betting game ----------------------------
# - Draw a single marble from a bag (assume it's random).
# - A bag has 10 marbles: 6 green, 4 red.
# - If you draw green marble you win same amount that you bet, if you 
#   draw red marble you lose amount you bet.
# - Marbles are replaced into a bag after each round.
# - Before each draw decide how much you bet and enter it.
# - Start the game with 1000 gold coins (or $ any one).
# - The number of rounds should be variable.
# - If you lose more than half of your money then game is over.
# - Print data as you go along, 
# Bonus: Replace 1 green marble with black marble(10X winner marble)
#        and 1 red marble with white marble(5x loser marble).


from random import random, shuffle, choice

# 6 green and 4 red marbles plus 1 black and 1 white marble.
bag = ["green", "green", "green", "green", "green", "black", "red", "red", "red", "white"]
# shuffle the bag.
shuffle(bag)
initial_money = 1000
curr_money = initial_money
round = 1
marble = "none"

print("******** Welcome to the Marble Betting **********")
while True:
    # Take bet from the user.
    bet = int(input(f'''------------ Round No:{round} ------------\n- Last round: you draw {marble} marble. \n- You have {curr_money} gold coins. \nEnter your bet (0 to exit): '''))
    if (bet == 0):
        print("You left the game.")
        break
    if (bet >= curr_money):
        print(f"You can't bet more than {curr_money} gold coin.")
        continue
    res = choice(bag)
    marble = res
    if res == "green":
        print(f"You draw {res} marble. You win the bet!!!")
        print(f"You received {bet} gold coins.")
        curr_money += bet
    elif res == "black":
        print("Jackpot!!!, you draw black marble, you got 10x reward!")
        print(f"You received {bet * 10} gold coins.")
        curr_money += (bet * 10)
    elif res == "white":
        print("Bad luck you draw white marble, you lost 5x bet.")
        print(f"you lose {bet * 5} gold coins")
        curr_money -= (bet * 5)
    else:
        print("Bad luck you draw {res} marble, you lost the bet.")
        print(f"you lose {bet} gold coins")
        curr_money -= bet
    round += 1
    # Game over if half of money is lost.
    if (curr_money < 0.5 * initial_money):
        print("You lost!!!, Game is over...")
        break
print(f"Starting money: {initial_money}, Ending money: {curr_money}")
print(f"gain/loss% = {(curr_money - initial_money)/initial_money * 100}%")

#OP:
# ******** Welcome to the Marble Betting **********
# ------------ Round No:1 ------------
# - Last round: you draw none marble. 
# - You have 1000 gold coins.
# Enter your bet (0 to exit): 100
# You draw green marble. You win the bet!!!
# You received 100 gold coins.
# ------------ Round No:2 ------------     
# - Last round: you draw green marble.     
# - You have 1100 gold coins.
# Enter your bet (0 to exit): 200
# You draw green marble. You win the bet!!!
# You received 200 gold coins.
# ------------ Round No:3 ------------     
# - Last round: you draw green marble.     
# - You have 1300 gold coins.
# Enter your bet (0 to exit): 0
# You left the game.
# Starting money: 1000, Ending money: 1300
# gain/loss% = 30.0%
