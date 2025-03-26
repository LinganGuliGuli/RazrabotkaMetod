from dvigatel import run_game
from Kratnoye import generate_lcm_question
from Progressiya import generate_geo_progression_question

if __name__ == "__main__":
    print("Choose a game:")
    print("1. LCM Game")
    print("2. Geometric Progression Game")
    choice = input("Enter the number of the game: ")

    if choice == '1':
        run_game(generate_lcm_question)
    elif choice == '2':
        run_game(generate_geo_progression_question)
    else:
        print("Invalid choice.")
