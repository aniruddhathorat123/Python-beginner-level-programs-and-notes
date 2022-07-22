# Guess the correct number in 3 guesses. If you don’t get it right 
# after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, 
# so If you want to see prints during while loop, then print to the input box

# Modification 1: number 1-100, tell user if guess is too high/low, 
# and let them have 5-10 guesses.
# Tip:( remember you won’t see print statements during execution, 
# so If you want to see prints during while loop, print to the input box
# (This is specific to this platform)

guess_limit = 5
num = 67
guess_num = int(input("Guess the number(1-100): "))

while guess_limit > 0:
    if guess_num == num:
        print(f"Correct guess!, you guess {num}")
        break
    elif guess_num > num:
        guess_num = int(input(f"Your guess is too high!, Guess again(1-100): (last guess: {guess_num}): "))
    else:
        guess_num = int(input(f"Your guess is too low!, Guess again(1-100): (last guess: {guess_num}): "))
    guess_limit -= 1

if num != guess_num:
    print(f"Sorry you lose.., guess number is {num}")

#### OP #####
# Guess the number(1-100): 23
# Your guess is too low!, Guess again(1-100): (last guess: 23): 45
# Your guess is too low!, Guess again(1-100): (last guess: 45): 78
# Your guess is too high!, Guess again(1-100): (last guess: 78): 60
# Your guess is too low!, Guess again(1-100): (last guess: 60): 65
# Your guess is too low!, Guess again(1-100): (last guess: 65): 68
# Sorry you lose.., guess number is 67
