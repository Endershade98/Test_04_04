"""Es 2:  Andare a creare un sistema ripetibile che si occupa di gestire la lunghezza delle stringhe e salvarle, 
l'utente potrà continuare a inserire dati finché la stringa inserita e più lunga della precedente, 
alla fine stamperà l'insieme delle stringhe date in input divise da virgole e quante stringhe ha inserito"""

start = bool(input("Vuoi iniziare? (True/False): "))
test_stringa = input("Inserire la stringa di test: ") # il mio test
insieme_stringhe = []

while start:# inizia il gioco se la condizione è verificata
    stringa = input("Inserire una stringa qualsiasi: ")
    while len(test_stringa) < len(stringa):
        insieme_stringhe.append(stringa)
        if len(test_stringa) >= len(stringa):# stampa l'insieme se la condizione è verificata
            print(insieme_stringhe)
            break
        
"""Es 1: Crea un sistema ripetibile che si occupi di dividere su tre possibili 
liste i tipi basilari di dato che riceve in entrata. 
Deve poter stampare una lista singola o tutte.  
Si deve ripetere X volte definite all'inizio dall'utente"""

def check_tipo(tipo_dato):
    """restituisce il tipo del dato inserito"""
    interi = []
    stringhe = []
    booleani = []
    if type(tipo_dato) == int:
        interi.append(tipo_dato)
    elif type(tipo_dato) == str:
        stringhe.append(tipo_dato)
    elif type(tipo_dato) == bool:
        booleani.append(tipo_dato)
