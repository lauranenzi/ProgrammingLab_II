# Definizione della classe CSVFile
class CSVFile():
    
    # Metodo costruttore della classe, inizializza l'attributo 'name' con il nome del file
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError('Nome del file non stringa')       
        self.name = name

        # Provo ad aprirlo e leggere una riga
        try:
            with open(self.name, 'r') as my_file:
                my_file.readline()
        except Exception as e:
                print('Errore in apertura del file: "{}"'.format(e))
        
        
    # Metodo per ottenere i dati dal file CSV
    def get_data(self, start=None, end=None):
        if start is not None:
            try:
                start = int(start)
            except:
                raise TypeError('Start non interpretabile come intero ("{}")'.format(start))
            if start <= 0:
               raise ValueError('Start minore o uguale a zero ("{}")'.format(start))
        if end is not None:
            try:
                end = int(end)
            except:
                raise TypeError('Start non interpretabile come intero ("{}")'.format(end))
            if end <= 0:
                raise ValueError('End minore o uguale a zero ("{}")'.format(end))
        
        if start is not None and end is not None and start > end:
            raise ValueError('Start maggiore di end! start="{}", end="{}"'.format(start,end))         
          
        # Apertura del file in modalità lettura
        my_file = open(self.name, 'r')
        my_list = []

        # Inizializzo `i` a -1 per gestire correttamente il ciclo anche se il file è vuoto
        i = -1
        # Scorrimento di ogni riga del file
        for i, line in enumerate(my_file):
                # Divido la riga in elementi separati da virgola
                elements = line.split(',')
                # Rimuovo eventuali spazi vuoti o caratteri di nuova linea alla fine
                elements[-1] = elements[-1].strip()
                # Salto l'intestazione se la prima colonna contiene 'Date'
                if elements[0] != 'Date':
                    # Aggiungo alla lista gli elementi di questa linea se devo
                    if start is not None and end is None:
                        if i+1 >= start:
                            my_list.append(elements)
                    elif end is not None and start is None:
                        if i+1 <= end:
                            my_list.append(elements)
                    elif start is not None and end is not None:
                        if i+1 >= start and  i+1 <= end:
                            my_list.append(elements)
                    else:
                        my_list.append(elements)

        # Controllo che `i` sia stato assegnato, altrimenti significa che il file era vuoto
        if i == -1:
            raise ValueError('Il file è vuoto!')
        
        if start is not None and start > i:
            raise ValueError('Start maggiore del totale delle righe del file (end="{}", righe="{}"'.format(start, i))            
        if end is not None and end > i:
            raise ValueError('End maggiore del totale delle righe del file (end="{}", righe="{}"'.format(end, i))  
        # Chiudo il file
        my_file.close()
        # Ritorno la lista dei dati letti dal file
        return my_list            
        
# Definizione della classe NumericalCSVFile, che eredita dalla classe CSVFile
class NumericalCSVFile(CSVFile):

    # Sovrascrittura del metodo get_data
    def get_data(self, *args, **kwargs):
        # Chiamo il metodo get_data della classe base (CSVFile) per ottenere i dati grezzi
        lista_dati = super().get_data(*args, **kwargs)

        # Lista per contenere i dati convertiti in numeri
        numerical_data = []

        # Scorro ogni riga nella lista dei dati
        for riga in lista_dati:
            # Lista per la riga convertita (se possibile) in numeri
            numerical_row = []

            # Scorro ogni elemento della riga
            for i, elemento in enumerate(riga):
                # Il primo elemento (indice 0) è mantenuto come stringa (es. la data)
                if i == 0:
                    numerical_row.append(elemento)
                else:
                    try:
                        # Provo a convertire l'elemento in float
                        numerical_row.append(float(elemento))
                    # Se c'è un errore di conversione, lo segnalo e interrompo la lettura della riga
                    except ValueError as e:
                        print('Il valore "{}" non è un numero. Errore: "{}" '.format(elemento, e))

            # Se la riga originale ha lo stesso numero di elementi convertiti, la aggiungo alla lista finale
            if len(riga) == len(numerical_row):
                numerical_data.append(numerical_row)

        # Ritorno la lista dei dati numerici
        return numerical_data
    

# shampoofile = NumericalCSVFile('shampoo_sales.csv')
# lista_dati = shampoofile.get_data()
# print(lista_dati)
