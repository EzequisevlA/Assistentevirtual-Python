import pyttsx3
import datetime
maquina = pyttsx3.init('sapi5')
voices = maquina.getProperty("voices")
maquina.setProperty("voice", voices[0].id)
maquina.setProperty("rate",170)
nome = []

def diga(audio):
    maquina.say(audio)
    maquina.runAndWait()
def greatme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12:
        diga(f"Bom dia {nome}!")
    elif hour >12 and hour <=18:
        diga(f"Boa tarde{nome}!")
    else: diga(f"Boa noite{nome}")
    diga("como posso ajudar??")
