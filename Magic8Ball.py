#this code stimulates a magic 8 ball
#users asks a yes or no question

import time
import random

print("Welcome to the Magic 8 Ball! Ask a question and we would tell what your fortune is :-)")

# A dictionary of twenty possible replies and their indices
dictionary = {"IT IS CERTAIN.":1, "IT IS DECIDEDLY SO.":2, "WITHOUT A DOUBT.":3, 
"YES, DEFINITELY.":4, "YOU MAY RELY ON IT.":5, "AS I SEE IT, YES.":6, "MOST LIKELY.":7, "OUTLOOK GOOD":8, 
"YES.":9, "SIGNS POINT TO YES.":10, "REPLY HAZY, TRY AGAIN.":11, "ASK AGAIN LATER.":12, 
"BETTER NOT TELL YOU NOW.":13, "CANNOT PREDICT NOW.":14, "CONCENTRATE AND ASK AGAIN.":15, "DON'T COUNT ON IT.":16,
"MY REPLY IS NO.":17, "MY SOURCES SAY NO.":18, "OUTLOOK  NOT SO GOOD.":19, "VERY DOUBTFUL":20
}

reply = 'y'
while reply != 'quit':
    question = input("Enter a question: ")
    print('Thinking....')

    random_pick = random.randint(1, 20) #this picks a number between 1 and 20

    time.sleep(3) #this delays the output for 5 seconds

    print("Answer: ", list(dictionary.keys())[random_pick])
    reply = input('Ask another question or quit(enter y to ask, quit to end the program): ')
