def start_game():
    print("welcome to the game!!!")

    health =100
    player_name = input("What is your name?")
    inventory = []


    while health > 0:
     print(f"welcome {player_name} your journey begins now, let us run")

     choice=print("There is a cave in front of you \n should you enter ,answer(yes,no):").lower().strip()

    if choice == "yes":
       print(f"great choice {player_name} their you get the sword")
       inventory.append("sword")

    elif choice == "no":
       health-=20
       print(f"You will be eaten by the wolf, health deduced to {health} ")


    if health <=0:
       print("game over!!!")

    start_game()       
       
       
