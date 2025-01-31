class ExamException(Exception):
    pass

class CSVTimeSeriesFIle():
    """
    Questa classe rappresenta un lettore di file CSV che:
      - Verifica che il file sia apribile;
      - Legge ogni riga, assumendo ci siano almeno due campi:
        (data, numero_di_passeggeri);
      - Prova a convertire il numero di passeggeri in int;
      - Se riesce, lo aggiunge a una lista nel formato [[data, passeggeri], ...],
        altrimenti ignora la riga.
    """
    def __init__(self, nome_file):
        # Salvataggio del nome del file
        self.name = nome_file

    def get_data(self):
        """
        Tenta di aprire il file `self.name`.
        Legge ogni riga e, se valida, la inserisce in un elenco
        time_series = [[date_str, passengers_int], ...].
        Ritorna time_series.
        """
        try:
            file = open(self.name, 'r') 
        except:
            # Se non riesce ad aprire il file, solleva un'eccezione
            raise ExamException('Impossibile aprire il file')
        
        time_series = []
        # Ciclo su ogni riga del file
        for line in file:
            # Separiamo i campi usando la virgola
            elementi = line.strip().split(',') # es. ["data", "n_passeggeri"]

            # Verifichiamo che non stiamo leggendo l'header (controlliamo se la prima
            # colonna è "date"). Se lo è, ignoriamo la riga.
            if elementi[0] != 'date':

                # Prendiamo la data come stringa
                data = elementi[0]
                try:
                    n_passeggeri = int(elementi[1])
                    time_series.append([data,n_passeggeri])
                except:
                    # Se fallisce la conversione, stampiamo un messaggiove e di fatto 
                    # ignoriamo la riga (non facciamo "continue", basta non aggiungere)
                    print('Il valore "{}" non è un numero intero. Riga {} ignorata'.format(elementi[1].strip(), elementi)) # type: ignore

        file.close()
        return time_series

def compute_variation(time_series, first_year, last_year):
    """
    Questa funzione:
      - Converte first_year e last_year in interi n_init e n_end;
      - Per ogni elemento di time_series (del tipo [data_str, passeggeri]),
        estrae l'anno e, se è compreso tra n_init e n_end (inclusi), raggruppa
        il valore di passeggeri in un dizionario:
              diz_anno_passeggeri[anno] = lista di passeggeri
      - Calcola la media dei passeggeri per ciascun anno
      - Calcola la variazione tra le medie di anni consecutivi nei dati
      - Ritorna un dizionario nel formato:
            {
              "anno1-anno2": variazione,
              ...
            }
    """ 
    
    # Converto gli anni in interi
    n_init = int(first_year)
    n_end = int(last_year)

    # Dizionario per raggruppare i valori di passeggeri per anno
    diz_anno_passeggeri = {}

    # Per ogni riga della serie, estraiamo l'anno e accumuliamo i passeggeri
    for lines in time_series:       # es. ["1950-01",100]
        data = lines[0].split('-')  # ["1950","01"]
        anno = int(data[0])         # 1950

        # Se l'anno è dentro l'intervallo desiderato
        if anno >= n_init and anno <= n_end:
            # Se l'anno non è ancora presente nel dizionario, lo aggiungiamo come
            # nuova chiave del dizionario e inizializziamo una lista vuota
            # Assumento che time_series sia ordinata, gli anni vengono aggiunti
            # al dizionario in ordine crescente
            if anno not in diz_anno_passeggeri.keys():                
                diz_anno_passeggeri[anno] = []
            # Aggiungiamo il valore di passeggeri alla lista di quell'anno     
            diz_anno_passeggeri[anno].append(lines[1])
    # {1950:[12,30,40],...}

    medie_annuali = []

    # Calcoliamo le medie annuali: costruiamo una lista di [anno, media]
    # Utilizziamo la funzione sorted() per essere sicuri che gli anni vengano
    # considerati in ordine crescente (lo stesso ordine in cui abbiamo creato le chiavi)
    for anno in sorted(diz_anno_passeggeri.keys()):
        somma = sum(diz_anno_passeggeri[anno])
        lunghezza =  len(diz_anno_passeggeri[anno])
        media = somma/lunghezza
        if lunghezza > 0 : # per costruzione è sempre verificato, ma un controllo in più non fa male
            medie_annuali.append([anno, media])

    # Calcoliamo ora la variazione tra le medie di ogni coppia consecutiva 
    dizionario_variazioni = {}
    for i in range(len(medie_annuali) - 1):
        # medie_annuali[i] = [anno_i, media_i]
        # medie_annuali[i+1] = [anno_{i+1}, media_{i+1}]

        # Chiave = "anno_i-anno_{i+1}" 
        chiave = str(medie_annuali[i][0]) + '-' + str(medie_annuali[i+1][0])
        # Valore = media_{i+1} - media_i
        valore = medie_annuali[i+1][1]-medie_annuali[i][1]
        dizionario_variazioni[chiave] = valore
    return dizionario_variazioni

# Blocco di prova del codice
if __name__ == "__main__":
        
        # Istanzio la classe passandole il nome del file
        time_series_file = CSVTimeSeriesFIle('data.csv')

        # Estraggo la serie temporale
        time_series = time_series_file.get_data()
        print(time_series)

        # Calcolo la variazione sulle medie annuali nell'intervallo 1953-1960
        variazioni = compute_variation(time_series, '1953', '1960')
        print(variazioni)
