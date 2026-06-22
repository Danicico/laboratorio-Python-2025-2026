#
# File: esercizio_6.py
#
# Author: D.Cicogna
#
# Date: 22/06/2026
#
# Version: 1.0
#
# Description: in un file separato, create una classe rubrica
#
#la classe rubrica deve fare 5 azioni:
#
#aprire una rubrica leggendola da un file (JSON oppure testo) - APRI
#
#aggiungere un elemento alla rubrica - AGGIUNGI
#
#rimuovere un elemento dalla rubrica (dato il nome) - RIMUOVI
#
#salvare la rubrica su un file (JSON o testo) - SALVA
#
#stampare tutte le informazioni di un contatto (data il nome), come nell’eserczio 3 - STAMPA
#
#la classe rubrica deve inizializzarsi con un dizionario (come nell’esercizio 3)
#
#la classe rubrica deve avere un classmethod per inizializzarla con un file JSON
#
#la classe rubrica deve avere un classmethod per inizializzarla con un file testo
#
#Per “aggiungere un elemento”, bisogna aver prima aperto una rubrica, altrimenti si ottine un messaggio di errore “Prima apri una rubrica”
#
#Per “rimuivere un elemento”, deve esserci almeno un elemento nella rubrica altrimenti si ottine un messaggio di errore “La rubrica è vuota”. 
#Se l’elemento da rimuovere non esiste, il messaggio di errore sarà “Il contatto NOME non esiste in rubrica”
#
#Per “stampare le informazioni”, deve esserci almeno un elemento nella rubrica altrimenti si ottine un messaggio di errore “La rubrica è vuota”. 
#Se l’elemento da rimuovere non esiste, il messaggio di errore sarà “Il contatto NOME non esiste in rubrica”
#
#Per salvare la rubrica su file (JSON o txt deciso dall’estensione del nome del file), la rubrica non deve essere vuota, altrimenti si ottine un 
#messaggio di errore “La rubrica è vuota”
#
#In un file separato importate la classe rubrica appena creata e scrivete un programma che in modo interattivo chieda all’utente di quale delle 5 
#operazioni della classe rubrica svolgere. Se l’azione richiesta non esiste, il programma continua a chiedere l’azione da svolgere finchè non viene 
#indicata la stringa “EXIT”
#
from esercizio_6_classe import Rubrica 

comando = input ("che cosa vuoi fare (comandi validi: apri, aggiungi, rimuovi, salva, stampa; per terminare: exit): ")
while comando.upper() != "EXIT":
    if comando.upper() == "APRI":
        nome_file = input("scrivi il nome del file da qui prendere i dati: ")
        if nome_file.endswith(".txt"):
            r = Rubrica.apri_txt(nome_file)
        elif nome_file.endswith(".json"):
            r = Rubrica.apri_json(nome_file)
    elif comando.upper() == "AGGIUNGI":
        nome= input("scrivi il nome: ")
        giorno= input("scrivi il giorno di nascita: ")
        mese= input("scrivi il mese di nascita: ")
        anno= input("scrivi l'anno di nascita: ")
        età= input("scrivi l'età: ")
        sesso= input("scrivi il sesso: ")
        mail= input("scrivi la mail: ")
        r.aggiungi(nome, giorno, mese, anno, età, sesso, mail)
        comando = "exit"
    elif comando.upper() == "RIMUOVI":
        nome = input("scrivi il nome della persona da rimuovere: ")
        r.rimuovi(nome)
    elif comando.upper() == "SALVA":
        r.salva()
    elif comando.upper() == "STAMPA":
        nome = input("di chi vuoi i dati: ")
        r.stampa(nome)
    else:
        print("comando non valido, riprovare")
    comando = input("che cosa vuoi fare (comandi validi: apri, aggiungi, rimuovi, salva, stampa; per terminare: exit): ")