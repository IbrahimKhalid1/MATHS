import math

# Ask the question
user_answer = float(input("What is 68 + 1? Enter your answer: "))

# Calculate the correct answer
correct_answer = 68 + 1.5

# Check if the user's answer is correct
if user_answer == correct_answer:
    print("Great! Your answer is correct.")
else:
    print("You lost. The correct answer is:", correct_answer)