import random
from math import gcd
from functools import reduce

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_of_list(numbers):
    return reduce(lcm, numbers)

def generate_lcm_question():
    numbers = [random.randint(1, 50) for _ in range(3)]
    correct_answer = lcm_of_list(numbers)
    return numbers, correct_answer
