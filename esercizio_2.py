testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''

caratteri = [',', '.', ':', ';', '?', '!']

def n_righe (t):
    list_testo = t.split ("\n")
    n_righe = 0
    for i in list_testo:
        if i != '':
            n_righe+=1
    return n_righe

def n_parole(t):
    list_testo = t.split ()
    n_parole =  len (list_parole)
    return n_parole

def n_caratteri(t):
    list_caratteri = list(t)
    n_caratteri = 0
    for i in list_caratteri:
        if i.isalnum:                       #con questo programma controllo quali
            n_caratteri+=1                  #caratteri sono alfanumerici
    return n_caratteri

def carattere_p(t, lettera):
    list_caratteri = list(t)
    n_caratteri = 0
    for i in range (len(list_caratteri)):
        if list_caratteri[i] == lettera or list_caratteri[i] == lettera.upper():
            n_caratteri+=1
    return n_caratteri

def sostituzione_PYTHON(t):
    list_testo = t.split('\n')
    parole_cercate = ['day', 'about', 'water']
    for i in range (len(list_testo)):
        parole = list_testo[i].split(" ")
        for j in range (len(parole)):
             for k in parole_cercate :
                if parole[j].lower() == k or parole[j].lower() == k + ',':
                    parole [j] = 'PYTHON'
        list_testo [i] = " ".join(parole)
    return list_testo

def parole_dispari(t):
    list_testo = t.split('\n')
    for i in range (len(list_testo)):
        parole = list_testo[i].split(" ")
        for j in range (len(parole)):
            if j%2 == 0:
                parole [j] = parole[j].upper()
        list_testo [i] = " ".join(parole)
    return list_testo

def versi_contrario(t):
    list_testo = t.split ("\n")
    list_contrario = []
    for i in range (len(list_testo)):
        list_contrario.append(list_testo [-i])
    return list_contrario

def verso_2_inverso(t):
    list_testo = t.split("\n")
    controllo = 0
    for i in range(len(list_testo)):
        if list_testo[i] != '' and list_testo[i] != ' ':
            list_parole = list_testo[i]
            if controllo == 1:
                list_parole = list(list_testo[i])
                list_parole = "".join(list_parole[::-1])   #compatto la lista in una str, attraverso lo slicing (funziona come il range circa)
            list_testo[i] = list_parole
            if controllo ==4 :
                controllo = 0
            controllo+=1
    return list_testo
 
def parole_uguali(t):
    strofe = t.strip().split('\n\n')
    parole_uguali = set()
    for i in range(len(strofe)):
        parole = strofe[i].split()
        for k in parole:
            controllo_1 = 0
            controllo_2 = 0
            controllo_3 = 0
            controllo_4 = 0
            for j in range(len(strofe)):
                if i != j:
                    parole_controllo = strofe[j].split()
                    for m in parole_controllo:
                        for n in (0, 1 ,2 ,3 ,4 ,5):
                            if j == 0 and (k.lower() == m.lower() or k.lower() == m.lower() + caratteri[n]) :
                                controllo_1 = 1
                            elif j == 1 and (k.lower() == m.lower() or k.lower() == m.lower() + caratteri[n]) :
                                controllo_2 = 1
                            elif j == 2 and (k.lower() == m.lower() or k.lower() == m.lower() + caratteri[n]) :
                                controllo_3 = 1
                            elif j == 3 and (k.lower() == m.lower() or k.lower() == m.lower() + caratteri[n]) :
                                controllo_4 = 1
                        somma = controllo_1 + controllo_2 + controllo_3 + controllo_4
                        if somma == 3:
                            parole_uguali.add(k.lower())
    return parole_uguali                        

def lista_parole_uniche(t):
    testo_senza_punteggiatura = "".join(c for c in t if c.isalpha() or c.isspace())
    lista_parole = testo_senza_punteggiatura.split()
    set_parole = set()
    lunghezza_parola_maggiore = 0
    for j in lista_parole:
        set_parole.add(j.lower()) 
    lista_parole = list (set_parole)
    for i in lista_parole:
        if lunghezza_parola_maggiore < len(i):
            lunghezza_parola_maggiore = len(i)
    for i in lista_parole:
        for j in range(lunghezza_parola_maggiore):

    return lista_parole
     


    
#print(n_righe(testo))
#print(n_parole(testo))
#print(n_caratteri(testo))
#lettera_cercata = input ('inserisci una lettera da cercare nel testo: ')
#print(carattere_p(testo, lettera_cercata))
#print(sostituzione_PYTHON(testo))
#print(parole_dispari(testo))
#print (versi_contrario(testo))
#print (verso_2_inverso(testo))
#print ("le parole uguali sono: ")
#print (parole_uguali(testo))
print (lista_parole_uniche(testo))
