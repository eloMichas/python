# import

import time

# przywitanie i rozpoczęcie

print("""
    Witaj w grze tekstowej przygotowanej specjalnie na potrzebe stworzenia odpowiedniego portfolio!
        Aby zagrać wystarczy tylko klawiatura (a w szczegolnośi 3 przyciski :/)
""")
print()
time.sleep(1)
print('No dobra z enterem 4...')
time.sleep(1.5)
name=input("Na początek proszę podaj swoje imię: ")
time.sleep(1)
print()
print(f'Witaj {name.capitalize()} ')
print()

# przygotowanie zmiennych do rozpoczęcia gry

licznik=0
time.sleep(1)
answer=None
exit=False

# samo rozpoczecie gry

while not exit:
    try:
        while True:
            answer=str(input(f'A więc {name.capitalize()} aby rozpocząć grę wciśnij "W" : '))
            licznik+=1
            if answer.upper()=="W" and licznik < 2:
                time.sleep(1)
                print('A więc zaczynajmy!')
                exit=True
                break
            elif answer.upper()=="W" and licznik > 2 :
                time.sleep(1)
                print('A więc teraz możemy zacząć!')
                exit = True
                break
            elif answer.upper()=='W' and licznik > 3 :
                time.sleep(1)
                print('A wiec zaczynamy!')
                exit = True
                break
            elif licznik > 5:
                time.sleep(1)
                print('zacznijmy po prosty...')
                exit = True
                break
            elif answer.isdigit():
                raise ValueError
    except:
        print('Używamy tylko liter :/')
        time.sleep(1)
print('A wiec wyobraź sobie ze jesteś w lesie, las jest ogromny! \n A ty stoisz sam/sama pośród drzew...')

time.sleep(1)

print('W oddali widzisz niedzwiedzi...')
time.sleep(1)
exit = False
counter = 0
while not exit:
    try:
        while True:
            time.sleep(1)
            answer = input('Co zrobisz? ("U" aby uciekać! "Z" aby zostać i walczyć z niedzwiedziem o terytorium!: ')
            counter+=1
            if answer.isdigit():
                raise ValueError
            elif answer.upper()=='U' and counter == 1:
                print('Właśnie dałeś/aś rade uciec niedźwiedziowi!')
                print()
                exit=True
                break
            elif answer.upper()=='U' and counter < 3:
                print('ufff, mało brakowało')
                time.sleep(1)
                print('Ale ostatecznie udało ci sie uciec! ')
                print()
                exit=True
                break
            elif answer.upper() == 'U' and counter < 5 :
                print('Woooow, było naprawde blisko!')
                time.sleep(1)
                print('Ale całe szczęście udało ci się uciec!')
                print()
                exit=True
                break
            elif answer.upper() == 'U' and counter < 7:
                print('nie wiem jak ale udało ci sie uciec')
                time.sleep(1)
                print('ktoś tu chyba jest dzieckiem szczęścia...')
                exit=True
                break
            elif answer.upper() == 'U' and counter < 10:
                print('no w końcu...')
                time.sleep(1)
                print('udało sie uciec jakimś cudem...')
                print()
                exit = True
                break
            elif answer.upper()=='Z' and counter == 1:
                print("WOW! ale jesteś odważny/odważna, ale może jednak uciekniesz?")
                print()
                time.sleep(1)
            elif answer.upper() == 'Z' and counter == 2:
                print('chyba pomyliłeś/aś "Z" z "U" spróbuj jeszcze raz!')
                print()
                time.sleep(1)
            elif answer.upper() == 'Z' and counter == 3:
                print('no no ktoś tu odważnego zgrywa...')
                print()
                time.sleep(1)
            elif answer.upper() == 'Z' and counter == 4:
                print('po prostu uciekaj!')
                print()
                time.sleep(1)
            elif answer.upper() == 'Z' and counter == 5:
                print('o.O')
                print()
                time.sleep(1)
            elif answer.upper()=='Z' and counter > 5 and counter < 8:
                time.sleep(1)
            elif counter == 8:
                print('bez internetu to chociaż tylko rodzina wiedziała...')
                print()
                time.sleep(2)
                print('idź dalej po prostu...')
                print()
                time.sleep(1)
                exit=True
                break
    except:
        print('No literki....')
total= counter + licznik
print()
if total < 3:
    print(f'BRAWO {name.upper()}!')
    time.sleep(0.5)
    print(f'Twój wynik to {total} !')
    time.sleep(0.5)
    print('Mam nadzieje że zobaczymy sie jeszcze raz!')
elif total < 5:
    print(f'BRAWO {name.upper()}!')
    time.sleep(0.5)
    print(f'Twój wynik to {total} !')
    time.sleep(0.5)
    print('Nastepnym razem uda ci sie zdobyć lepszy wynik!')
elif total < 8:
    print(f'BRAWO {name.upper()}!')
    time.sleep(0.5)
    print(f'Twój wynik to {total} !')
    time.sleep(0.5)
    print('Ale postaraj sie poprawić :/')
elif total < 13:
    print(f'prawdziwy as z ciebie {name.upper()}...')
    time.sleep(1)
    print(f'twój wynik to {total}')
    time.sleep(0.5)
    print('kiedyś się uda... ')
    time.sleep(1)
    print('wierze...')
elif total==14:
    print('...')
    time.sleep(2)
    print('po prostu idź...')
