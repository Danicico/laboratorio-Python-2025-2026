#
# File: esercizio_5.py
#
# Author: D. Cicogna
#
# Date: 22/06/2026
#
# Version: 1.0
#
# Description: Trovate 10 soluzioni per il gioco delle regine con il metodo delle permutazioni: 
#quanto è il tempo medio necessario a trovare una soluzione?
#
#Contate quanti tentativi fa il programma per trovare ogni soluzione del problema 8 regine
#
#Alcune soluzioni possono essere ripetute: fate in modo che le soluzioni siano “uniche”
#
#Se ci sono soluzioni ripetute, contate quante volte ogni soluzione è ripetuta
#
#Generalizzate il programma per risolvere una scacchiera di qualunque dimensione NxN
#
#Trovate quale è la scacchiera con lato N più grande possibile per cui si riesce a trovare 1 soluzione in meno di 15s
#
#Ogni soluzione è ‘simmetrica’ per rotazioni della scacchiera 8x8 di 90, 180 e 270 gradi. Scrivete delle funzioni che, 
#una volta trovata una soluzione alla scacchiera, costruiscano le 4 soluzioni simmetriche per rotazione. 
#Trovate 5 soluzioni “uniche” e le rispettive soluzioni simmetriche per rotazione per una scacchiera 8x8
#
import random
import time

def stessa_diagonale(x0, y0, x1, y1):
    '''Ritorna Vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa "diagonale"
    '''
    # distanza lungo y
    dy = abs(y1 - y0)
    
    # distanza lungo x
    dx = abs(x1 - x0) 

    # se dx == dy , dx/dy == 1 e sono sulla stessa diagonale, boolean expression
    return dx == dy     


def incrocia_colonne(posizioni, col):
    '''Ritorna Vero se la colonna 'col', che indica la posizione della regina
      (col, posizioni[col]) incrocia la diagonale di qualcuna 
      delle posizioni delle regine precedenti 
    '''
    # controllo tutte le precedenti fino a questa 'col'
    for c in range(col):     
        # la coordinata X (la riga) è indice (c) 
        # la coordinata Y,(la colonna) è valore lista nell'indice (c)
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            # stop se trovo problemi
            return True  
    # nessun incrocio, la posizione va bene e NON incrocia altre colonne        
    return False   


def soluzione_ok(soluzione_posizioni):
    '''Controlla tutte le posizioni della possibile soluzione
       'soluzione_posizioni' per verificare se ognuna delle posizioni 
       (colonne dela permatazione) ogni colonna incrocia la diagonale
       di qualche altra posizione
    '''

    for col in range(1, len(soluzione_posizioni)):
        # verifica se incrocia
        #if incrocia_colonne(soluzione_posizioni, col) == True:
        if incrocia_colonne(soluzione_posizioni, col):
            # stop se trova incroci, la soluzione non è valida
            return False 

    # Se non è ritornato prima, 
    # allora nessun incrocio trvato: posizioni della soluzione valide 
    return True

def rotazione_90(soluzione_posizioni, dim):
    """creo la soluzione ruotata di 90 gradi rispetto alla soluzione data"""
    lista_90 = []
    for i in range(dim):
        lista_90.append(0)
    for c in range(dim):
        lista_90[soluzione_posizioni[c]] = (dim - 1)-c
    return lista_90 

def rotazione_180(soluzione_posizioni, dim):
    """creo la soluzione ruotata di 180 gradi rispetto alla soluzione data"""
    lista_180 = []
    for i in range(dim):
        lista_180.append(0)
    for c in range(dim):
        lista_180[(dim - 1)-c]= (dim - 1)-soluzione_posizioni[c]
    return lista_180

def rotazione_270(soluzione_posizioni, dim):
    """creo la soluzione ruotata di 270 gradi rispetto alla soluzione data"""
    lista_t_90 = rotazione_90(soluzione_posizioni, dim)
    lista_270 = rotazione_180(lista_t_90, dim)
    return lista_270 

def main():
    # inizializzo generatore permutazioni
    random_generator = random.Random() 

    n = input('scrivi la grandezza della tabella: ')
    
    # preparo la "possibile soluzione" con posizoni da testare
    scacchiera = list(range(int(n))) 
    
    # conto le soluzioni trovate, inizio da 0           
    solutions = 0                 
    
    # misuro il tempo di partenza per la ricerca della soluzione
    start_time = time.time() 

    lista_tempo = []

    lista_combinazioni = []  

    numero_tentativi = 0

    dizionario_ripetizioni = dict()
    
    # loop finchè non trovo una soluzione
    if int(n) >=4:
        while solutions < 1:

            controllo = True 
            lista_rotazioni = []
            # permutazione casuale della soluzione 'mescolando' posizioni

            random_generator.shuffle(scacchiera)
            corretto = str(scacchiera)
            if corretto in dizionario_ripetizioni:          #verifico se la soluzione era già comparsa e quante volte
                dizionario_ripetizioni[corretto] += 1
            if corretto not in dizionario_ripetizioni and soluzione_ok(scacchiera):     #sennò la inserisco nel dizionario delle soluzioni già comparse
                dizionario_ripetizioni[corretto] = 1
            numero_tentativi+=1

            # verifica se la permutazione casuale e' soluzione  
            #if soluzione_ok(scacchiera) == True:

            for i in lista_combinazioni:
                if scacchiera == list(i):
                    controllo = False
            if soluzione_ok(scacchiera) and controllo: 
                # se la soluzione è buona, scrive
                print(f'Found solution {scacchiera} in {time.time() - start_time} s.')
                tempo = time.time() - start_time
                lista_rotazioni.append(rotazione_90(scacchiera, int(n)))
                lista_rotazioni.append(rotazione_180(scacchiera, int(n)))
                lista_rotazioni.append(rotazione_270(scacchiera, int(n)))
            
                # incremento contatore soluzioni trovate (condizione stop loop)
                if controllo:
                    solutions += 1      
                lista_tempo.append (tempo)
                scacchiera_1 = tuple(scacchiera)
                lista_combinazioni.append(scacchiera_1)
                # reset timer ricerca soluzione
                start_time = time.time()
                print("tempo medio = " + str(sum(lista_tempo)/solutions))
                print("il numero di tentativi per trovare " + str(solutions) + " soluzioni è circa: " + str(numero_tentativi))
                numero_tentativi = 0
        print (dizionario_ripetizioni)
        print(lista_rotazioni)
    else:
        print ('numero di righe non valido')
    while control:
        random_generator.shuffle(list(range(int(control_numero))))
        if soluzione_ok(scacchiera) and controllo: 
            tempo = time.time() - tempo_inizio
        if tempo>15:
            control = False
        else:
            control_numero+=1
    print ("la dimensione minima è " + str(control_numero))



# chiamo la funzione principale 
main()
