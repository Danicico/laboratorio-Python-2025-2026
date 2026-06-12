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