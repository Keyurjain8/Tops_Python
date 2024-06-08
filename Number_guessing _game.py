import random

print("Welcome to the Number Guessing Game!")
print()
print("There are 3 levels in this game. You have two lifelines for all levels combined.")
print()

# Initialize variables
total_lifelines = 2

# Level 1
level = 1
max_num = 100
max_chances = 5
computer_guess = random.randint(1, max_num)
chances = max_chances

print(f"Level {level}: Guess a number between 1 and {max_num}. You have {max_chances} chances.")
print()

while chances > 0:
    user_guess = int(input("Enter your guess: "))
    print()
    
    if user_guess > computer_guess:
        print("Hint: Guess a lower number.")
        print()
    elif user_guess < computer_guess:
        print("Hint: Guess a higher number.")
        print()
    else:
        print("Right Guess!")
        print()
        print(f"CONGRATULATIONS. YOU WON LEVEL {level}!")
        print()
        break

    chances -= 1
    print(f"You have {chances} chances left.")
    print()

    if total_lifelines > 0 and chances > 0:
        use_lifeline = input(f"Do you want to use a lifeline? (yes/no) You have {total_lifelines} lifelines left: ").lower()
        print()
        if use_lifeline == 'yes':
            print(f"Lifeline: The correct number is {computer_guess}.")
            print()
            total_lifelines -= 1
            break

if chances == 0:
    print("Sorry, you've run out of chances.")
    print()
    print(f"The correct number was {computer_guess}.")
    print()
    print("Game Over!")
    print()
else:
    # Level 2
    level = 2
    max_num = 150
    max_chances = 8
    computer_guess = random.randint(1, max_num)
    chances = max_chances

    print(f"Level {level}: Guess a number between 1 and {max_num}. You have {max_chances} chances.")
    print()

    while chances > 0:
        user_guess = int(input("Enter your guess: "))
        print()
        
        if user_guess > computer_guess:
            print("Hint: Guess a lower number.")
            print()
        elif user_guess < computer_guess:
            print("Hint: Guess a higher number.")
            print()
        else:
            print("Right Guess!")
            print()
            print(f"CONGRATULATIONS. YOU WON LEVEL {level}!")
            print()
            break

        chances -= 1
        print(f"You have {chances} chances left.")
        print()

        if total_lifelines > 0 and chances > 0:
            use_lifeline = input(f"Do you want to use a lifeline? (yes/no) You have {total_lifelines} lifelines left: ").lower()
            print()
            if use_lifeline == 'yes':
                print(f"Lifeline: The correct number is {computer_guess}.")
                print()
                total_lifelines -= 1
                break

    if chances == 0:
        print("Sorry, you've run out of chances.")
        print()
        print(f"The correct number was {computer_guess}.")
        print()
        print("Game Over!")
        print()
    else:
        # Level 3
        level = 3
        max_num = 200
        max_chances = 12
        computer_guess = random.randint(1, max_num)
        chances = max_chances

        print(f"Level {level}: Guess a number between 1 and {max_num}. You have {max_chances} chances.")
        print()

        while chances > 0:
            user_guess = int(input("Enter your guess: "))
            print()
            
            if user_guess > computer_guess:
                print("Hint: Guess a lower number.")
                print()
            elif user_guess < computer_guess:
                print("Hint: Guess a higher number.")
                print()
            else:
                print("Right Guess!")
                print()
                print(f"CONGRATULATIONS. YOU WON LEVEL {level}!")
                print()
                break

            chances -= 1
            print(f"You have {chances} chances left.")
            print()

            if total_lifelines > 0 and chances > 0:
                use_lifeline = input(f"Do you want to use a lifeline? (yes/no) You have {total_lifelines} lifelines left: ").lower()
                print()
                if use_lifeline == 'yes':
                    
                    print(f"Lifeline: The correct number is {computer_guess}.")
                    print()
                    total_lifelines -= 1
                    break

        if chances == 0:
            print("Sorry, you've run out of chances.")
            print()
            print(f"The correct number was {computer_guess}.") 
            print()
            print("Game Over!")
            print()
        else:
            print("CONGRATULATIONS. YOU COMPLETED ALL LEVELS!")
