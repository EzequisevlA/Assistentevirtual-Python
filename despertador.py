import datetime

agora = relogio()

def relogio():
    hora = datetime.datetime.now().hour
    minutos = datetime.datetime.now().minute
    agora = (f'{hora}:{minutos}')
    print(agora)
relogio()

def despertar():
    for(agora >=):