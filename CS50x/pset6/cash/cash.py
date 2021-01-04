from cs50 import get_float

# "do while loop"


while True:
    change = get_float("Change owed: ")
    if (change > 0):
        break

change = int(change * 100)

coins = 0

while True:

    # default
    if (change == 0):
        break

    # if more than one quarter
    elif (change >= 25):
        coins += int(change / 25)
        change %= 25
    # if more than one dime
    elif (change >= 10):
        coins += int(change / 10)
        change %= 10
    # if more than one nickel
    elif (change >= 5):
        coins += int(change / 5)
        change %= 5
    # only pennies
    else:
        coins += change
        change = 0


print(coins)