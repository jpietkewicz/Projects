import sys
from cs50 import SQL

db = SQL("sqlite:///students.db")

if len(sys.argv) != 2:
    print("Usage: python roster.py house")
    sys.exit(1)

house = sys.argv[1]

students = db.execute("select first, middle, last, birth from students where house = ? order by last, birth desc", house)

for student in students:
    if student["middle"] != None:
        print(student["first"] + " " + student["middle"] + " " + student["last"] + ", born " + str(student["birth"]))
    else:
        print(student["first"] + " " + student["last"] + ", born " + str(student["birth"]))