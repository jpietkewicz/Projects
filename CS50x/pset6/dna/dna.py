import csv
import sys

# wrong command line argument check
if (len(sys.argv) != 3):
    print("Usage: python dna.py data.csv sequence.txt")
    sys.exit(1)

# open and read sequence into string
with open(sys.argv[2], "r") as sequenceFile:
    sequence = sequenceFile.read()

# check if subString is in seq for matching DNA


def contains_sequence(subString, seq):
    if subString in seq:
        return True
    return False


# open database to read STR numbers
with open(sys.argv[1], "r") as database:
    reader = csv.reader(database)

    # get field names to extend STR into subString for checking
    headers = next(reader)

    for row in reader:
        # store name to print
        name = row[0]

        counter = 1
        while (counter < len(row)):
            # multiply header (STR) by how many consecutive occurrences for each person
            seq = headers[counter] * int(row[counter])

            # if sequence contains person-specific STR repeated and only that string
            if contains_sequence(seq, sequence) and not contains_sequence(seq + headers[counter], sequence):
                # matched all STR sequences
                if (counter == len(row) - 1):
                    print(name)
                    sys.exit()
                counter += 1
            else:
                break

    print("No Match")