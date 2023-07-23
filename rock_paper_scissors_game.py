import random

user_wins = 0
computer_wins = 0
            # 0 ,  1 ,2
options = ['rock','paper','scissors']

while True:
    userinput = input("Do you want to paly? (y/n): ").lower()
    if userinput == 'n':
        break

    elif userinput == 'y':
        userinput = input("Type Rock/paper/Scissors? : ").lower()
        random_number = random.randint(0, 2)
        computer_pick = options[random_number]  # 0 or 1 or 2
        print("Computer Pick", computer_pick)
        if userinput == 'rock' and computer_pick == 'scissors':
            print("User wins")
            user_wins += 1
        elif userinput == 'paper' and computer_pick == 'rock':
            print("User wins")
            user_wins += 1
        elif userinput == 'scissors' and computer_pick == 'paper':
            print("User wins")
            user_wins += 1
        else:
            print("Computer wins")
            computer_wins += 1
    else:
        print("Inavalid input")
        continue

print(f"You won {user_wins} times")






