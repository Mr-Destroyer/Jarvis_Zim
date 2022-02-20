import pyttsx3

while True:
    
        friend = pyttsx3.init()
        speech = input("say something: ")
        friend.say(speech)
        friend.runAndWait()







