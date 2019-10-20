## Speech Recognize send directly to google api

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("speak anything")
    audio = r.listen(source,timeout=3)

    try:
        text = r.recognize_google(audio)
        print( "You said,{}".format(text))
    except:
        print("Sorry not recognized")



## Speech is saved as wav format
import speech_recognition as sr

r= sr.Recognizer()

with sr.Microphone() as source:
    print("speak anything")
    audio = r.listen(source,timeout=3)

    with open('speech.wav','wb')as f:
        f.write(audio.get_wav_data())