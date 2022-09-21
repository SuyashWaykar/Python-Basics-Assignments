import logging
logging.basicConfig(filename="Assignment_17", level=logging.INFO)
logging.info("Assignment 17 in Python Basics")

# 1 : Assign teh value 7 to the variable guess_me. then, write the conditional tests (if, else, and elif) to print the
# string 'too low' if guess_me is less than 7, 'too high' if greater than 7, and 'just right' if equal to 7.

guess_me = 7
if guess_me < 7 :
    print('too low')
elif guess_me > 7 :
    print('too high')
else:
    print('just right')

# 2 : Assign the value 7 to the variable guess_me and the value 1 to the variable start. Write a while loop that
# compares start with guess_me. Print too low if start is less than guess me. If start equals guess_me, print
# 'found it!' and exit the loop. If start is greater than guess_me, print 'oops' and exit the loop. Increment start at
# the end of the loop.

guess_me = 7
start = 1

while True :
    if start < guess_me :
        print("too low")
    elif start == guess_me :
        print("found it!")
        break
    else :
        print("oops")
        break
    start += 1

# 3 : Print the following values of the list [3, 2, 1, 0] using a loop.

list = [3, 2, 1, 0]
for num in list :
    print(num)

# 4 : Use a list comprehension to make a list of the even numbers in range(10).

Even_numbers = [num for num in range(10) if num % 2 == 0]
print(Even_numbers)

# 5 : Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the keys, and use the
# square of each key as its value.

limit = 10
squares = {num: num * num for num in range(limit)}
print(squares)

# 6 : Construct the set odd from the odd numbers in the range using a set comprehension (10).

odd = {num for num in range(10) if num % 2 == 1}
print(odd)

# 7 : Use a generator comprehension to return the string 'Got ' and a number for the numbers in range(10). Iterate
# through this by using a for loop.

string_generator = ('Got ' + str(num) for num in range(10))
for item in string_generator:
    print(item)

# 8 : Define a function called good that returns the list['Harry','Ron,'Hermione'].

def good() :
    return["Harry","Ron","Hermione"]
print(good())

# 9 : Define a generator function called get_odds that returns the odd numbers from range(10). Use a for loop to find
# and print the third value returned.

def get_odds() :
    return{num for num in range(10) if num % 2 == 1}
print(get_odds())
count = 0
for num in get_odds() :
    if count == 2 :
        print(num)
        break
    count += 1

# 10 : Define an exception called OopsException. Raise this exception to see what happens. Then write the code to catch
# this exception and print 'Caught an oops'.

class OopsException(Exception) :
    pass

def with_exception(a):
    if a < 0:
        raise OopsException(a)

try:
    with_exception(-1)
except OopsException as err:
    print("Caught an oops")

# 11 : Use zip() to make a dictionary called movies that pairs these
# lists: titles = ['Creature of Habit', 'Crewel Fate'] and plots = ['A nun turns into a monster','A haunted yarn shop'].

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']

movies = {}
for titles, plots in zip(titles,plots) :
    movies[titles] = plots
print(movies)



# FINISH

