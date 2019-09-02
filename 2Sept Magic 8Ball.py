# Magic 8-Ball
# 2 Sept 2019

import random
import time

response = ["Very doubtful. \n",
            "Don't count on it. \n",
            "It's cute you think that there's a chance. \n",
            "The time travellers wouldn't want you to know that right now. \n",
            "Maybe?? \n",
            "Why do you think a computer program would know this?? \n",
            "Outlook good. \n",
            "Yes, definitely. \n",
            "Without a doubt. \n",
            "You may rely on it. \n"]
def reply():
    print("Divinating...")
    time.sleep(3)
    print(response[random.randint(0,9)])

divinating = True
first = True
while divinating == True:
    if first:
        input("Ask a question and I will answer. \n")
        reply()
        first = False
    else:
        query = input("Do you have another question? If so, ask. If not, enter 'exit'. \n")
        if query.lower() == "exit":
            divinating = False
            print("Very well, good-bye.")
        else:
            reply()
