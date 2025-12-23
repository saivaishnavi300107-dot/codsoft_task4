print("Welcome to ROCK-PAPER-SCISSORS")

turn=0
while True:
    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print('''
RULES 
Rock beats Scissors 
Scissors beats Paper 
Paper beats Rock 
Same choice → Tie
''')
    while True:
        user_choice=input("\nEnter your choice: ")
        if user_choice=="1":
            user_pick="Rock"
            break
        elif user_choice=="2":
            user_pick="Paper"
            break
        elif user_choice=="3":
            user_pick="Scissors"
            break
        else:
            print("Invalid choice.")
            
    options=["Rock", "Paper", "Scissors"]
    index = turn % 3
    computer_choice=options[index]
    turn +=1

    print("\nYou chose: ",user_pick)
    print("Computer chose: ",computer_choice)

    if user_pick==computer_choice:
        print("TIE")
    elif (user_pick=="Rock" and computer_choice=="Scissors") or (user_pick=="Scissors" and computer_choice=="Paper") or (user_pick=="Paper" and computer_choice=="Rock"):
        print("You Win!")
    else:
        print("Computer wins!")
        
    play_again=input("\nDo you want to play again? (yes/no)").lower()
    if play_again !="yes":
        print("Game Over")
        break 


