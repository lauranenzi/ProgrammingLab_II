# Esercizio 1: Stampare l'equivalente di 538 minuti nel formato 12h:32min.   
frase = "538 minuti sono {}h:{}min"
frase_completa = frase.format(538//60, 538%60)
print(frase_completa)

# Esercizio 2: Definire una funzione che prende come argomento una parola e una lettera. 
# Ritorna quante volte quella lettera è contenuta nella parola.  
def conta(parola, lettera):
    quante_volte = 0
    for carattere in parola:
        if carattere == lettera:
            quante_volte += 1
    return quante_volte

def conta2(parola, lettera):
    return parola.count(lettera)

# Esercizio 3: Scrivere una funzione che prende in input una stringa 
# e ritorna True se è un palindromo, False altrimenti
def is_palindromo(stringa):
    return stringa == stringa[::-1]

# Esercizio 4: Definire una funzione che dati 3 numeri interi stabilisce 
# se possono essere i valori di 3 lati di un triangolo e se si di che tipo di triangolo
def tipo_triangolo(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Non è un triangolo"
    elif a == b == c:
        return "Triangolo equilatero"
    elif a == b or a == c or b == c:
        return "Triangolo isoscele"
    else:
        return "Triangolo scaleno"
    
# Esercizio 5: Definire una funzione che prende in input una lista A, 
# gli indici i e j, e scambia il valore di A[i] con A[j].
def scambio_indici(lista, i,j):
    valore_i = lista[i]
    lista[i] = lista[j]
    lista[j] = valore_i
    return lista

def scambio_indici2(lista, i,j):
    lista[i], lista[j] = lista[j], lista[i]
    return lista

# Esercizio 6: Definiere la funzione fattoriale
def fattoriale(n):
    if n  == 0 or n == 1:
        return 1
    else:
        return n * fattoriale(n-1)
    
def fattoriale_iterativo(n):
    risultato = 1
    for i in range(1, n + 1):
        risultato *= i
    return risultato

# Esercizio 7: Scrivere una funzione che prende in input due liste 
# e ritorna `True` se le due liste hanno almeno un elemento in comune
def elementi_in_comune(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True

# Esercizio 8: Definire una funzione che prende in input una lista di numeri interi in [0, 9] 
# e ritorna una lista di stringhe, corrispondenti ai numeri scritti in Italiano, 
# es. [1,0,7,9,8] ->["uno","zero","sette","nove","otto"]
def converti_numeri(lista_numeri):
    lista_stringhe = []
    dizionario_numeri_stringhe = { 0:"0", 1: "1", 2: "2", 3:"3", 4:"4",
                               5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
    for numero in lista_numeri:
        lista_stringhe.append(dizionario_numeri_stringhe[numero])
    return lista_stringhe
 