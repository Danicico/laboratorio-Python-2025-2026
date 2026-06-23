#
# File: Progetto.py
#
# Author: D.Cicogna
#
# Date: 23/06/2026
#
# Version: 1.0
#
# Description: Programma per giocare a poker texas hold'em contro un singolo avversario, ma senza che lui risponda (come se fosse un bot di allenamento)
#
import random
budget = 1000
def analisi_carte(mano, tavolo):
    """creo un dizionario con tutti i numeri e i simboli"""
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

def vittoria(giocatore, avversario, valore_g, valore_a, budget, soldi):
    """creo un programma base per vedere chi è il vincitore"""
    if giocatore and avversario:
        if valore_g>=valore_a:
            print("HAI VINTO!!!")
            budget = budget + int(soldi)*2
            print("il tuo budget è adesso di: " + str(budget))
        else:
            print("hai perso")
            print("il tuo budget è adesso di: " + str(budget))
    elif giocatore:
        print("HAI VINTO!!!")
        budget = budget + int(soldi)*2
        print("il tuo budget è adesso di: " + str(budget))
    else:
        print("hai perso")
        print("il tuo budget è adesso di: " + str(budget))
    return budget
            
simboli = ["fiori", "picche", "quadri","cuori"]
valori = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
random_generator = random.Random()
aumento = 0
gioco = "1"
while gioco == "1":
    carte_mazzo = [[s, v] for s in simboli for v in valori]         #uso una list comprehension per creare una lista di liste con tutte le carte a disposizione
    random_generator.shuffle(carte_mazzo)
    carte_giocatore = list()
    carte_avversario = list()
    carte_tavolo = list()
    controllo = 0
    while controllo<5:                                              #creo il tavolo e le carte del giocatore e dell'avversario
        if controllo < 2:
            carte_giocatore.append(carte_mazzo.pop())               #estraggo un elemento dalla lista carte mazzo, eliminandolo anche da quest'ultima
            carte_avversario.append(carte_mazzo.pop())
        carte_tavolo.append(carte_mazzo.pop())
        controllo += 1
    print ("ecco le sue carte, ha un budget iniziale di " + str(budget) + " euro, usali bene: \n \n" + str(carte_giocatore) + "\n \n")
    print("CARTE DEL TAVOLO: \n \n " + str(carte_tavolo[0:3]) )
    if int(carte_giocatore [0][1]) >= int(carte_giocatore [1][1]):
        carta_alta_g = int(carte_giocatore[0][1])
    else:
        carta_alta_g = int(carte_giocatore[1][1])
    if int(carte_avversario [0][1]) >= int(carte_avversario [1][1]):
        carta_alta_a = int(carte_avversario[0][1])
    else:
        carta_alta_a = int(carte_avversario[1][1])
    controllo_gioco = 1
    tavolo = 0
    while controllo_gioco < 3:                                  #faccio vedere le carte e scegliere all'utente cosa fare, e dopo mostro una nuova carta
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
    # controllo un'ultima volta cosa vuole fare l'utente
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
    #mostro tutte le carte e faccio l'analisi di chi a vinto
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
    valore_coppia_g = [0]
    valore_tris_g = [0]
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
                valore_coppia_g.append(int(i))
                if len(valore_coppia_g) > 2:
                    del valore_coppia_g[min(valore_coppia_g)] 
            elif carte_tot_giocatore[i] == 3:
                tris_g = True
                valore_tris_g.append(int(i))
            elif carte_tot_giocatore[i] == 4:
                poker_g = True
                valore_poker_g = i
            if str(int(i)+1) in carte_tot_giocatore:
                if str(int(i)+2) in carte_tot_giocatore:
                    if str(int(i)+3) in carte_tot_giocatore:
                        if str(int(i)+4) in carte_tot_giocatore:
                            scala_g = True
                            inizio_scala_g = int(i)
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
    scala_colore_a = False
    full_a = False
    valore_coppia_a = [0]
    valore_tris_a = [0]
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
                valore_coppia_a.append(int(i))
                if len(valore_coppia_a) > 2:
                    del valore_coppia_a[min(valore_coppia_a)] 
            elif carte_tot_avversario[i] == 3:
                tris_a = True
                valore_tris_a.append(int(i))
            elif carte_tot_avversario[i] == 4:
                poker_a = True
                valore_poker_a = int(i)
            if str(int(i)+1) in carte_tot_avversario:
                if str(int(i)+2) in carte_tot_avversario:
                    if str(int(i)+3) in carte_tot_avversario:
                        if str(int(i)+4) in carte_tot_avversario:
                            scala_a = True
                            inizio_scala_a = int(i)
    if (coppia_a or doppia_coppia_a) and tris_a:
        full_a = True
    if scala_a and colore_a:
        scala_colore_a = True

    if scala_colore_g or scala_colore_a:
        budget = vittoria(scala_colore_g, scala_colore_a, inizio_scala_g, inizio_scala_a, budget, tavolo)
    elif poker_g or poker_a:
        budget = vittoria(poker_g, poker_a, valore_poker_g, valore_poker_a, budget, tavolo)
    elif full_g or full_a:
        if max(valore_tris_g) != max(valore_tris_a):
            budget = vittoria(full_g, full_a, max(valore_tris_g), max(valore_tris_a), budget, tavolo)
        elif max(valore_coppia_g) != max(valore_coppia_a):
            budget = vittoria(full_g, full_a, max(valore_coppia_g), max(valore_coppia_a), budget, tavolo)
        elif carta_alta_a>carta_alta_g:
            print("hai perso")
            print("il tuo budget è adesso di: " + str(budget))
        else:
            print("HAI VINTO!!!")
            budget = budget + int(tavolo)*2
            print("il tuo budget è adesso di: " + str(budget))
    elif colore_g or colore_a:
        budget = vittoria(colore_g, colore_a, carta_alta_g, carta_alta_a, budget, tavolo)
    elif scala_g or scala_a:
        budget = vittoria(scala_g, scala_a, inizio_scala_g, inizio_scala_a, budget, tavolo)
    elif doppia_coppia_g or doppia_coppia_a:
        if len(valore_coppia_g) == len(valore_coppia_a):
            if max(valore_coppia_g) != max(valore_coppia_a):
                budget = vittoria(doppia_coppia_g, doppia_coppia_a, max(valore_coppia_g), max(valore_coppia_a), budget, tavolo)
            elif min(valore_coppia_g) != min(valore_coppia_a):
                budget = vittoria(doppia_coppia_g, doppia_coppia_a, min(valore_coppia_g), min(valore_coppia_a), budget, tavolo)
            else:
                budget = vittoria(doppia_coppia_g, doppia_coppia_a, carta_alta_g, carta_alta_a, budget, tavolo)
        else:
            if len(valore_coppia_a) == 1:
                print("HAI VINTO!!!")
                budget = budget +int(tavolo)*2
                print("il tuo budget è adesso di: " + str(budget))
                budget = budget + int(tavolo)*2
            elif len(valore_coppia_g) ==1:
                print("hai perso")
                print("il tuo budget è adesso di: " + str(budget))
    elif tris_g or tris_a:
        if max(valore_tris_g) != max(valore_tris_a):
            budget = vittoria(tris_g, tris_a, max(valore_tris_g), max(valore_tris_a), budget, tavolo)
        else:
            budget = vittoria(tris_g, tris_a, carta_alta_g, carta_alta_a, budget, tavolo)
    elif coppia_g or coppia_a:
        if max(valore_coppia_g) != max(valore_coppia_a):
            budget = vittoria(coppia_g, coppia_a, max(valore_coppia_g), max(valore_coppia_a), budget, tavolo)
        else:
            budget = vittoria(coppia_g, coppia_a, carta_alta_g, carta_alta_a, budget, tavolo)
    else:
        if carta_alta_g >= carta_alta_a:
            print("HAI VINTO!!!")
            budget = budget + int(tavolo)*2
            print("il tuo budget è adesso di: " + str(budget))
        else:
            print("hai perso")
            print("il tuo budget è adesso di: " + str(budget))
    gioco = input("vuoi fare un'altra mano (1 = sì , altro tasto = no)? ")
    