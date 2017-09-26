from gtts import gTTS
import os

mytext = str(input())

#set language to english
language = 'en'

#Speech to text
myobj = gTTS(text=mytext, lang=language, slow=False)

#save file
myobj.save("t2s.mp3")
 
