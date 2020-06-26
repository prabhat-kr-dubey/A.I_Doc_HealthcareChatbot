
import random

import wikipedia

GREETING_INPUTS = ("what can you do","hello", "hi", "greetings", "sup", "what's up", "hey",'hi there!',
              'hi!',
              'how do you do?',
              'how are you?',
              'i\'m cool.',
              'fine, you?',
              'always cool.',
              'i\'m ok',
              'glad to hear that.',
              'i\'m fine',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.',
              'what\'s your name?',
              'i\'m Dia. ask me a math question, please.')
GREETING_RESPONSES = ["I am personal Consultant Doctor. If you want to Consult type 'consult'.",
                      "I can also answer your quries about Diseases. type the Diseases name for Information."
                      ,"hi", "hey", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
def response(user_response):
        print(wikipedia.summary(user_response))      


flag=True
print("My name is dia.")
print("I am personal Consultant Doctor. If you want to Consult type 'consult'.")
print("I can also answer your quries about Diseases. type the Diseases name for Information.")
print("If you want exit type 'bye'")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("You are welcome..")
        else:
            if(user_response=='consult'):
                exec(open(r"bot.py").read())
            else:
                if(greeting(user_response)!=None):
                      print(""+greeting(user_response))
                else:
                      print("",end="")
                      print(response(user_response))
                
    else:
        flag=False
        print("Bye! take care..")