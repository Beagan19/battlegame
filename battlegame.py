# game characters and stats


wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"

wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 80

wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 110

dragon_hp = 300
dragon_damage = 50

# prompt player to choose character
while True:
    print("1) " + wizard)
    print("2) " + elf)
    print("3) " + human)
    print("4) " + orc)
    print("5) Exit")
    character = input("Choose your character: ").upper()

    # While loop for player choice
    while True:
        if character == "1" or character == "WIZARD":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            print("You have chosen the character: " + character)
            print("Health: " + str(my_hp))
            print("Damage: " + str(my_damage))
            break

        elif character == "2" or character == "ELF":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            print("You have chosen the character: " + character)
            print("Health: " + str(my_hp))
            print("Damage: " + str(my_damage))
            break

        elif character == "3" or character == "HUMAN":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            print("You have chosen the character: " + character)
            print("Health: " + str(my_hp))
            print("Damage: " + str(my_damage))
            break

        elif character == "4" or character == "ORC":
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            print("You have chosen the character: " + character)
            print("Health: " + str(my_hp))
            print("Damage: " + str(my_damage))
            break
        elif character == "5" or character == "EXIT":
            False
            print("Goodbye!")
            exit()
            break
        else:
            print("Unknown character")
            continue

    # Battle with the dragon

    while True:
        dragon_hp = dragon_hp - my_damage
        print("The " + character + " damaged the Dragon!")
        print("The Dragon's hitpoints are now: " + str(dragon_hp))
        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            break
        my_hp = my_hp - dragon_damage
        print("The Dragon strikes back at " + character)
        print("The " + character + "'s hitpoints are now: " + str(my_hp))
        if my_hp <= 0:
            print("The " + character + " has lost the battle.")
            break

    # Play again option

    play_again_option = input("Do you want to play again?").upper()
    if play_again_option == "YES":
        True
    elif play_again_option == "NO":
        print("Thanks for playing!")
