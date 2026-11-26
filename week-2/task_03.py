# ============================================================
#  BioSkillz CodeStart — Python Foundations | Batch 01
#  TASK 03: Loops (Session 03)
# ============================================================
#
#  Name            : Adeel Hussain
#  GitHub username : adeelhussain20255
#  Date            : 11/26/2026
#
#  ⚠ BEFORE YOU START
#  Practise the Session 03 examples and the Week 2 Reference
#  Guide first. Try every question yourself before asking for
#  help. Errors are part of learning!
#
#  HOW TO SUBMIT
#  1. Write your code under each question in this file.
#  2. Run the file in VS Code and make sure it works.
#  3. Rename it to:  yourname_task_03.py   (no spaces)
#                    e.g. ali_raza_task_03.py
#  4. Upload it to your GitHub repository.
#  5. Submit your GitHub link as instructed by the team.
#
#  DEADLINE: Friday, 27 November 2026, 9:00 PM (PKT)
#
#  TIP: Code shown inside comments (lines starting with #) does
#  not run. To test it, copy it below and remove the #.
# ============================================================


# ############################################################
#  PART A: SESSION EXERCISES (from the slides)
# ############################################################

# ------------------------------------------------------------
# Exercise 1: Predict the output
# ------------------------------------------------------------
# Write your prediction for each snippet. Then copy the code
# below, run it, and check.
#
# 1)  for i in range(3):
#         print("Hi", i)
#     My prediction: Hi 0
#                    Hi 1
#                    Hi 2
#
# 2)  x = 0
#     for i in range(1, 4):
#         x += i * 2
#     print(x)
#     My prediction: 12
#
# 3)  for i in range(3, 0, -1):
#         print(i, end="")
#     My prediction: 321
#
# 4)  for ch in "code":
#         if ch == "d": break
#         print(ch, end="")
#     My prediction: co
#
# 5)  for i in range(6):
#         if i % 3 == 0: continue
#         print(i, end=" ")
#     My prediction: 1 2 4 5
#
# 6)  for i in range(2, 10, 3):
#         print(i, end=" ")
#     My prediction: 2 5 8 
#===========================================================
# Your code goes here:
#===========================================================
for i in range(3):
    print("Hi", i)
#===========================================================
x = 0
for i in range(1, 4):
    x += i * 2
print(x)
#===========================================================
for i in range(3, 0, -1):
       print(i, end="")
#===========================================================
for ch in "code":
   if ch == "d": break    
   print(ch, end="")
#===========================================================
for i in range(6):
  if i % 3 == 0: continue
  print(i, end=" ")
#===========================================================
for i in range(2, 10, 3):
   print(i, end=" ")
#===========================================================
#===========================================================
# ------------------------------------------------------------
# Exercise 2: Find and fix 4 bugs
# ------------------------------------------------------------
# This program should print 1 to 5, then the sum of 1 to 5
# (which is 15). It has 4 bugs. Only ONE gives an error
# message; the other three run but behave wrongly.
#
#     count = 1
#     while count <= 5
#         print(count)
#
#     for i in range(1, 5):
#         total = 0
#         total += i
#     print("Sum of 1 to 5:", total)
#
# Write the fixed program below, and add a comment next to
# each fix explaining the bug.
#
#===========================================================
# Your code goes here:
#===========================================================
count = 1 
while count <= 5: # a : was missing here 
   print(count)
   count += 1 # this has to increment to avoid infinite looping
 

total = 0  # move out the total out of the loop so the values are not reseted on every iteration
for i in range(1, count): # count here because this make things more robust and 5 only runs the loop 1-4 times but we need the sum of 5 numbers
  total += i 

print("Sum of 1 to 5:", total) 
#===========================================================
#===========================================================
# ------------------------------------------------------------
# Exercise 3: Number guessing game
# ------------------------------------------------------------
# Write a game that:
#   1. Picks a secret number from 1 to 10
#   2. Keeps asking for a guess (while loop)
#   3. Says "Too high" or "Too low" (if-elif)
#   4. Stops when the guess is correct (break)
#   5. Prints how many tries it took (counter)
#
# Start with these two lines:
#     import random
#     secret = random.randint(1, 10)
#
# Example:
#   Guess (1-10): 5
#   Too low
#   Guess (1-10): 7
#   Correct! You took 2 tries
#
#===========================================================
# Your code goes here:
#===========================================================
import random as rn 
secret = rn.randint(1, 10) # picks a random numer for each run

tries = 0

while True:
    num = input("Guess (1-10): ")
    
    if not num.isdigit():
        print("Numbers only, please!") # can add tries +=1 here if want to count these tries too (optional)
        continue 
    else:
        num = int(num)
        tries += 1

    if num < secret:
        print("Too low")
    elif num > secret:
        print("Too high")
    else:
        print(f"Correct! you took {tries} tries")
        break
#===========================================================
#===========================================================

# ############################################################
#  PART B: TASKS
# ############################################################

