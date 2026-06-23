#
# File: esercizio_8_EAFP.py
#
# Author: D.Cicogna
#
# Date: 23/06/2026
#
# Version: 1.0
#
# Description: Scrivete un programma per “il gioco dell’impiccato” in cui:
#
#leggete una lista di parole da un file JSON
#
#scegliete una parola a caso con cui giocare dalla lista letta, tramite random
#
#chiedete continuamente all’utente di inserire una lettera o di indovinare la parola, fino al termine del gioco in cui si esauriscono i tentativi o si indovina la parola
#
#La rappresentazione grafica del gioco è libera, così come il numero dei “tentativi” disponibili.
#
#1- Scrivete il programma con un approccio totalmente LBYL
#2- RI-scrivete il programma con un approccio totalmente EAFP
#

import json
import random
import string               #libreria che contiene costanti utili legate alle stringhe

with open("esercizio_8_parole.json", "r") as in_file:
    parole = json.load(in_file)

parole = parole["parole"]
random_generator = random.Random()
random_generator.shuffle(parole)
parola_cercata = parole[0]
lettere_parole = list(parola_cercata)
lettere_nascoste = []
dizionario_lettere = dict()
for i in lettere_parole:
    try:
        dizionario_lettere[i] += 1
    except KeyError:
        dizionario_lettere[i] = 1

for i in range(len(lettere_parole)):
    try:
        a = i/i
        b = i/(i-len(lettere_parole)+1)
        lettere_nascoste.append("_")
    except ZeroDivisionError:
        lettere_nascoste.append(lettere_parole[i])
print("Buongiorno, questo è il gioco dell'impiccato  ")
controllo = 0
vite = 0
lettere_già_usate = dict()
while controllo != 1:
    print(" questa è la parola da cercare: " + str(lettere_nascoste))
    lettera_inserita = input("inserire una lettera: ")
    lettera_inserita = lettera_inserita.lower()
    try:
        lettere_già_usate[lettera_inserita] += 1
        print ("lettera già usata")
    except KeyError:
        try:
            lettera_inserita = int(lettera_inserita)
            print("i numeri non valgono")
        except ValueError:
            try:
                string.punctuation.index(lettera_inserita)              #controlla che non ci siano segni di punteggiatura
                print("non valgono i segni di punteggiatura")
            except ValueError:
                try:
                    controllo_più_lettere = lettera_inserita[1]
                    print("inserisci una sola lettera")
                except IndexError:
                    pass
    try:
        dizionario_lettere [lettera_inserita] += 1
        posizioni = [i for i, x in enumerate(lettere_parole) if x == lettera_inserita.lower()]      # mi estrae da un iterabile una coppia indice valore e dopo controllo quali vanno bene e quali no
        for i in posizioni:
            lettere_nascoste[i] = lettere_parole[i]
    except KeyError:
        vite +=1
        print("la lettera non c'è nella parola, adesso hai " + str(5-vite) + " vite")

    try:
        vite_conto = vite/(vite-5)
    except ZeroDivisionError:
        controllo = 1
        print("GAME OVER")

    try:
        "".join(lettere_nascoste).index("_")
    except ValueError:
        print("THERE IS A WINNER")
        controllo = 1
        
    lettere_già_usate[lettera_inserita] = 1