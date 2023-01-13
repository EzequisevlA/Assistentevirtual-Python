import speech_recognition as sr

def ouvir():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ouvindo...")
        r.pause_threshold = 1 
        audio = r.listen(source, 0,2)
    try:
        print("Entendendo...")
        comando = r.recognize_google(audio , language='pt-br')
        print(f'você disse {comando}')
    except:
        return""
    comando = str(comando)
    return comando.lower()
ouvir()