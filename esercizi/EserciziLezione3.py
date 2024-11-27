# Esercizio 1: Definire una funzione che prende in input un file ed una parola e 
# conta quante volte quella parola è presente nel file
def parola_nel_testo(file_name, parola):
    # Metto la parola in minuscolo
    parola = parola.lower()    
    # Inizializzo una variabile che tiene conto della somma
    somma = 0
    # Apro il file, lo leggo, e lo chiudo
    testo = open(file_name, 'r')
    contenuto = testo.read()
    testo.close()
    # Divido le parole in base agli spazi
    parole = contenuto.split()
    # Per ogni parola nel testo
    for p in parole:
        # La trasformo in minuscolo
        p = p.lower()
        # Controllo se è uguale alla parola target, se lo è aggiungo alla variable somma +1
        if p == parola:
            somma+=1     
    return somma

def parola_nel_testo_v2(file_name, parola):
    # Apro e leggo del file con gestione automatica della chiusura
    with open(file_name, 'r') as file:
        contenuto = file.read()   
    # Divisione del contenuto in parole in base agli spazi 
    parole = contenuto.split()
    # Conteggio delle occorrenze con metodo count
    return parole.count(parola)


#  Esercizio 2: Definire una funzione che prende come input un file e conta quante volte ogni parola è presente
def parole_nel_testo(file_name):
    # Inizializzo un dizionario vuoto
    dizionario = {}
    
    # Apro il file, lo leggo e lo chiudo 
    testo = open(file_name, 'r')
    contenuto = testo.read()
    testo.close()

    # Divido le parole in base agli spazi
    parole = contenuto.split()
    
    # Per ogni parola nel testo
    for p in parole:
        # La trasformo in minuscolo
        p = p.lower()
        
        # Controllo nel dizionario se la parola è già stata aggiunta
        if p not in dizionario.keys():
            # Se non lo è la aggiungo e inizializzo a 1 il contatore
            dizionario[p] = 1
        else:
            # Se è già nel dizionario aggiorno il contatore di 1
            dizionario[p] +=1
    
    testo.close()        
    return dizionario

#  Esercizio 3: Definire una funzione che prende in input un file e costruisce un dizionario con chiavi 
# la lettere iniziali e con valore le parole di lunghezza maggiore contenute nel file che 
# iniziano con quelle lettere.
def lettere_iniziali(file_name):
    # Inizializzo un dizionario vuoto
    dizionario = {}
    
    # Apro il file, lo leggo e lo chiudo 
    testo = open(file_name, 'r')
    contenuto = testo.read()
    testo.close()

    # Divido le parole in base agli spazi
    parole = contenuto.split()
    
    # Per ogni parola nel testo
    for p in parole:
        # La trasformo in minuscolo
        p = p.lower()
        
        # Controllo nel dizionario se la parola è già stata aggiunta
        if p[0] not in dizionario.keys():
            # Se non lo è la aggiungo e inizializzo alla lunghezza della parola il contatore
            dizionario[p[0]] = len(p)
        
        # Se la parola è già nel dizionario controllo se il contatore è minore della lunghezza
        # della parola attuale    
        elif dizionario[p[0]] < len(p):
            # Se lo è aggiorno il contatore con la lunghezza dell'attuale parola
            dizionario[p[0]] = len(p)
    
    return dizionario

# Esercizio 4: Definire una funzione conteggio che prende come input un file e ritorna un dizionario 
# con chiave la prima parola di ogni frase e valore il numero di volte che una frase inizia 
# con quella parola. Considerare come inizio di frase qualsiasi parola che segue un punto, 
# un punto esclamativo, un punto interrogativo o si trova all'inizio del testo.
def conteggio(file_name):
    # Inizializzo un dizionario vuoto
    dizionario = {}
    
    # Apro il file, lo leggo
    testo = open(file_name, 'r')
    contenuto = testo.read()
    testo.close()   

    # Sostituisco con un . sia ? e ! così da avere un separatore unico
    contenuto = contenuto.replace('?', '.').replace('!', '.')
    # Quindi divido il testo rispetto al .
    frasi = contenuto.split('.')
    
    # Leggo una frase alla volta
    for f in frasi:
        # Controllo che la frase non sia vuota
        f = f.strip()
        # Se la frase non lo è
        if f:
            # Ottengo la parola iniziale dividendo la frase per spazio, prendo il primo elemento
            # e lo trasformo in minuscolo
            parola_inziale = f.split()[0].lower()
            
            # Controllo che la parola non sia già nel dizionario
            if parola_inziale not in dizionario.keys():
                # Se non lo è la aggiungo e metto il contatore a 1
                dizionario[parola_inziale] = 1
            else:
                # Se lo è aggiorno il contatore di 1
                dizionario[parola_inziale] +=1
    
     
    return dizionario

# Importo un pacchetto esterno
import re
def conteggio_v2(file_name):
    # Inizializzo un dizionario vuoto
    dizionario = {}
    
    # Apro il file, lo leggo e lo chiudo
    testo = open(file_name, 'r')
    contenuto = testo.read()
    testo.close() 

    # Utilizzo una funzione da un pacchetto esterno (re) che mi da la possibilità
    # di dividere il testo in base al .,?,!
    # https://docs.python.org/3/library/re.html
    frasi = re.split(r'[.!?]\s*', contenuto)
    
    # Leggo una frase alla volta
    for f in frasi:
        # Controllo che la frase non sia vuola
        f = f.strip()
        # Se la frase non lo è
        if f:
            # Ottengo la parola iniziale dividendo la frase per spazio, prendo il primo elemento
            # e lo trasformo in minuscolo
            parola_inziale = f.split()[0].lower()
            
            # Controllo che la parola non sia già nel dizionario
            if parola_inziale not in dizionario.keys():
                # Se non lo è la aggiungo e metto il contatore a 1
                dizionario[parola_inziale] = 1
            else:
                # Se lo è aggiorno il contatore di 1
                dizionario[parola_inziale] +=1
      
    return dizionario

# Esercizio 5: Definire una funzione che prende come input un file, rimuove tutte le righe duplicate, 
# scrive il risultato in un nuovo file chiamato unique.txt.
def rimuovi_duplicato(file_name):

    # Leggo riga per riga 
    with open(file_name, 'r') as file:
        lista_righe = file.readlines()
    
    # Inizializzo una lista vuota che conterrà le righe già viste
    righe = []
    for riga in lista_righe:
        # Se la riga attuale non è nella lista della righe già viste
        if riga not in righe:
            # Aggiungo la riga alla list
            righe.append(riga)
            
    # Scrivo su un file le righe uniche
    with open('unique.txt', 'w') as file_unique:
        for riga in righe:
            file_unique.write(riga)
    
    