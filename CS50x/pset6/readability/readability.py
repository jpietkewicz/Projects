from cs50 import get_string
import string

text = get_string("Text: ")

letters = 0
words = 1
sentences = 0

# loop through string to add
for c in text:
    # if letter
    if c.isalpha():
        letters += 1
    # if space (between words)
    elif c.isspace():
        words += 1
    # if end of sentence
    elif c == "." or c == "!" or c == "?":
        sentences += 1

L = (letters / words) * 100
S = (sentences / words) * 100

# Coleman-Liau index equation
index = 0.0588 * L - 0.296 * S - 15.8

# check index to determine grade level
if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print(f"Grade {round(index)}")