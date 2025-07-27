from random import random

random_float = random() * 10
if random_float >= 5.5:
    print(f"Number {random_float} = Heads")
else:
    print(f"Number {random_float} = Tails")
