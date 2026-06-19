#
# File: esercizio_4.py
#
# Author: D.Cicogna
#
# Date: 19/06/2026
#
# Version: 1.0
#
# Description: Partendo dall’esercizio 3, aggiungete una opzione al programma per generare un file di testo rubrica.txt 
#contenente tutti gli elmenti della rubrica, uno per linea, con tutte le informazioni separate da virgole. Ad esempio:
#Paolino Paperino, 9, giugno, 1934, 89, M, paolino.paperin0@disney.org
#Ron Weasley, 1, marzo, 1980, 43, M, ron_weasley80@hogwards.uk
#ecc...
#
#Create un file JSON che contiene la rubrica con la stessa struttura del dizionario interno al programma
#
#Leggete la rubrica salvata in un file formato JSON e visualizzate tutto il contenuto
#
import sys                              #importo delle librerie per poter inserire elementi dalla barra del terminale
import argparse
import json

rubrica = {
  'Paolino Paperino': {'giorno': 9, 
                      'mese': 'giugno',
                      'anno': 1934,
                      'età': 93,
                      'sesso': 'M',
                      'mail': 'paolino.paperin0@disney.org'},
'Ron Weasley': {'giorno': 1, 
                'mese': 'marzo', 
                'anno': 1980, 
                'età': 46, 
                'sesso': 'M', 
                'mail': 'ron_weasley80@hogwards.uk'},
'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}
ciclo = True

def formattazione_frasi():
    """stampo una frase per ogni personaggio nella lista, facendo differenza fra uomo e donna"""
    lista_persone = []
    for i in rubrica:
        giorno = rubrica [i]['giorno']
        mese = rubrica [i]['mese']
        anno = rubrica [i]['anno']
        età = rubrica [i]['età']
        sesso = rubrica [i]['sesso']
        mail = rubrica [i]['mail']
        if sesso == 'M':
            out = f'Sono {i}, sono nato il {giorno} {mese} del {anno}, ho {età} anni, mi identifico come un maschio ({sesso}) e la mia mail è {mail}'
        else:
            out = f'Sono {i}, sono nata il {giorno} {mese} del {anno}, ho {età} anni, mi identifico come una femmina ({sesso}) e la mia mail è {mail}'
        lista_persone.append(out)
    return lista_persone

def lista_età():
    """creo una lista ordinata in base all'età"""
    rubrica_ordinata = dict(sorted(rubrica.items(), key = lambda x: x[1]['età']))        #comando usato per mettere in ordine i dizionari secondo un parametro particolare
    lista_nomi_ordinati = []
    for i in rubrica_ordinata:
        lista_nomi_ordinati.append(i)
    return lista_nomi_ordinati

def lista_età_contrario():
    """creo la stessa lista di prima ma capovolta"""
    rubrica_ordinata = dict(sorted(rubrica.items(), key = lambda x: x[1]['età'], reverse=True))  #comando usato per mettere in ordine i dizionari secondo un parametro particolare al contrario
    lista_nomi_ordinati = []
    for i in rubrica_ordinata:
        lista_nomi_ordinati.append(i)
    return lista_nomi_ordinati

def messaggio_personaggio(controllo):
    """creo un messaggio personalizzato per un singolo personaggio"""
    giorno = rubrica [controllo]['giorno']
    mese = rubrica [controllo]['mese']
    anno = rubrica [controllo]['anno']
    età = rubrica [controllo]['età']
    sesso = rubrica [controllo]['sesso']
    mail = rubrica [controllo]['mail']
    if sesso == 'M':
        carattere = 'o'
    else:
        carattere = 'a'
    out = (f'Car{carattere} {controllo},\n sei nat{carattere} il {giorno} di {mese} del {anno}'
           f'e quindi a breve compirai {età} anni. \n Ti manderemo gli auguri a {mail}')    
    return out 

def dato_cercato_sys ():
    try:
        """cerco un personaggio in base ad un dato inserito via sys"""
        dizionario_persone = {}
        if sys.argv [1] == 'giorno' or sys.argv [1]== 'mese' or sys.argv [1]== 'anno' or \
        sys.argv [1]== 'età' or sys.argv [1] == 'sesso' or sys.argv [1] == 'mail':
            for i in rubrica:
                dizionario_persone [i] = rubrica [i] [sys.argv [1]]
        else:
            dizionario_persone['errore'] = 'valore non valido, mi dispiace'
    except IndexError:
        dizionario_persone ['errore'] = "non hai inserito nulla"
    return dizionario_persone

def dato_cercato_argv (chiave):
    """faccio lo stesso ragionamento di prima, ma con argv"""
    dizionario_persone = {}
    if  chiave == 'giorno' or chiave == 'mese' or chiave == 'anno' or chiave== 'età' \
    or chiave == 'sesso' or chiave== 'mail':
        for i in rubrica:
            dizionario_persone [i] = rubrica [i] [chiave]
    else:
        dizionario_persone['errore'] = 'valore non valido, mi dispiace'
    return dizionario_persone

# scrivo il messaggio per l'utente del programma in caso si usi argvparse
parser = argparse.ArgumentParser()
parser.add_argument ('-cntrl', '--controllo', help='codice di controllo: 1: presentazione di tutti i personaggi; 2: lista in base alla età; 3: listà in base alla età al contrario; 4: messaggio del personaggio; 5: cercare un dato preciso: 6: crea un file di testo')
parser.add_argument ('-n', '--nome', help='nome del personaggio da mettere fra Paolino, Ron, Ramona, Madoka (se controllo = 4)')
parser.add_argument ('-k', '--chiave', help='inserire una delle seguenti parole: giorno, mese, anno, sesso, età, mail (se controllo = 4)')
parser.add_argument ('-c', '--cognome', help='associa ai nomi precedenti i cognomi, ogni nome associato al cognome nella stessa posizione, Paperino, Weasley, Flowers, Ayukawa (se controllo = 5)')
args = parser.parse_args()
controllo = args.controllo
if controllo == '1':
    print(formattazione_frasi())
elif controllo == '2':
    print(lista_età())
elif controllo == '3':
    print(lista_età_contrario())
elif controllo == '4':
    try:
        controllo_nome = args.nome + ' ' + args.cognome
        print(messaggio_personaggio(controllo_nome))
    except TypeError:
        print("non hai inserito tutti i dati richiesti")
elif controllo == '5':
    chiave = args.chiave
    print(dato_cercato_argv(chiave))
elif controllo == '6':
    righe_nomi = open('righe_nomi.txt', 'w')                #apro un file di testo di tipo txt
    for i in rubrica:
        testo = '' + i + ' , ' + str(rubrica [i]['giorno']) + ' , ' + str(rubrica [i]['mese']) + ' , ' + str(rubrica [i]['anno']) + ' , ' \
                + str(rubrica [i] ['età']) + ' , ' + str(rubrica [i]['sesso']) + ' , '  + str(rubrica[i]['mail']) + '\n'
        righe_nomi.write(testo)
    righe_nomi.close()
else:
    print('comando sbagliato, mi dispiace')

#apro e prima scrivo e poi leggo un file json
with open ("dizionario_file.json", "w") as write_file:
    json.dump(rubrica, write_file, indent = 4)
with open ('dizionario_file.json', "r") as in_file:
    data = json.load (in_file)

print(data)
