# String Practice:

# Create a Python program that asks the user to input a sentence.
sentence = input("Type a sentence. ")
# Print the first and last letter of the sentence.
print(sentence[0])
print(sentence[12])
# Convert the entire sentence to uppercase and print the result.
print(sentence.upper())
# Find and print a substring from the inputted sentence.
print(sentence[2:6])
# Replace a word in the sentence and print the updated sentence.
print(sentence.replace("die", "live"))

# Input Practice:

# Create a Python program that asks the user for their name, age, and favorite movie.
name = input("What is your name? ")
age = input("How old are you? ")
movie = input("What is your favorite movie? ")
# Print a message back to the user with this information.
print(f"{name} is {age} years old and their favorite movie is {movie}")
# Note: Make sure to convert the age to an integer.

# F-String Practice:

# Create a Python program that asks the user for three objects in the room.
object = input("What is 1 thing in your room? ")
object2 = input("What is another obejct in your room? ")
object3 = input("What is one final thing in your room? ")
# Create variables from these objects and insert those variables into an f-string sentence.
# Print the f-string sentence.
print(f"In {name}'s room there are {object}, {object2}, and {object3}.")

# Advanced String Practice:

# Create a Python program that asks the user for the name of their favorite book, movie, and song.
book = input("What is your favorite book? ")
movie2 = input("What is your favorite movie? ")
song = input("What is your favorite song? ")

# Print a message that says, "Your favorite book is [Book], your favorite movie is [Movie], and your favorite song is [Song]."
print(
    f"Your favorite book is {book}, your favorite movie is {movie2}, and your favorite song is {song}."
)

# Advanced F-String Practice:

# Create a Python program that asks the user for their name, age, and the current year.
name2 = input("What is your name? ")
age2 = input("How old are you? ")
year = input("What year is is? ")
year2 = 2007
# Use f-strings to print a message like: "Hello [Your Name], you were born in [Current Year - Your Age]."
print(f"Hello {name2}, you were born in {year2}.")

# Type Conversion Practice:

# Create a Python program that asks the user for two numbers.
num1 = int(input("What is your first number? "))
num2 = int(input("What is your second number? "))
# Print the sum, difference, product, and quotient of the two numbers.
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
# Note: Make sure to convert the input to integers before performing any calculations.

# Summary Challenge:

# Find a summary of a movie online and create a variable called movie_summary and store the summary in this variable.
movie_summary = "The Machine Girl, is a 2008 Japanese action comedy film written and directed by Noboru Iguchi, and starring Minase Yashiro, Asami, Kentarō Shimazu and Honoka. The plot follows an orphaned Japanese schoolgirl whose life is destroyed when her brother is killed by a son of a Ninja-Yakuza clan. When her hand is cut off, she replaces it with a makeshift machine gun and seeks revenge."
# Print the length of the summary.
print(len(movie_summary))
# Uppercase the entire summary and print it.
print(movie_summary.upper())
# Replace a word in the summary and print the updated summary.
print(movie_summary.replace("film", "movie"))
# Print the last word of the summary.
print(movie_summary[373:380])

# Real Challenge:

# Create a Python program that asks the user for their first and last name, their age, and their favorite color.
full = input("What is your full name? ")
ano = input("What is your age? ")
color = input("What is your favorite color? ")
# Using f-strings, print a message that says, "Hello [First Name] [Last Name], you are [Age] years old and your favorite color is [Favorite Color]."
print(
    f"Hello {full}, you are {ano} years old and your favorite color is {color}."
)
