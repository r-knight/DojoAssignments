import random
def randInt(lower=0, upper=100):
    if lower > upper:
        temp = lower
        lower = upper
        upper = lower
    randNum = int(random.random()*(upper-lower)) + lower
    return (randNum)