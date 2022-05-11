#Gets the random library so the answers
#can really be random
import random

print("========================")
print("|     Magic 8 Ball     |")
print("========================")

#Gets neccessary input
_name = input("Please enter your name: ")
_question = input("Ask your question: ")

#Stores the answer
_answer = ""

#Randomizer to get the answer
_randomNumber = random.randint(1, 9)

#Find the answer
if _randomNumber == 1:
    _answer = "Yes - definetely,"
elif _randomNumber == 2:
    _answer = "It is decidely so,"
elif _randomNumber == 3:
    _answer = "Without a doubt."
elif _randomNumber == 4:
    _answer = "Reply hazy, try again,"
elif _randomNumber == 5:
    _answer = "Ask again later."
elif _randomNumber == 6:
    _answer = "Better not tell you now."
elif _randomNumber == 7:
    _answer = "My sources say no."
elif _randomNumber == 8:
    _answer = "Outlook not so good."
elif _randomNumber == 9:
    _answer = "Very doubtful."
else:
    _answer = "8 ball broken"

#Answer

_output = ""

#Check if name is given
if _name == "":
    _name = "Someone has asked"

if _question == "":
    _question = "nothing"
    print("Please ask a question")
    print("========================")
else:
    _output = _name + " has asked " + _question + ".\nThe 8 ball's answer to that is: " + _answer
    print(_output)
    print("========================")
