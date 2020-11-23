# Problem 3: Magic 8-Ball
 # Simulate a magic 8-ball, allowing the user to enter their question.
 # Display an in progress message(i.e. "thinking").
 # Create responses and show a random response.
 # Allow the user to ask another question or quit.

# Original: 2 Sept 2019
# Edited: 24 November 2020

import random
import time

response = ["Very doubtful. \n",
            "Don't count on it. \n",
            "It's cute you think that there's a chance. \n",
            "The time travellers wouldn't want you to know that right now. \n",
            "Perhaps. \n",
            "Why do you think a computer program would know this?? \n",
            "Outlook good. \n",
            "Yes, definitely. \n",
            "Without a doubt. \n",
            "You may rely on it. \n"]

def reply():
    print("Divinating...")
    time.sleep(3)
    print(response[random.randint(0,9)])

first = True
while True:
    if first:
        input("Ask a question and I will answer. \n")
        reply()
        first = False
    else:
        query = input("Do you have another question? If so, ask. If not, enter 'exit'. \n")
        if query.lower() == "exit":
            print("You'll be back soon.")
            break
        else:
            reply()
