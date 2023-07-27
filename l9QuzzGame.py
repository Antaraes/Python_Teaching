print("Welcome to our game")

playing = input("Do you want to play Yes?") #global  scope

if playing.lower() != "yes":
    quit()
# refactor
else:
    print("Let's play'")
    score = 0 # int
    answer = input("Where is the UK in the World?")
    if answer.lower() == "near french":
        print("Correct")
        score = score + 10 # 0 + 10
        print(f"Score = {score}") # 0
    else:
        print("Incorrect")
        score = score - 10
        print("Score = " + str(score))  # 0

    answer = input("What does CPU stands for?")
    if answer.lower() == "central processing unit":
        print("Correct")
        score += 10
        print("Score = " + str(score))
    else:
        print("Incorrect")
        score -= 10
        print("Score = " + str(score))
    print(f"You got {score}")


