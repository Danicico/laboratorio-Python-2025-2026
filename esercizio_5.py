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
    lista_90 = []
    for i in range(dim):
        lista_90.append(0)
    for c in range(dim):
        lista_90[soluzione_posizioni[c]] = 7-c
    return lista_90

def rotazione_180(soluzione_posizioni, dim):
    lista_180 = []
    for i in range(dim):
        lista_180.append(0)
    for c in range(dim):
        lista_180[7-c]= 7-soluzione_posizioni[c]
    return lista_180

def rotazione_270(soluzione_posizioni, dim):
    lista_t_90 = rotazione_90(soluzione_posizioni, dim)
    lista_270 = rotazione_180(lista_t_90, dim)
    return lista_270



import random
import time 

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
            if corretto in dizionario_ripetizioni:
                dizionario_ripetizioni[corretto] += 1
            if corretto not in dizionario_ripetizioni and soluzione_ok(scacchiera):
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
    tempo_inizio = time.time()
    control_numero = 2
    control = True
    """while control:
        random_generator.shuffle(list(range(int(control_numero))))
        if soluzione_ok(scacchiera) and controllo: 
            tempo = time.time() - tempo_inizio
        if tempo>15:
            control = False
        else:
            control_numero+=1
    print ("la dimensione minima è " + str(control_numero))"""





# chiamo la funzione principale 
main()
