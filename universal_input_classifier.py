def is_odd_or_even(number):
    if number % 2 == 0:
        return f"{number} is Even."
    else:
        return f"{number} is Odd."

def is_vowel_or_consonant(letter):
    vowels = "aeiouAEIOU"
    if letter.isalpha():
        if letter in vowels:
            return f"{letter} is a Vowel."
        else:
            return f"{letter} is a Consonant."
    return "Invalid input. Please enter a letter."

def is_special_character(character):
    if not character.isalnum():
        return f"{character} is a Special Character."
    return f"{character} is not a Special Character."

def combined_function():
    value = input("Enter a value (number or letter or character): ")
    if value.isdigit():
        print(is_odd_or_even(int(value)))
    elif value.isalpha():
        print(is_vowel_or_consonant(value))
    elif len(value) == 1:
        print(is_special_character(value))
    else:
        print("Invalid input.")

def main():
    while True:
        print("\nMenu:")
        print("1. Determine if a number is Odd or Even")
        print("2. Determine if a letter is a Vowel or Consonant")
        print("3. Determine if a character is a Special Character")
        print("4. Combination of all functions")
        print("Type 'STOP' to exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            number = input("Enter a number: ")
            if number.isdigit():
                print(is_odd_or_even(int(number)))
            else:
                print("Invalid input. Please enter a number.")
        elif choice == "2":
            letter = input("Enter a letter: ")
            if len(letter) == 1 and letter.isalpha():
                print(is_vowel_or_consonant(letter))
            else:
                print("Invalid input. Please enter a single letter.")
        elif choice == "3":
            character = input("Enter a character: ")
            if len(character) == 1:
                print(is_special_character(character))
            else:
                print("Invalid input. Please enter a single character.")
        elif choice == "4":
            combined_function()
        elif choice.upper() == "STOP":
            print("Program stopped.")
            break
        else:
            print("Invalid choice. Please select a number between 1-4 or type 'STOP' to exit.")

if __name__ == "__main__":
    main()
