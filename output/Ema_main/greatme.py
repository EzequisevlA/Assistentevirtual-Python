import pyttsx3
import datetime
maquina = pyttsx3.init('sapi5')
voices = maquina.getProperty("voices")
maquina.setProperty("voice", voices[0].id)
maquina.setProperty("rate",170)


def diga(audio):
    maquina.say(audio)
    maquina.runAndWait()
def greatme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12:
        diga("Bom dia!")
    elif hour >12 and hour <=18:
        diga("Boa tarde!")
    else: diga("Boa noite")
    diga("como posso ajudar??")
