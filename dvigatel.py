def run_game(game_logic, rounds=3):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    for _ in range(rounds):
        question, correct_answer = game_logic()
        print(f"Question: {' '.join(map(str, question))}")
        user_answer = input("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
