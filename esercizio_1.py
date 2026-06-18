#
# File: esercizio_1.py
#
# Author: D. Cicogna
#
# Date: 2026/18/06
#
# Version: 1.0
#
# Description: scrivete una funzione di controllo, is_pari(n), 
#che accetti come parametro un numero intero e restituisca True se il numero è pari, False altrimenti.
#
#Create una funzione di generazione che chieda all’utente un numero intero positivo e lo restituisca 
#come risultato della funzione. Se l’utente inserisce un numero non valido (es. negativo o zero), 
#il ciclo deve continuare a richiederlo finché l’input non è corretto.
#
#Scrivete una funzione che usando il numero scelto dall’utente,
# generi una lista seguendo questa regola: se il numero è pari,
# va diviso per 2; se è dispari, va moltiplicato per 3 e aggiunto 1. 
#Il processo va ripetuto finchè si arriva a 1 o la lista abbia piu’ di 100 numeri
#
#Scrivete una funzione analizza_sequenza(lista) che riceva la lista generata e restituisca tre valori:
# il valore massimo raggiunto, la lunghezza della sequenza e la somma di tutti i numeri.
#
#Scrivete una funzione ricerca(lista) che scorra la lista e stampi solo i numeri della sequenza che sono divisibili
# per 5. Se non ce ne sono, va stampato un messaggio dedicato.
#
#Unite il tutto in un main program che chieda all’inizio all’utente quanti numeri vuole testare.
# Usate uno o più loop per chiedere all’utente i numeri da analizzare e per eseguire i punti precedenti 
#per ogni numero. Alla fine stampate un riepilogo che mostri quale numero iniziale ha generato la sequenza più lunga.
#

def is_pari (n):                                #creo la funzione per vedere se un numero è pari
    '''Vedo se un numero è pari o dispari'''    
    if n%2 == 0 :                               #verifico se il numero è pari   
        return True
    else :
        return False

def return_valore ():                                #creo la funzione per chiedere un numero alla persona
    '''Chiedo all'utente un numero positivo'''       
    a = True
    while a:                                         #verifico se il numero che ottengo è positivo, sennò richiedo il numero
        b = input('scrivi un numero positivo: ')
        b = int (b)
        if b > 0:
            a = False                                
    return b                                        #mi faccio ritornare come soluzione il numero che ho ottenuto

def lista_valore_pr (controllo_valore):             # creo la funzione per creare una lista dal valore iniziare
    '''creo una lista in base al numero precedente'''
    a = controllo_valore
    a = int (a)
    b = 0
    valoritr = []
    while a > 1 and b < 100 :                       # creo un ciclo per inserire i valori della lista
        if is_pari (a):                             # verifico se il numero è pari
            a = a//2
        else :
            a = a*3 +1
        valoritr.append(a)                          # inserisco il numero nella lista
        b += 1
    return valoritr                                 # mi faccio ritornare la lista

def analizza_sequenza (lista) :                     # creo una funzione per verificare diversi dettagli della lista
    '''Vedo qual'è il valore maggiore, la somma e la lunghezza della lista'''
    massimo = 0
    somma = 0
    controllo = 0
    lunghezza = len (lista)                         # vedo la lunghezza della lista
    while controllo < lunghezza:                    # uso un ciclo per vedere qual'è il valore massimo, e poi me lo salvo, svolgendo nel frattempo anche 
        valorel = lista [controllo]                 # la somma
        if valorel > massimo:
            massimo = valorel
        somma = somma + valorel
        controllo += 1
    return massimo, somma, lunghezza            

def ricerca_divisibili_5 (lista):                   # creo una funzione per vedere quanti elementi di questa lista sono divisibili per cinque
    '''ricerco e trascrivo i numeri divisibili per 5'''
    length = len (lista)
    control = 0
    ndivisibili = 0
    print ('i numeri divisibili per 5 sono: ')
    while control < length:                        # uso nuovamente un ciclo per verificare i valori
        valorel = lista [control]
        if valorel % 5 == 0:
            print (valorel)
            ndivisibili += 1
        control+=1
    if ndivisibili == 0:
        print('non erano presenti numeri divisibili per 5')

numero_da_analizzare = input ('quanti numeri vuoi analizzare? ')        #chiedo all'utente di inserire un numero
numero_da_analizzare = int (numero_da_analizzare)                       #lo rendo int

for i in range (numero_da_analizzare):            # creo un ciclo per svolgere quanto richiesto per tutti i numeri che l'untente inserisce
    numero_controllo = return_valore ()
    numero_controllo = int (numero_controllo)
    print (is_pari (numero_controllo))
    sequenza = lista_valore_pr (numero_controllo)
    print ('I sequenti numeri rappresentano il massimo, la somma e la lunghezza della lista') 
    print (analizza_sequenza (sequenza))
    ricerca_divisibili_5 (sequenza)
