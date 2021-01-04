import csv
from sys import argv, exit
from cs50 import SQL

db = SQL("sqlite:///students.db")

if (len(argv) != 2):
    print("Usage: python import.py characters.csv")
    exit(1)

with open(argv[1], "r") as characters:
    reader = csv.DictReader(characters)

    for row in reader:
        name = row["name"].split()

        # middle name present
        if len(name) == 3:
            first = name[0]
            middle = name[1]
            last = name[2]
        else:
            first = name[0]
            middle = None
            last = name[1]

        db.execute("insert into students (first, middle, last, house, birth) values (?,?,?,?,?)", first, middle, last, row["house"], row["birth"])