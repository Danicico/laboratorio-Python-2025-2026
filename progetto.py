import random
simboli = ["fiori", "picche", "quadri", "cuori"]
valori = ["A", "2", "3", "4", "5", "6", "7", "8", "9"]
random_generator = random.Random()
carte_giocatore = list()
carte_avversario = list()
carte_tavolo = list()
carte_mazzo = [[s, v] for s in simboli for v in valori]
random_generator.shuffle(carte_mazzo)
controllo = 0
while controllo<5:
    if controllo < 2:
        carte_giocatore.append(carte_mazzo.pop())
        carte_avversario.append(carte_mazzo.pop())
    carte_tavolo.append(carte_mazzo.pop())
    controllo += 1
budget = 1000
print ("ecco le sue carte, ha un budget iniziale di 1000 euro, usali bene: \n \n" + str(carte_giocatore) + "\n \n")
print("CARTE DEL TAVOLO: \n \n " + str(carte_tavolo[0:3]) )

controllo_gioco = 1
tavolo = 0
while controllo_gioco < 3:
    cosa_fare = input("Cosa vuoi fare (0: abbandonare la partita, 1: continuare ma non mettere soldi, 2: aumentare la posta in gioco, altri tasti: come tasto 1)? ")
    if cosa_fare != "0":
        if cosa_fare == "2" and budget > 0:
            aumento = input("di quanto rialzi? ")
            if int(aumento) < budget:
                budget = budget - int(aumento)
                print("adesso il tuo budget è di " + str(budget) + " euro")
            else:
                aumento = budget
                print("allora vai all in")
                budget = 0
            tavolo = tavolo + int(aumento)
            print("l'importo totale è adesso di: " + str(tavolo*2))
        elif budget == 0:
            print("sei già all in")
        if cosa_fare != "0":
            print("LE TUE CARTE: \n \n" + str(carte_giocatore))
            print("CARTE DEL TAVOLO : \n \n " + str(carte_tavolo[0:controllo_gioco+3]))
        controllo_gioco +=1
    else:
        print("CARTE DEL TAVOLO: \n \n " + str(carte_tavolo))
        controllo_gioco = 5
print("Signore e signori, showdown: \n \n" + "LE TUE CARTE: \n \n" + str(carte_giocatore) + "\n \nCARTE DEL TAVOLO: \n \n " + str(carte_tavolo) + "\n \n CARTE AVVERSARIO: \n \n " + str(carte_avversario))