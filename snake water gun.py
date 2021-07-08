import  random
print("****************Welcome to the game*****************")
n = int(input("Enter how many times you want to play:"))
print("You want to play", n, "times:")

player_score = 0
computer_score = 0

while n > 0:
    comp_choice = random.choice(["s", "w", "g"])
    your_choice = input("Enter your choice (Snake(s), Water(w), Gun(g)): \n")
    your_choice = your_choice.lower()
    if your_choice == comp_choice:
        print("tie")
        print("you choose:", your_choice, " computer choose:", comp_choice)

    elif your_choice == "s" and comp_choice == "w":
        player_score = player_score+1
        print(f"\nYou choose snake and Computer chose water! ")
        print("The snake drank water\n")
        print("You won this round")
        print("You got 1 point\n")
    elif your_choice == "w" and comp_choice == "s":
        computer_score = computer_score+1
        print(f"\nYou choose water and Computer chose snake! ")
        print("The snake drank water\n")
        print("Computer won this round")
        print("Computer got 1 point\n")

    elif your_choice == "w" and comp_choice == "g":
        player_score = player_score+1
        print(f"\nYou choose water and Computer chose gun! ")
        print("The gun was sank on water\n")
        print("You won this round")
        print("You got 1 point\n")

    elif your_choice == "g" and comp_choice == "w":
        computer_score = computer_score+1
        print(f"\nYou choose gun and Computer chose water! ")
        print("The gun was sank on water\n")
        print("Computer won this round")
        print("Computer got 1 point\n")

    elif your_choice == "g" and comp_choice == "s":
        player_score = player_score+1
        print(f"\nYou choose gun and Computer chose snake! ")
        print("The snake was shot\n")
        print("You won this round")
        print("You got 1 point\n")

    elif your_choice == "s" and comp_choice == "g":
        computer_score = computer_score+1
        print(f"\nYou choose snake and Computer chose gun! ")
        print("The snake was shot\n")
        print("Computer won this round")
        print("Computer got 1 point\n")
    else:
        print("please enter valid input\n")
        continue
    n = n-1
    print("\nNo. of guesses left: {}".format(n))

if player_score > computer_score:
    print("You are the winers !!!!!!!!!!!!!\n")
elif player_score < computer_score:
    print("Computer is the winers !!!!!!!!!!\n")
else:
    print("***********Tie***********")
print(f"\nYour points are {player_score} and Computer's points are {computer_score}!\n")












