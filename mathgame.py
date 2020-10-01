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
        print("Let's play a game : ")
        time.sleep(1)
        
        name = input("Whats your name : ")
        #print(str(name))
        print("Hello " +name+ " :")
        time.sleep(1)
        print("I am going to ask you " + (str(size)) + " " + "Questions")
        time.sleep(1)


    except:
        message = "broken"
        os.system('say "{0}"'.format(message + " " + "test"))
        time.sleep(1)

        


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
            print("What is it ? ")
            #print(random)
            answer = input("Whats the answer?: ")


        except:
            message = "broken"
            os.system('say "{0}"'.format(message + " " + "test"))
            time.sleep(1)

            

        if (int(answer)) >= 700:
            print("I said between 1 & 6!")
            
            time.sleep(1)
            print("You choose" + (str(answer) + "are you stupid?"))
            time.sleep(1)
            print("You wasted a turn, Try again")

        elif (int(answer)) == (int(sum)):
            print("correct, you rule!")
            os.system('say "{0}"'.format(message))
            time.sleep(1)
            print("The answer is" + (str(sum)))
            time.sleep(1)
            print('say "{0}"'.format("Well done!"))


        else:
            count = count + 1
            print("wrong")
           
            time.sleep(1)
            print("The answer was" + (str(sum)))
            time.sleep(1)
            print("count =" + (str(count)))


    time.sleep(1)
    score = (size - count)
    print("You scored" + (str(score)))
    time.sleep(1)
    if score > highScore:
        highScore = score
        highScoreName = name
    else:
        pass
    print("The high score is" + (str(highScore)))
    time.sleep(1)
    print("Would you like to play again?" )
    again = input("Yes or No: ")
    again2 = again.lower()
    if again == (str("yes")):
            tryAgain = True
            print(highScoreName + "is the current champ with a high score of " + (str(highScore)))
            time.sleep(1)
    else:
            tryAgain = False




