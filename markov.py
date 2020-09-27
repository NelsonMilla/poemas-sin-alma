import json
import io
from collections import defaultdict
import random

f = io.open("./pablo.json", mode="r", encoding="utf-8") #Abre el archivo JSON.
file = json.load(f)
palabras = []
for i in file:
    l = str(file[i]).split(" ")
    palabras.append(l)

almacen = defaultdict(lambda: list())

def add_word(prev,next):
    global almacen #Modifica una varibale afuera del scope.
    almacen[prev].append(next) #Buscamos la palabra anterior y le asignamos la siguiente.

def gen_word(): #Funcion que genera una cadena de palabras a partir del almacen.
    word = list()
    state = "START","START"
    while True:
        w = random.choice(almacen[state])#Elige una palabra al azar del almacen, enviandole el estado en el que se encuentra. # can fail
        word.append(w)
        state = state[1],w #Modifica el estado.
        if w.endswith(".") or w.endswith("!"): #Pone un espacio donde es necesario.
            return " ".join(word)

for frase in palabras: #Pobla el diccionario.
    frase = list(frase)
    for i,palabra in enumerate(frase):
        if i == 0:
            add_word(("START","START"),palabra)
            continue
        if i == 1:
            add_word(("START",frase[0]),palabra)
            continue
        add_word((frase[i-2],frase[i-1]),palabra)

for i in range(10):
    print(gen_word())
