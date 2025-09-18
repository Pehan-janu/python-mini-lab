# File name suggestion: adventure_journey.py

name = input("Type your name: ")
print(f"Welcome, {name}, to this thrilling adventure!")

answer = input(
    "You are on a dirt road. It comes to an end and you can go left or right. Which way do you choose? ").lower()

if answer == "left":
    answer = input(
        "You arrive at a river. Do you want to walk around it or swim across? (walk/swim): ").lower()

    if answer == "swim":
        print("You bravely swam across, but an alligator was waiting... You lose!")
    elif answer == "walk":
        print("You walked for miles and ran out of water. You lose!")
    else:
        print("Invalid choice. You lose.")

elif answer == "right":
    answer = input(
        "You come across a wobbly bridge. Do you cross it or go back? (cross/back): ").lower()

    if answer == "back":
        print("You decided to go back. Sometimes caution is key, but you lose this time.")
    elif answer == "cross":
        answer = input(
            "You successfully cross the bridge and meet a stranger. Do you talk to them? (yes/no): ").lower()

        if answer == "yes":
            print("The stranger shares a treasure map with you. You WIN!")
        elif answer == "no":
            print("The stranger feels ignored and disappears. You lose.")
        else:
            print("Invalid choice. You lose.")
    else:
        print("Invalid choice. You lose.")

else:
    print("Invalid choice. You lose.")

print(f"Thanks for playing, {name}! Hope you enjoyed the adventure.")
