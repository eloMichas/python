'''
    Program ma za zadanie posortowanie alfabetycznie wpisanych słów
'''
list=[]
#Pętla nieskończona do pytania odnośnie produktów które potem sie doda
while True:
    x=input('(0 żeby zakończyć)Dodaj słówko: ')
    list.append(x)
#Dzięki tej części, po wpisaniu '0', aby wyjść z pętli. Pętla zostanie przerwana i zostanie usunięty ostatni element, czyli '0'
    if x==str(0):
        list.pop()
        break
#Sortowanie listy
list.sort()
#Wypisanie listy od góry do dołu pojedyńczo
for w in list:
    print(w)
