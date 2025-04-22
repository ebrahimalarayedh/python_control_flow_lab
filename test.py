def guess_number():
    import random
    target = random.randint(1, 100)
    chances = 5

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100. You have 5 attempts.")

    while chances > 0:
        user_input = input("Guess a number within the range (1 to 100): ")

        if not user_input.isnumeric():
            chances -= 1
            print(f"Invalid input! You lost a chance. You have {chances} attempts left.")
            continue

        user_guess = int(user_input)

        if not (1 <= user_guess <= 100):
            chances -= 1
            print(f"Out of range! You lost a chance. You have {chances} attempts left.")
            continue

        if user_guess == target:
            print("🎉 Congratulations, you guessed correctly!")
            return

        chances -= 1
        diff = abs(target - user_guess)

        if user_guess > target:
            if diff < 10:
                print(f"Close! Just a bit too high — off by ones. You have {chances} attempts left.")
            else:
                print(f"Your guess is too high — you're off by tens! You have {chances} attempts left.")
        else:
            if diff < 10:
                print(f"Close! Just a bit too low — off by ones. You have {chances} attempts left.")
            else:
                print(f"Your guess is too low — you're off by tens! You have {chances} attempts left.")

        if chances == 1:
            print("⚠️ Last chance!")

    print(f"❌ Sorry, you failed to guess the number in five attempts. The answer was {target}.")


guess_number()