import random

def analisi_carte(mano, tavolo):
    carte = mano + tavolo
    dizionario_carte = dict()
    for i in range(len(carte)):
        try:
            dizionario_carte[carte[i][1]] += 1
        except KeyError:
            dizionario_carte[carte[i][1]] = 1
        try:
            dizionario_carte[carte[i][0]] += 1
        except KeyError:
            dizionario_carte[carte[i][0]] = 1
    return dizionario_carte
def vittoria(giocatore, avversario, valore_g, valore_a):
    if giocatore and avversario:
        if valore_g>valore_a:
            print("HAI VINTO!!!")
        else:
            print("hai perso")
    elif giocatore:
        print("HAI VINTO!!!")
    else:
        print("hai perso")
                
simboli = ["fiori", "picche", "quadri","cuori"]
valori = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
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
cosa_fare = input("Cosa vuoi fare (0: abbandonare la partita, 1: continuare ma non mettere soldi, 2: aumentare la posta in gioco, altri tasti: come tasto 1)? ")
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
print("\n Signore e signori, showdown: \n \n" + "LE TUE CARTE: \n \n" + str(carte_giocatore) + "\n \nCARTE DEL TAVOLO: \n \n " + str(carte_tavolo) + "\n \n CARTE AVVERSARIO: \n \n " + str(carte_avversario))
carte_tot_giocatore = analisi_carte(carte_giocatore, carte_tavolo)
carte_tot_avversario = analisi_carte(carte_avversario, carte_tavolo)
coppia_g = False
doppia_coppia_g = False
tris_g = False
colore_g = False
scala_g = False
poker_g = False
full_g = False
scala_colore_g = False
valore_coppia_g = []
valore_tris_g = []
valore_poker_g = 0
inizio_scala_g = 0
simbolo_scala_g = "Nessuno"
for i in simboli:
    if i in carte_tot_giocatore:
        if carte_tot_giocatore[i] >= 5:
            colore_g = True
            simbolo_scala_g = i
for i in valori:
    if i in carte_tot_giocatore:
        if carte_tot_giocatore[i] == 2 and coppia_g:
            coppia_g = False
            doppia_coppia_g = True
        if carte_tot_giocatore[i] == 2:
            coppia_g = True
            valore_coppia_g.append(i)
        elif carte_tot_giocatore[i] == 3:
            tris_g = True
            valore_tris_g.append(i)
        elif carte_tot_giocatore[i] == 4:
            poker = True
            valore_poker_g = i
        if str(int(i)+1) in carte_tot_giocatore:
            if str(int(i)+2) in carte_tot_giocatore:
                if str(int(i)+3) in carte_tot_giocatore:
                    if str(int(i)+4) in carte_tot_giocatore:
                        scala_g = True
                        inizio_scala_g = i
if (coppia_g or doppia_coppia_g) and tris_g:
    full_g = True
if scala_g and colore_g:
    scala_colore_g = True
coppia_a = False
doppia_coppia_a = False
tris_a = False
colore_a = False
scala_a = False
poker_a= False
valore_coppia_a = []
valore_tris_a = []
valore_poker_a = 0
inizio_scala_a = 0
simbolo_scala_a = "Nessuno"
for i in simboli:
    if i in carte_tot_avversario:
        if carte_tot_avversario[i] >= 5:
            colore_a = True
            simbolo_scala_a = i
for i in valori:
    if i in carte_tot_avversario:
        if carte_tot_avversario[i] == 2 and coppia_a:
            coppia_a = False
            doppia_coppia_a = True
        if carte_tot_avversario[i] == 2:
            coppia_a = True
            valore_coppia_a.append(i)
        elif carte_tot_avversario[i] == 3:
            tris_a = True
            valore_tris_a.append(i)
        elif carte_tot_avversario[i] == 4:
            poker_a = True
            valore_poker_a = i
        if str(int(i)+1) in carte_tot_avversario:
            if str(int(i)+2) in carte_tot_avversario:
                if str(int(i)+3) in carte_tot_avversario:
                    if str(int(i)+4) in carte_tot_avversario:
                        scala_a = True
                        inizio_scala_a = i
if (coppia_a or doppia_coppia_a) and tris_a:
    full_a = True
if scala_a and colore_a:
    scala_colore_a = True

if scala_colore_g or scala_colore_a:
    vittoria(scala_colore_g, scala_colore_a, inizio_scala_g, inizio_scala_a)
elif poker_g or poker_a:
    vittoria(poker_g, poker_a, valore_poker_g, valore_poker_a)
elif full_g or full_a:
    if full_g:
        
    vittoria(full_g, full_a,)