# ------------------------------------------------------------
# Task 1: Multiplication table
# ------------------------------------------------------------
# Ask the user for a number and print its table from 1 to 10.
#
# Example:
#   Enter a number: 7
#   7 x 1 = 7
#   7 x 2 = 14
#   ...
#   7 x 10 = 70
#
#===========================================================
# Your code goes here:
#===========================================================
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
#===========================================================
#===========================================================
# ------------------------------------------------------------
# Task 2: Predict the output
# ------------------------------------------------------------
# Write your prediction first, then run the code to check.
# If your prediction was wrong, write one line explaining why.
#
# 1)  for i in range(1, 4):
#         print(i * i, end=" ")
#     My prediction: 1 4 9
#
# 2)  total = 0
#     for i in range(0, 10, 3):
#         total += i
#     print(total)
#     My prediction: 18 
#
# 3)  n = 3
#     while n > 0:
#         print(n)
#         n -= 1
#     My prediction: 3
#                    2
#                    1
#
# 4)  for ch in "loop":
#         if ch == "o":
#             continue
#         print(ch, end="")
#     My prediction: lp
#
# 5)  count = 0
#     for i in range(5):
#         for j in range(2):
#             count += 1
#     print(count)
#     My prediction: 10 --> (5 * 2 = 10)
#
# 6)  for i in range(5, 0, -2):
#         print(i, end=" ")
#     My prediction: 5 3 1

# ------------------------------------------------------------
# Task 3: Find and fix the bugs
# ------------------------------------------------------------
# This program should:
#   - print the sum of the even numbers from 1 to 10 (answer: 30)
#   - then count down from 10 to 1
# It has 4 bugs.
#
#     total = 0
#     for i in range(1, 10)
#         if i % 2 = 0:
#             total += i
#     print("Sum of even numbers 1-10:", total)
#
#     count = 10
#     while count > 0:
#         print(count)
#
# Write the fixed program below, and add a comment next to
# each fix explaining the bug.
#===========================================================
# Your code goes here:
#===========================================================
total = 0
for i in range(1, 11): # a : missing and the stop valuse should be 11 not 10
    if i % 2 == 0: # == weres suppose to be used here stead of single =
        total += i
print("Sum of even numbers 1-10:", total)

count = 10
while count > 0:
    print(count)
    count -= 1 # have to add this to avoid the infinite looping
#===========================================================
#===========================================================
# ------------------------------------------------------------
# Task 4: Character counter
# ------------------------------------------------------------
# Ask the user for a sentence. Using a loop, count and print:
#   - the number of vowels (a, e, i, o, u)
#   - the number of digits
#   - the number of spaces
#
# Example:
#   Sentence: CodeStart has 8 sessions
#   Vowels: 7
#   Digits: 1
#   Spaces: 3
#
# Hint: use .lower(), in, .isdigit() and counter variables.
#
# Write your code below:
#===========================================================
# Your code goes here:
#===========================================================
isSpace = 0
isVowel = 0
isDigit = 0

sen = input("Sentence: ")
sen = sen.lower()

for ch in sen:
    if ch in "aeiou":
        isVowel +=1
    elif ch.isdigit():
        isDigit +=1
    elif ch == " ":
        isSpace +=1
        
print(f"Vowels: {isVowel}\nDigits: {isDigit}\nSpace: {isSpace}")
#===========================================================
#===========================================================
# ------------------------------------------------------------
# Task 5: Your field
# ------------------------------------------------------------
# Solve a small problem from YOUR field using a loop.
# Choose ONE option (or create your own):
#
#   Option A: GC content
#     Ask for a DNA sequence (e.g. ATGCGCAT). Count the G and C
#     letters with a loop and print the GC content as a
#     percentage with an f-string.
#     Example: GC content: 50.0%
#
#   Option B: Lab readings
#     Ask how many readings there are (n). Then ask for each
#     reading in a loop and print the average, minimum and
#     maximum.
#
#   Option C: Temperature Tracker (Physics Lab)
#     Ask the user how many temperature readings they took.
#     Then, use a loop to ask for each temperature in Celsius 
#     (allow decimals).
#     Count how many are "Freezing" (<= 0) and how many are 
#     "Boiling" (>= 100). Calculate the average temperature.
#     Example: 
#       How many readings? 3
#       Reading 1: -5
#       Reading 2: 25.5
#       Reading 3: 105
#       Output -> Freezing: 1, Boiling: 1, Average: 41.8°C
#
#     Hint: Use float() for the inputs, a loop to collect data, 
#     if/elif for the freezing/boiling checks, and counters!
#
#===========================================================
# Your code goes here: (Option: C)
#===========================================================
nOread = int(input("How many reading? "))
isFrez = 0
isBoil = 0
count = 0
total = 0

if nOread > 0:
    for i in range(nOread):
        read = float(input(f"Reading {i+1}: "))
        
        count +=1
        total += read

        if read <= 0:
            isFrez +=1
        elif read >= 100:
            isBoil +=1

    averageTemp = (total / count)
    print(f"Freezing: {isFrez}\nBoiling: {isBoil}\nAverage: {averageTemp:.1f}°C")
    
else:
    print("No readings were entered.")
#===========================================================
#===========================================================