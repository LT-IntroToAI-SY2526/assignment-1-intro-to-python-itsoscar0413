# Assignment 1: AI-Generated Python Problems
# Name: Oscar Huerta

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
I'm learning Python basics in a high school programming class. I have experience with Javascript as i took APCSP and scored a 4, 
so I have a good understand of the basics of coding, but I don't understand anything about Pythons. Could you create 5 practice
problems that cover the basic foundations of Python, like basic stuff I should know?

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: Problem 1: Hello, Input! Goal: Ask for user input and print a greeting.

Input: In Python, you use the input() function to get text typed by the user.

Storing input: Store what the user types in a variable, like name = input("What is your name? ").

Output: Use print() to display text on the screen.

String concatenation: Combine the greeting string and the name variable. In Python, you can do this using commas inside print() (which adds a space), or use string formatting.

Tip: Think about how you might do alert("Hello, " + name) in JavaScript — in Python, it's similar but with print().
"""

"""
Problem 2: Even or Odd Goal: Check if a number is even or odd.

Use input() to get the number as text.

Convert the input string to an integer with int().

Use the modulo operator % to find the remainder when dividing by 2.

If the remainder is 0, the number is even; otherwise, it's odd.

Use if and else statements to decide what to print.
"""

"""
Problem 3: FizzBuzz Lite Goal: Loop through numbers 1 to 20, print special words for multiples of 3, 5, or both.

Use a for loop with range(1, 21) to get numbers from 1 to 20.

Use if statements and modulo % to check:

If divisible by 3 and 5 (both), print "FizzBuzz".

Else if divisible by 3, print "Fizz".

Else if divisible by 5, print "Buzz".

Else, print the number itself.

Remember the order of checking matters: check "both" first to avoid missing it.
"""
"""
Problem 4: List Sum Goal: Add all numbers in a list.

You already have a list, e.g., numbers = [2, 5, 8, 3, 1].

Create a variable to keep track of the total sum, starting at 0.

Use a for loop to go through each number in the list.

Add each number to the total sum.

After the loop, print the total sum.
"""
"""
Problem 10: Convert Temperature Goal: Convert Celsius to Fahrenheit.

Get Celsius from the user (convert input to float or int).

Apply the formula F = C * 9/5 + 32.

Print the Fahrenheit temperature.
"""






# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
name = input("What is your name? ")
# The input is the users response that it gives in the terminal
print(name + " is my friends name!")

print("\nTesting Problem 2:")
number = input("Give me a number, and I'll guess even or odd: ")
number = int(number)
    # This converts string to integer so code works, AI helped me with this
if(number % 2 == 0):
    print("Even")
else:
    print("Odd!") 

print("Testing Problem 3:")
numero = int(input("Give me a big number: "))
# Asks for a number, so I can test this multiple times by running program

def numbers(numero):
    for each in range(1, numero + 1):
        if each % 3 == 0 and each % 5 == 0:
            # if the index's remainder of 3 AND 5 equals 0
            print(str(each) + ": Fizzbuzz")
        elif each % 3 == 0:
            # elif is equal to else if
            print(str(each) + ": Fizz")
        elif each % 5 ==0:
            print(str(each) + ": Buzz")
        else:
            print(str(each) + ": None")

numbers(numero)

print("Testing Problem 4:")

def sum_list(list):
    answer = 0
    for each in list:
        answer = answer + each
        # I could do answer += each, but this is easier for me to learn

    print(answer)

sum_list([1, 2, 3, 4, 5])
sum_list([1, 2, 3])
sum_list([1, 2, 3, 10, 23])

print("\nTesting Problem 5:")

def temperature(celsius):
    fahrenheit = 0
    fahrenheit = celsius * 9/5 + 32
    # This is the formula to convert celsius to fahrenheit
    print (fahrenheit)

temperature(32)
temperature(29)
temperature(60)