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
def formattazione_frasi():
    valore = ''
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
    rubrica_ordinata = dict(sorted(rubrica.items(), key = lambda x: x[1]['età']))        #comando usato per mettere in ordine i dizionari secondo un parametro particolare
    lista_nomi_ordinati = []
    for i in rubrica_ordinata:
        lista_nomi_ordinati.append(i)
    return lista_nomi_ordinati
def lista_età_contrario():
    rubrica_ordinata = dict(sorted(rubrica.items(), key = lambda x: x[1]['età'], reverse=True))  #comando usato per mettere in ordine i dizionari secondo un parametro particolare al contrario
    lista_nomi_ordinati = []
    for i in rubrica_ordinata:
        lista_nomi_ordinati.append(i)
    return lista_nomi_ordinati
# print(formattazione_frasi())
# print(lista_età())
# print(lista_età_contrario())