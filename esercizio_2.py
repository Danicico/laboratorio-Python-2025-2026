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

def n_righe (t):
    list_testo = t.split ("\n")
    n_righe = 0
    lunghezza = len (list_testo)
    for i in range(lunghezza):
        if list_testo[i] != '':
            n_righe+=1
    return n_righe

def n_parole(t):
    list_testo = t.split ("\n")
    n_parole = 0
    for j in range (len(list_testo)):
        if list_testo [j] != '':
         list_parole = list_testo[j].split (" ")
         n_parole = n_parole + len (list_parole)
    return n_parole

def n_caratteri(t):
    list_caratteri = list(t)
    n_caratteri = 0
    for i in range (len(list_caratteri)):
        if list_caratteri[i].isalnum:       #con questo programma controllo quali
            n_caratteri+=1                  #caratteri sono alfanumerici
    return n_caratteri

print(n_righe(testo))
print(n_parole(testo))
print(n_caratteri(testo))
