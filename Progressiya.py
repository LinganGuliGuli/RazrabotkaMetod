import random

def generate_geo_progression_question():
    first_term = random.randint(1, 10)
    ratio = random.randint(2, 5)
    length = random.randint(5, 10)
    progression = [first_term * (ratio ** i) for i in range(length)]

    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'

    return progression, correct_answer
