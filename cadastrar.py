import pyttsx3
import speech_recognition
import pywhatkit
import wikipedia
import webbrowser


def recebercomando():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('Ouvindo....')
        r.pause_threshold=1
        r.energy_threshold = 300
        audio = r.listen(source,0,4 )
    try:
        print('Entendendo...')
        guardar = r.recognize_google(audio, language='pt-br')
        print(f"you said: {guardar}\n")
    except Exception as e: 
        print('Não entendi, diga novamente!')
        return "None"
    return guardar
guardar = recebercomando().lower()
maquina = pyttsx3.init('sapi5')
voices = maquina.getProperty("voices")
maquina.setProperty("voice", voices[0].id)
maquina.setProperty("rate",170)
nome =[]

def diga(audio):
    maquina.say(audio)
    maquina.runAndWait()

def cadastrardados():
    nome = guardar
    diga(f"seu nome é  {nome} ?")

     

   
   