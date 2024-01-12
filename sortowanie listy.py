# lista
lista=[]
# pętla nieskończona do pytania odnośnie produktów które potem sie doda
while True:
    x=input('(0 żeby zakończyć)Dodaj słówko: ')
    lista.append(x)
    if x==str(0):
        lista.pop()
        break
# sortowanie listy
lista.sort()
# wypisanie listy od góry do dołu pojedyńczo
for w in lista:
    print(w)