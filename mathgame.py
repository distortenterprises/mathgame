import os
import time
import sys
from random import randint
import random


answer = 0
name = str()
tries = 0
size = (10)
ops = ["+","-","*","/"]
count = 0
highScore = 0
highScoreName = str()
tryAgain = True


while tryAgain == True:
    try:
        os.system('say "{0}"'.format("Lets play a game!"))
        time.sleep(1)
        os.system('say "{0}"'.format("Whats your name?"))
        name = raw_input("Whats your name?: ")
        #print(str(name))
        os.system('say "{0}"'.format("Hi" + " " + name))
        time.sleep(1)
        os.system('say "{0}"'.format("I am going to ask you" + (str(size)) + " " + "Questions"))
        time.sleep(1)


    except:
        message = "broken"
        os.system('say "{0}"'.format(message + " " + "test"))
        time.sleep(1)

        sys.exit('operation completed')


    for i in range(0,size):

        try:
            operation = random.choice(ops)
            rando1 = randint(0,10)
            rando2 = randint(0,10)
            random1 = (str(rando1))
            random2 = (str(rando2))
            sum = eval(random1 + operation + random2)
            print(operation)
            tries = tries + 1
            message = (random1 + operation + random2 + "= ")
            os.system('say "{0}"'.format(message))
            time.sleep(1)
            os.system('say "{0}"'.format("What is it?"))
            #print(random)
            answer = raw_input("Whats the answer?: ")


        except:
            message = "broken"
            os.system('say "{0}"'.format(message + " " + "test"))
            time.sleep(1)

            sys.exit('operation completed')

        if (int(answer)) >= 700:
            message = "I said between 1 & 6!"
            os.system('say "{0}"'.format(message))
            time.sleep(1)
            os.system('say "{0}"'.format("You choose" + (str(answer))) + "are you stupid?")
            time.sleep(1)
            os.system('say "{0}"'.format("You wasted a turn, Try again"))

        elif (int(answer)) == (int(sum)):
            message = "correct, you rule!"
            os.system('say "{0}"'.format(message))
            time.sleep(1)
            os.system('say "{0}"'.format("The answer is" + (str(sum))))
            time.sleep(1)
            os.system('say "{0}"'.format("Well done!"))


        else:
            count = count + 1
            message = "wrong"
            os.system('say "{0}"'.format(message))
            time.sleep(1)
            os.system('say "{0}"'.format("The answer was" + (str(sum))))
            time.sleep(1)
            print("count =" + (str(count)))


    time.sleep(1)
    score = (size - count)
    os.system('say "{0}"'.format("You scored" + (str(score))))
    time.sleep(1)
    if score > highScore:
        highScore = score
        highScoreName = name
    else:
        pass
    os.system('say "{0}"'.format("The high score is" + (str(highScore))))
    time.sleep(1)
    os.system('say "{0}"'.format("Would you like to play again?" ))
    again = raw_input("Yes or No: ")
    if again == (str("Yes")):
            tryAgain = True
            os.system('say "{0}"'.format(highScoreName + "is the current champ with a high score of " + (str(highScore))))
            time.sleep(1)
    else:
            tryAgain = False


