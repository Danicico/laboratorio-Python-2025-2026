#
# File: esercizio_8_LBYL.py
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

with open("esercizio_8_parole.json", "r") as in_file:
    parole = json.load(in_file)

parole = parole["parole"]
random_generator = random.Random()
random_generator.shuffle(parole)
parola_cercata = parole[0]
lettere_parole = list(parola_cercata)
lettere_nascoste = []
for i in range(len(lettere_parole)):
    if i == 0 or i == len(lettere_parole)-1:
        lettere_nascoste.append(lettere_parole[i])
    else:
        lettere_nascoste.append("_")
controllo_parola = True
while controllo_parola:
    controllo = input("Buongiorno, ti va di giocare all'impiccato? se si prema 1, altrimenti un qualsiasi altro numero positivo(hai 5 vite): ")
    if not controllo.isdigit():
        print("seguire le istruzioni dette prima")
    else:
        controllo_parola = False
vite = 0
lettere_già_usate = set()
while int(controllo) == 1:
    print("bene, questa è la parola da cercare: " + str(lettere_nascoste))
    lettera_inserita = input("inserire una lettera: ")
    if lettera_inserita.lower() in lettere_già_usate:
        print("la lettera è già stata inserita")
    elif lettera_inserita.isalpha() and len(lettera_inserita) == 1:
        if lettera_inserita.lower() in lettere_parole:
            posizioni = [i for i, x in enumerate(lettere_parole) if x == lettera_inserita.lower()]      # mi estrae da un iterabile una coppia indice valore e dopo controllo quali vanno bene e quali no
            for i in posizioni:
                lettere_nascoste[i] = lettere_parole[i]
        else:
            vite +=1
            print("la lettera non c'è nella parola, adesso hai " + str(5-vite) + " vite")
        if "_" not in lettere_nascoste:
            controllo = 0
            print("THERE IS A WINNER")
        if vite == 5:
            print("GAME OVER")
            controllo = 0
        lettere_già_usate.add(lettera_inserita.lower())
    else:
        print("carattere non valido")
