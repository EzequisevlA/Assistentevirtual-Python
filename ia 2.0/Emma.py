import random
import json
import torch
from cerebro import neuralnet
from Neuralnetwork import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('comandos.json','r') as json_data:
    comandos = json.load(json_data)


FILE = "TreinoData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]


model = neuralnet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#---------------------------------------------------------------------------
Assistente = "Emma"
from ouça import ouvir
from Diga import diga
def Main():
    comando = ouvir()
    if comando =="tchau":
        exit()
    comando = tokenize(comando)
    X= bag_of_words(comando,all_words)
    X = X.reshape(1,X.shape[0])
    X= torch.from_numpy(X).to(device)


    output = model(X)
    __ , predicted = torch.max(output,dim=1) 
    tag = tags[predicted.item()]
    probs = torch.softmax(output,dim=1)
    probs = probs[0][predicted.item()]

    if probs.item() > 0.75:
        for comando in comandos['comando']:
            if tag == comando["tag"]:
                reply = random.choice(comando["responses"])
                diga(reply)
Main()