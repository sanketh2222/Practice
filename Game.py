import random
options=["snake","water","gun"]
computer_points=0
user_points=0
computer_choice=random.choice(options)
count=0
#print(computer_choice)


def game_start():
    choice=input("Snake\nWater\nGun")
    print(count)
    return  choice


while count<3:
    while(1):
        user_choice=game_start()
        if user_choice.lower() not in options:
            print("Invalid choice\n")
            game_start()
        else:
            count=count+1
            print(computer_choice+"!")
            print(count)
            break

    if user_choice.lower()=="snake" and computer_choice=="snake":
            pass
    elif user_choice.lower()=="gun" and computer_choice=="snake":
            user_points=user_points+1
    elif user_choice.lower() == "water" and computer_choice == "snake":
        computer_points = computer_points + 1
    elif user_choice.lower()=="snake" and computer_choice=="water":
            user_points=user_points+1
    elif user_choice.lower()=="gun" and computer_choice=="water":
            computer_points = computer_points + 1
    elif user_choice.lower() == "water" and computer_choice == "water":
            pass
    if user_choice.lower()=="snake" and computer_choice=="gun":
            computer_points = computer_points + 1
    elif user_choice.lower()=="gun" and computer_choice=="gun":
            pass
    elif user_choice.lower() == "water" and computer_choice == "gun":
            user_points=user_points+1


if user_points>computer_points:
    final=f"you win with {user_points} points\nComputer score {computer_points}"
    print(final)
elif computer_points>user_points:
    final=f"I win with {computer_points} points\nYour score {user_points}"
    print(final)
else:
    print("Its a Tie")

