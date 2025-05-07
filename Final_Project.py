# Function to display character details
def display_character(character):
    print("\nCharacter Created!")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Race: {character['race']}")
    print(f"Strength: {character['strength']}")
    print(f"Intelligence: {character['intelligence']}")
    print(f"Charisma: {character['charisma']}")

# Function to create a character
def create_character():
    character = {}

    # Collecting character details
    print("Welcome to the Character Creator!\n")
    character['name'] = input("Enter your character's name: ")

    # Choose class
    print("\nChoose a class for your character:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Thief")
    print("4. Archer")
    class_choice = input("Enter the number of the class: ")

    if class_choice == '1':
        character['class'] = "Warrior"
    elif class_choice == '2':
        character['class'] = "Mage"
    elif class_choice == '3':
        character['class'] = "Thief"
    elif class_choice == '4':
        character['class'] = "Archer"
    else:
        character['class'] = "Unknown"

    # Choose race
    print("\nChoose a race for your character:")
    print("1. Human")
    print("2. Elf")
    print("3. Dwarf")
    print("4. Orc")
    race_choice = input("Enter the number of the race: ")

    if race_choice == '1':
        character['race'] = "Human"
    elif race_choice == '2':
        character['race'] = "Elf"
    elif race_choice == '3':
        character['race'] = "Dwarf"
    elif race_choice == '4':
        character['race'] = "Orc"
    else:
        character['race'] = "Unknown"

    # Random abilities (You can adjust this to have more detailed options)
    print("\nNow, assign some abilities to your character (on a scale of 1 to 10):")
    character['strength'] = int(input("Strength: "))
    character['intelligence'] = int(input("Intelligence: "))
    character['charisma'] = int(input("Charisma: "))

    return character

# Main program loop
def main():
    while True:
        print("\nCharacter Creator Menu:")
        print("1. Create a new character")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            character = create_character()
            display_character(character)
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
