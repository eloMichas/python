
    #Program ma za zadanie wygenerowanie losowego hasła
    #oraz zapisanie go w .txt, jest też możliwość dodania
    #miejsca użycia hasła

#import random
import random

#Zmienne
char = 'abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ123456789!@#$%&'
password = ''

#Pętla nieskończona pytająca o długość hasła
while True:

    try:
        pass_len = int(input('Jaka ma być długość hasła? '))
        break
    except:
        print("Proszę o podanie liczby :)")

#Pętla wykonująca program
while True:
    for i in range(pass_len):
        pass_char = random.choice(char)
        password += pass_char
    break

#Wypisanie hasła
print(password)

#Zapytanie gdzie zostało użyte hasło
where_use = input('Podaj miejsce użycia hasła :) : ')

#Zapisanie na pliku .txt
with open('C:\\Users\\mlawn\\Desktop\\passwords.txt','a') as file:

    file.write(password + ' ' + where_use + '\n')