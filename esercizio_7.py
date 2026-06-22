#
# File: esercizio_6.py
#
# Author: D.Cicogna
#
# Date: 22/06/2026
#
# Version: 1.0
#
# Description: Creare un programma per giocare con le tabelline.
#
#Il programma deve:
#
#contenere un generatore che, dato un numero (ad esempio 7), generi la tabellina corrispondente al numero selezionato (0x7 = 0; 1x7 = 7; 2x7 = 14; ecc…);
#
#contenere un loop che chieda in modo interrattivo all’utente di indovinare il valore corrente nella tabellina selezionata;
#
#gestire tutti i caratteri alfanumerici (non deve “rompersi” se l’utente sceglie una lettera);
#
#gestire caretteri speciali o numeri decimali;
#
#gestire la chiusura del gioco in modo personalizzato.
#

def generatore(numero):
    x = 0
    while True:
        yield x*numero
        x = x+1

numero_corretto = True
while numero_corretto:
    ctrl = True
    n = input("Ciao!!! facciamo un gioco, dammi un numero intero e prova ad indovinare la tabellina, se indovini prendi tu il punto, sennò lo prendo io (considera che la tabellina deve essere completa): ")
    try:
        n = int(n)
    except ValueError:
        print ("numero non corretto, riprovare")
        ctrl = False
    if ctrl:
        numero_corretto = False

controllo = True
punteggio_m = 0
punteggio_u = 0
controllo_numero = True
prodotto = generatore(n)
valore_corretto = next(prodotto)
while controllo:
        
    if controllo_numero:
        numero_corretto = True
        while numero_corretto:
            ctrl = True
            n_input = input("A che numero siamo arrivati? ")
            try:
                n_input = int(n_input)
            except ValueError:
                print ("numero non corretto, riprovare")
                ctrl = False
            if ctrl:
                numero_corretto = False
        if n_input == valore_corretto:
            punteggio_u +=1
            print("Bingo, hai indovinato!!!")
        else:
            print("Mi dispiace, ti sei confuso, il numero giusto era: " + str(valore_corretto))
            punteggio_m +=1
        print("Siamo " + str(punteggio_u) + " a " + str(punteggio_m))
    else:
        print("Mi dispiace, valore non valido, riprovare")
    controllo_ciclo = True
    valore_corretto = next(prodotto)
    while controllo_ciclo:
        decisione = input("cosa vuoi fare adesso??? (0: finisco il gioco, 1: continuo a giocare): ")
        if decisione == "0":
            if punteggio_u >= punteggio_m:
                print("è stato bello giocare con te, torna pure a trovarmi, cosi ci sfidiamo ancora con i numeri e questa volta vincerò!!! :)")
            else:
                print("è stato bello giocare con te, torna pure a trovarmi, cosi questa volta riuscirai a battermi, forse")
            controllo_ciclo = False
            controllo = False
        elif decisione == "1":
            print("BENE, continuiamo, che ho voglia di vincere")
            controllo_ciclo = False
        else:
            print("comando non valido, riprovare")
if punteggio_u == 0:
    print("mi raccomando, ripassa bene le tabelline per la prossima volta, non è divertente vincere così ;)")    