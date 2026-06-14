import json
import random

dati = {"parole" : ["elicottero", "parallelepipedo", "trapezio"]}
with open ("esercizio_8_parole.json", "w") as write_file:
    json.dump(dati, write_file, indent = 4)

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
controllo = input("Buongiorno, ti va di giocare all'impiccato? se si prema 1, altrimenti 0, (hai 5 vite): ")
vite = 0
lettere_già_usate = set()
while controllo != 1:
    print("bene, questa è la parola da cercare: " + str(lettere_nascoste))
    lettera_inserita = input("inserire una lettera: ")
    if lettera_inserita.lower() in lettere_già_usate:
        print("la lettera è già stata inserita")
    elif lettera_inserita.isalpha():
        if lettera_inserita.lower() in lettere_parole:
            posizioni = [i for i, x in enumerate(lettere_parole) if x == lettera_inserita.lower()]
            for i in posizioni:
                lettere_nascoste[i] = lettere_parole[i]
        else:
            vite +=1
            print("la lettera non c'è nella parola, adesso hai " + str(5-vite) + " vite")
        if "_" not in lettere_nascoste:
            controllo = 1
            print("THERE IS A WINNER")
        if vite == 5:
            print("GAME OVER")
            controllo = 1
            lettere_già_usate.add(lettera_inserita.lower())
    else:
        print("carattere non valido")
