import random

for i in range(5):
    player_choice = int(input("Enter a Integer value[1-100]: "))
    computer_choice = random.randint(1,100)
    if (player_choice > 0 and player_choice < 100) and (computer_choice > 0 and computer_choice < 100):
        if player_choice > computer_choice:
            print("Its bigger than expected number")
            print("expected number:%d" % computer_choice)
        elif player_choice < computer_choice:
            print("Its lower than expected number")
        else:
            print("Its expected number")
    else:
        print("unwanted range")