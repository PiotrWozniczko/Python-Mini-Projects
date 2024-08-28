def adventure_game():
    name = input("Type your name: ")
    print("Welcome", name, "to this adventure!")

    # Choose a weapon
    weapon = input("Choose your weapon (sword/shield/bow): ").lower()

    answer = input("You are on a dirt road, it has come to an end. You can go left or right, which way do you want to go? (left/right) ").lower()

    if answer == "left":
        answer = input("You come to a river, you can walk around it or swim across. Do you want to swim or walk? (swim/walk) ").lower()

        if answer == "swim":
            print("You have been eaten by a crocodile.")
            play_again()
            return
        elif answer == "walk":
            print("You walked for many miles, ran out of water, and lost the game.")
            play_again()
            return
        else:
            print("Not a valid option. You lose.")
            play_again()
            return
    elif answer == "right":
        answer = input("You come to a bridge, it looks wobbly. Do you want to cross it or go back? (cross/back) ").lower()

        if answer == "cross":
            answer = input("You crossed the bridge and met a stranger. Do you want to talk to him? (yes/no) ").lower()

            if answer == "yes":
                print("You talked to the stranger and he gave you a treasure. You win!")
                play_again()
                return
            elif answer == "no":
                print("You ignored the stranger and walked away. You lose.")
                play_again()
                return
            else:
                print("Not a valid option. You lose.")
                play_again()
                return
        elif answer == "back":
            print("You came back to the main road.")
        else:
            print("Not a valid option. You lose.")
            play_again()
            return
    else:
        print("Not a valid option. You lose.")
        play_again()
        return

    # Encounter with a monster
    answer = input("You encounter a fierce dragon! Do you want to fight or run? (fight/run) ").lower()

    if answer == "fight":
        if weapon == "sword":
            print("You bravely fight the dragon with your sword and defeat it. You win!")
        elif weapon == "shield":
            print("You defend yourself with your shield, but the dragon's fire is too strong. You lose.")
        elif weapon == "bow":
            print("You shoot arrows at the dragon from a distance and defeat it. You win!")
        else:
            print("You have no weapon to fight with. You lose.")
    elif answer == "run":
        print("You run away safely, but the adventure ends here. You lose.")
    else:
        print("Not a valid option. You lose.")

    play_again()

def play_again():
    answer = input("Do you want to play again? (yes/no) ").lower()
    if answer == "yes":
        adventure_game()
    else:
        print("Thanks for playing!")

adventure_game()