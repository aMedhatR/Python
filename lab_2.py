"""Write a function that accepts two arguments (length, start) to
generate an array of a specific length filled with integer numbers
increased by one from start."""

import array as arr

# def arrayCreator(length, start):
#     for i in range(int(start), int(length)):
#         a[i] = 1
#         print(a[i])
#
#
# start = input("enter start ")
# length = input("enter length ")
#
# a = arr.array("i", range(int(length)))
# arrayCreator(length, start)

"""write a function that takes a number as an argument and if the
number divisible by 3 return "Fizz" and if it is divisible by 5 return
"buzz" and if is is divisible by both return " FizzBuzz"""

# def fizzBuzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "FizzBuzz"
#     elif num % 5 == 0:
#         return "buzz"
#     elif num % 3 == 0:
#         return "Fizz"
#
#
# start = input("enter number ")
# value = fizzBuzz(int(start))
# print(value)


"""Write a function which has an input of a string from user then it
will return the same string reversed."""

# def reverser(s):
#     st = ""
#     for i in s:
#         st = i + st
#     return st
#
#
# inp = input("write word ")
# value = reverser(inp)
# print(value)


"""Ask the user for his name then confirm that he has entered his
name(not an empty string/integers). then proceed to ask him for
his email and print all this data (Bonus) check if it is a valid email
or not"""

# def asker():
#     name = input("type your name ")
#     if any(i.isdigit() for i in name) or name == "":
#         value = "you entered wrong value"
#         return value
#     else:
#         email = input("enter your email")
#         value = f"hi {name} your email is {email}"
#         return value
#
#
# val = asker()
# print(val)


"""Write a function that takes a string and prints the
longest alphabetical ordered substring occurred For example, if
the string is ' abdulrahman ' then the output Longest substring in
alphabetical order is: abdu"""


def longest():
    s = input("Enter string: ")
    long = s[0]
    current = s[0]
    for c in s[1:]:
        if c >= current[-1]:
            current += c
        if len(current) > len(long):
            long = current
        else:
            current = c
    print("Longest substring in alphabetical order is:", long)


longest()

"""Write a program which repeatedly reads numbers until the user
enters “done”.
○
Once “done” is entered, print out the total, count, and
average of the numbers.
○
If the user enters anything other than a number, detect their
mistake, print an error message and skip to the next number."""

# def calculater():
#     i = 0
#     sm = 0
#     while True:
#         value = input("enter number ")
#         i = i + 1
#         if value == "done":
#             print(f"number of iteration {i}")
#             print(f"the sum is {sm}")
#             print(f"the average is {sm / i}")
#             break
#         elif not value.isdigit():
#             print("you entered wrong value")
#             continue
#
#         sm = int(value) + sm
#
#
# calculater()


"""Word guessing game (hangman)
○
A list of words will be hardcoded in your program, out of
which the interpreter will
○
choose 1 random word.
○
The user first must input their names
○
Ask the user to guess any alphabet. If the random word
contains that alphabet, it
○
will be shown as the output(with correct placement)
○
Else the program will ask you to guess another alphabet.
○
Give 7 turns maximum to guess the complete word."""
import random

# def hangman():
#     i = 1
#     words = ['car', 'cat', 'rocket']
#     num = random.randrange(0, len(words))
#     name = input("enter your name ")
#
#     def loop():
#         nonlocal i
#         if i < 7:
#             c = input(f"enter random char round {i} ")
#             i += 1
#             if any(c == w for w in words[num]):
#                 print(f"you have correct guss {name} the word is {words[num]}")
#             else:
#                 loop()
#         else:
#             print(f"try the next time {name}")
#     loop()
#
#
# hangman()
