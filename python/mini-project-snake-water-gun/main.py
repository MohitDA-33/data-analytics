import random   # Random is a module in python that generates random numbers/integers.

def game_win(user, computer):   # This is a funtion that will decide everything.
    if user == computer:
        return None

    # snake vs water
    if user == "w" and computer == "s":
        return False
    if user == "s" and computer == "w":
        return True
    
    # g vs s
    if user == "g" and computer == "s":
        return True
    if user == "s" and computer == "g":
        return False
    
    # w vs g 
    if user == "w" and computer == "g":
        return True
    if user == "g" and computer == "w":
        return False

rand_no = random.randint(1, 3)

print("Computer's turn: snake(s), water(w), gun(g) : ")   # It will ask the computer to choose in between s, w, g.

if rand_no ==1:
    computer = "s"

elif rand_no ==2:
    computer = "w"

else:
    computer = "g"

user = input("Your's turn: snake(s), water(w), gun(g) : ").lower()   # If you have written in capital letter, .lower will return a new string in lowercase.

result = game_win(user, computer)   # Prints Draw if none, True if you won, and False if you lose.

print(f"Computer chose: {computer}")
print(f"User chose: {user}")

if result is None:   # Cause of this, what i have noticed if you write a wrong value it will print draw!.
    print("Its a draw!")

elif result:
    print("You win")

else:
    print("You lose")