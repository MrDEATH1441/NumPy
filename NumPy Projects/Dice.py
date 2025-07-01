import numpy as np


# function to count cardinalitty
def count_dice(n):
    # indices where n appeared
    indices = np.where(outcome == n)[0]
    return len(indices)

# function to calculate probabilty of a roll
def prob_roll(n):
    return count_dice(n)/len(outcome)

# rolling dice, 100 times
outcome = np.random.randint(1, 7, size=100)


# Calculating Cardinality and Probability of each outcome

for num in range(1,7):
    print(f"Cardinility of {num} is {count_dice(num)}.")
    print(f'The Relative frequency of {num} is {prob_roll(num):.3f}.', end="\n\n")
    