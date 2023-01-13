import pyttsx3
def diga(Text):
    maquina = pyttsx3.init("sapi5")
    voices = maquina.getProperty('voices')
    maquina.setProperty('voices', voices[1].id)
    maquina.setProperty('rate',180)
    print(f"A.i : {Text}")
    maquina.say(text=Text)
    maquina.runAndWait()
    print("  ")
