import random

def variance(data):
    mean = sum(data)/len(data)
    variances = [(d-mean)**2 for d in data]
    return sum(variances)/len(data) - 1

def mean(data):
    return sum(data)/len(data)

def dice_rolls(num_dice):
    return random.choices([1, 2, 3, 4, 5, 6], weights=[1, 1, 1, 1, 1, 1], k=num_dice)

def sum_dice_rolls(num_dice):
    roll_results = random.choices([1, 2, 3, 4, 5, 6], weights=[1, 1, 1, 1, 1, 1], k=num_dice)
    return sum(roll_results)