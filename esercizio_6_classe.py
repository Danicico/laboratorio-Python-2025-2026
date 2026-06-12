import json

class Rubrica :
    def __init__(self):
        self.rubrica = {}
        self.controllo = False
    @classmethod
    def apri_json(cls, nome_file):
        try:
            with open(nome_file, "r") as in_file:
                dati=json.load(in_file)
        except FileNotFoundError:
            print("il file non esiste")
            return None
        rub = cls()
        rub.rubrica = dati
        rub.controllo = True
        return rub
    @classmethod
    def apri_txt(cls, nome_file):
        try:
            file_testo = open(nome_file, "r")
            contenuto = file_testo.readlines()
            file_testo.close()
        expect FileNotFoundError:
        print("il file non esiste")

        rub = cls()
        for righe in contenuto:
            righe = righe.strip()
            if not righe:
                continue
        try: nome, giorno, mese, anno, età, sesso, mail = line.split(";")
        rub.rubrica[nome] = 
        {
            "giorno":giorno,
            "mese": mese,
            "anno": anno,
            "età":età,
            "sesso": sesso,
            "mail": mail
        }
        rub.aperta = True
        return rub

    def aggiungi(self, nome, giorno, mese, anno, età, sesso, mail):
        if controllo:
            self.rubrica[nome] = {"giorno": giorno, "mese": mese, "anno" : anno, "età" :età, "sesso":sesso, "mail": mail}
        else:
            print("apri prima una rubrica")
    def rimuovi(self, nome):
        if not self.rubrica:
            print ("la rubrica è vuota")
        else:
            if nome not in self.rubrica:
                print("il contatto" + str(nome) + "non esiste in rubrica")
            else:
                del self.rubrica[nome]
    def salva(self, nome_file):
        if not self.rubrica:
            print("La rubrica è vuota")
        else:
            if nome_file.endswith(".json"):
                with open("esercizio_6.json", "w") as write_file:
                    json.dump(self.rubrica, write_file, indent=4)
            elif nome_file.endswith(".txt"):
                file_testo = open(nome_file, "w")
                file_testo.write(str(self.rubrica))
                file_testo.close
    def stampa(self, nome):
        if not self.rubrica:
            print ("la rubrica è vuota")
        else:
            if nome not in self.rubrica:
                print("Il contatto non esiste")
            else: 
                if  self.rubrica[nome]["sesso"].upper() == 'M':
                    print ("Caro " + str(nome) + ", sei nato il " + str(self.rubrica[nome]["giorno"]) + " di " + str(self.rubrica[nome]["mese"]) + " del "+ str(self.rubrica[nome]["anno"]) + " e quindi a breve compirai " + str(self.rubrica[nome]["età"]) + " anni. Ti manderemo gli auguri a " + str(self.rubrica[nome]["mail"]))
                else :
                    print ("Cara " + str(nome) + ", sei nata il " + str(self.rubrica[nome]["giorno"]) + " di " + str(self.rubrica[nome]["mese"]) + " del "+ str(self.rubrica[nome]["anno"]) + " e quindi a breve compirai " + str(self.rubrica[nome]["età"]) + " anni. Ti manderemo gli auguri a " + str(self.rubrica[nome]["mail"]))
