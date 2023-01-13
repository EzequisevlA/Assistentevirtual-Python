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
        query = r.recognize_google(audio, language='pt-br')
        print(f"you said: {query}\n")
    except Exception as e: 
        print('Não entendi, diga novamente!')
        return "None"
    return query
query = recebercomando().lower()
maquina = pyttsx3.init('sapi5')
voices = maquina.getProperty("voices")
maquina.setProperty("voice", voices[0].id)
maquina.setProperty("rate",170)


def diga(audio):
    maquina.say(audio)
    maquina.runAndWait()
def searchgoogle(query):
    if 'google' in query:
        import wikipedia as googleScrap
        query=query.replace("google", " ")
        query=query.replace("procure", " ")
        query=query.replace("no", " ")
        diga("isso foi oque encontrei no google")
        wikipedia.set_lang('pt')
        pywhatkit.search(query)
       
       
def searchyoutube():
    if 'toque' in query:
        diga("Isso foi oque encontrei com oque me foi solicitado.")
        query = query.replace("youtube", " ")
        result = pywhatkit.playonyt(query)
        diga("Feito!" + result)
def searchwikipedia():
    if "wikipédia" in query:
        diga("Buscando na wikipedia....")
        query = query.replace("Wikipedia", " ")
        wikipedia.set_lang('pt')
        results = wikipedia.summary(query, sentences = 2)
        diga("isso foi oque encontrei com a busca mencionada no wikipedia")
        print(results)
        diga(results)