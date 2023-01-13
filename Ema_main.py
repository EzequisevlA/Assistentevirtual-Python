import pyttsx3
import speech_recognition
import pywhatkit
import requests
from bs4 import BeautifulSoup
from playsound import playsound
import pyautogui
import os
import selenium
import datetime
from multiprocessing import Process
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
from glob import glob




# configurações de  voz 
maquina = pyttsx3.init('sapi5')
voices = maquina.getProperty("voices")
maquina.setProperty("voice", voices[1].id)
maquina.setProperty("rate",490)

nome=[]

def diga(audio):#função para máquina falar
    maquina.say(audio)
    maquina.runAndWait()
def recebercomando():#maquina escuta o comando
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
if __name__ =="__main__":#estruturas de comando
   
    while True:
        query = recebercomando().lower()
        if "acorde" in query:
            
            class video(object):
             def __init__(self, path):
                self.path = path
             def play(self):
                from os import startfile
                startfile(self.path)
            class Movie_MP4(video):
                type="MP4"
            movie = Movie_MP4(r"C:\\Users\\qui12\\.vscode\\estudos\\estudos\\treino\\ia\\video (4).mp4")
            movie.play()
            
            
                
            
            from greatme import greatme
            greatme()
            
            
            while True:
                query = recebercomando().lower()
                if "dormir" in query:
                    diga(f"tudo bem {nome}! pode me chamar sempre que quiser")
                    break
                elif 'olá' in query:
                        diga("Olá, tudo bem??")
                elif 'estou bem' in query:
                    diga("Que ótimo")
                elif 'como está você' in query:
                    diga("Estou bem!")
                elif 'está bem' in query:
                    diga("Estou sim!")
                elif 'obrigado' in query:
                    diga("Disponha")
                elif 'google' in query:
                    from searchnow import searchgoogle
                    searchgoogle(query)
                elif 'youtube' in query: # comando para reproduzir video no youtube
                    tocar = query.replace('youtube', " ")
                    tocar = query.replace('pesquise', " ")
                    tocar = query.replace('tocar', " ")
                    resultado = pywhatkit.playonyt(tocar)
                    maquina.say('tocando' + tocar)
                    maquina.runAndWait()
                
                        
                    

                elif 'wikipedia' in query:# comando Wikipedia
                    from searchnow import searchwikipedia
                    searchwikipedia(query)
                elif 'clima' in query:# comando de clima
                    procura = "clima"
                    url = f"https://www.google.com/search?q={procura}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    diga(f" {temp}")
                elif 'temperatura' in query:
                    procura = "clima"# comando de clima
                    url = f"https://www.google.com/search?q={procura}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    diga(f" {temp}")
                elif 'meu nome é' in query:#comando para cadastrar nome em desenvolvimento...
                    nome = query.replace('meu nome é' , " ")

                    diga(f"Olá {nome}")
                    diga('tudo bem?')
               
                elif 'desligar sistema' in query:
                    diga('encerrando protocolos e desligando o sistema')
                    diga(f'Até mais{nome}!')
                    exit()
                elif 'deezer' in query:
                    musica = musica.replace('deezer', '')
                    resultado = playsound("https://www.deezer.com/search/{musica}")
                elif 'pause' in query: #pausa o video aberto na aba ativa
                   pyautogui.press('k')
                   diga('video pausado')
                elif 'play' in query: #despausa o video aberto na aba ativa
                    pyautogui.press('k')
                    diga('video despausado')
                elif 'mutar' in query:#muta o video aberto na aba ativa
                    pyautogui.press('m')
                    diga('video mutado')
                elif 'fechar aba' in query:#fecha a aba ativa
                    with pyautogui.hold('Ctrl'):
                        pyautogui.press('w')
                        diga(f'aba fechada{nome}')
                elif 'abrir aba' in query:
                    with pyautogui.hold('ctrl'):
                        pyautogui.press('t')
                        diga(f'aba aberta{nome}')
                elif 'desligar o computador' in query:
                    if(os.name =="nt"):
                        diga('desligando o computador')
                        os.system("shutdown /s /t 1")
                    else:
                        os.system("shutdown -h now")
                elif 'horas' in query:
                  horas = datetime.datetime.now().hour 
                  minutos = datetime.datetime.now().minute 
                  
                  diga(f'agora são exatamente {horas} horas')
                  if minutos !=0:
                    diga(f'e {minutos} minutos!')
                  else:
                    diga('')
                elif 'abrir navegador' in query:
                    pyautogui.press('win')
                    pyautogui.press('g')
                    pyautogui.press('o')
                    pyautogui.press('o')
                    pyautogui.press('g')
                    pyautogui.press('l')
                    pyautogui.press('e')
                    pyautogui.press('enter')
                    diga('navegador aberto')
                elif 'criar alarme' in query:
                    diga('tudo bem, que hora gostaria que o chamasse?')
                elif 'que dia é hoje' in query:
                    dia = datetime.datetime.now().day
                    mes = datetime.datetime.now().month
                    ano = datetime.datetime.now().year
                    diga(f'Hoje é {dia} do {mes} de {ano}')
                    
                

                    