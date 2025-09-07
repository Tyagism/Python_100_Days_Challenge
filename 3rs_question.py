import pyttsx3 as tts

# two methods of using text to speach in python

# 1st
engine = tts.init()
engine.say('hello world, this is your boi Harshit Tyagi')
engine.runAndWait()

# 2nd
tts.speak('hello world, this is your boi Harshit Tyagi but in a different way yet same :D')
