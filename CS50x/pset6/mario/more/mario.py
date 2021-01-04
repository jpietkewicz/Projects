from cs50 import get_int

# recursive function to print pyramids


def printpyr(h, max):

    # base case
    if h == 0:
        return

    printpyr(h - 1, max)

    # print leading spaces
    for x in reversed(range(max - h)):
        print(" ", end='')

    # print hashes for first pyramid
    for x in range(h):
        print("#", end='')

    # print mid spaces
    print("  ", end='')

    # print second pyramid
    for x in range(h):
        print("#", end='')

    # skip to next line
    print()


# "do while loop" to check inputs
while True:
    height = get_int("Height: ")
    if (height > 0 and height < 9):
        break
    print("Invalid height.")

printpyr(height, height)