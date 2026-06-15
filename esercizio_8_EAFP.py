import json
import random
import string

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
    try:
        lettere_già_usate[lettera_inserita] += 1
        print ("lettera già usata")
    except KeyError:
        try:
            lettera_inserita = int(lettera_inserita)
            print("i numeri non valgono")
        except ValueError:
            try:
                string.punctuation.index(lettera_inserita)
                print("non valgono i segni di punteggiatura")
            except ValueError:
                pass
    try:
        dizionario_lettere [lettera_inserita] += 1
        posizioni = [i for i, x in enumerate(lettere_parole) if x == lettera_inserita.lower()]
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
            

