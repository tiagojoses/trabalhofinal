# coding: utf-8
import json as js
import numpy as np
import nltk
from nltk.stem.rslp import RSLPStemmer
import tflearn as tfl
import tensorflow as tf
import random
import speech_recognition as sr
from random import randint
from gtts import gTTS
from playsound import playsound
import funcoes

#Funcao responsavel por falar
def cria_audio(text):
  nome = str(randint(0,250))
  tts = gTTS(text,lang='pt-br')
  tts.save('audios/'+nome+'.mp3')
  playsound('audios/'+nome+'.mp3')


# Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        audio = microfone.listen(source)

    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
    except:
        cria_audio("Não entendi")

    return frase


with open("intents.json", encoding='utf-8') as file:
  data = js.load(file)

palavras = []
intencoes = []
sentencas = []
saidas = []

# pega intenção por intenção
for intent in data["intents"]:

  tag = intent['tag']
  print(intent['responses'])
  if tag not in intencoes:
     intencoes.append(tag)

  for pattern in intent["patterns"]:
    wrds = nltk.word_tokenize(pattern, language='portuguese')
    palavras.extend(wrds)
    sentencas.append(wrds)
    saidas.append(tag)

stemer = RSLPStemmer()
stemmed_words = [stemer.stem(w.lower()) for w in palavras]
stemmed_words = sorted(list(set(stemmed_words)))


training = []
output = []
# criando um array preenchido com 0
outputEmpty = [0 for _ in range(len(intencoes))]

for x, frase in enumerate(sentencas):
  bag = []
  wds = [stemer.stem(k.lower()) for k in frase]
  for w in stemmed_words:
    if w in wds:
      bag.append(1)
    else:
      bag.append(0)

  outputRow = outputEmpty[:]
  outputRow[intencoes.index(saidas[x])] = 1

  training.append(bag)
  output.append(outputRow)


training = np.array(training)
output = np.array(output)

# reiniciando os dados
tf.reset_default_graph()

# camada de entrada
net = tfl.input_data(shape=[None, len(training[0])])
# oito neuronios por camada oculta
net = tfl.fully_connected(net, 8)
# camada de saida
net = tfl.fully_connected(net, len(output[0]), activation="softmax")
#
net = tfl.regression(net)

# criando o modelo
model = tfl.DNN(net)

model.fit(training, output, n_epoch=500, batch_size=50, show_metric=True)
model.save("model.chatbot30G")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array(bag)

def chat():
    cont = False
    Online = True
    cria_audio("Bem vindo ao bot do corona virus,pergunte o que quer saber")

    while Online:
        try:
            resposta = 0
            if cont == True:
                cria_audio("O que mais deseja saber?")
            frase = ouvir_microfone()
            bag_usuario = bag_of_words(frase, stemmed_words)
            results = model.predict([bag_usuario])
            results_index = np.argmax(results)
            tag = intencoes[results_index]
            if tag == "dicas" or tag == "sintomas" or tag == "mortes" or tag == "pais-brasil" or tag == "mundo":
                if tag=="dicas":
                    dicas = str(funcoes.gerardicascorona(resposta))
                    cria_audio(dicas)
                if tag=="sintomas":
                    sintomas = str(funcoes.gerarsintomas(resposta))
                    cria_audio(sintomas)
                if tag=="pais-brasil":
                    casosbrasil = str(funcoes.gerarcasosbrasil(resposta))
                    cria_audio(casosbrasil)
                if tag=="mundo":
                    casosmundo = str(funcoes.gerarcasosmundo(resposta))
                    cria_audio(casosmundo)
                if tag == "mortes":
                    mortes = str(funcoes.gerarmortes(resposta))
                    cria_audio(mortes)
                cont = True
            else:
                for tg in data["intents"]:
                    if tg['tag'] == tag:
                        responses = tg['responses']
                        cont = True
                cria_audio(random.choice(responses))

            if tag == "ate-mais":
                Online = False
        except:
            print("erro! reiniciando")

chat()