def is_pari (n):
    '''Vedo se un numero è pari o dispari'''
    if n%2 == 0 :
        return True
    else :
        return False

def return_valore ():
    '''Chiedo all'utente un numero positivo'''
    a = True
    while a:
        b = input('scrivi un numero positivo: ')
        b = int (b)
        if b > 0:
            a = False
    return b

def lista_valore_pr ():
    '''creo una lista in base al numero precedente'''
    a = return_valore ()
    a = int (a)
    b = 0
    valoritr = []
    while a >= 1 and b < 100 :
        if is_pari (a):
            a = a//2
        else :
            a = a*3 +1
        valoritr.append(a)
        b += 1
    return valoritr

def analizza_sequenza (lista) :
    '''Vedo qual'è il valore maggiore, la somma e la lunghezza della lista'''
    massimo = 0
    somma = 0
    controllo = 0
    lunghezza = len (lista)
    while controllo < lunghezza:
        valorel = lista [controllo]
        if valorel > massimo:
            massimo = valorel
        somma = somma + valorel
        controllo += 1
    return massimo, somma, lunghezza

def ricerca_divisibili_5 (lista):
    '''ricerco e trascrivo i numeri divisibili per 5'''
    length = len (lista)
    control = 0
    ndivisibili = 0
    print ('i numeri divisibili per 5 sono: ')
    while control < length:
        valorel = lista [control]
        if valorel % 5 == 0:
            print (valorel)
            ndivisibili += 1
        control+=1
    if ndivisibili == 0:
        print('non erano presenti numeri divisibili per 5')

numero_da_analizzare = input ('quanti numeri vuoi analizzare? ')
numero_da_analizzare = int (numero_da_analizzare)

for i in range (numero_da_analizzare):
    numero_controllo = return_valore ()
    numero_controllo = int (numero_controllo)
   print (is_pari (numero_controllo))
   sequenza = lista_valore_pr () 
   print (analizza_sequenza (sequenza))
   ricerca_divisibili_5 (sequenza)

