'''
            Ulepszony szyfr Cezara!
            Program ma za zadanie zaszyfrować wpisany tekst.
            Litery na parzystych pozycjach są przesuwane o +2,
            a litery na nieparzystych pozycjach są przesuwane o +1,
            (numer pozycji liczę [1,2,3,4], a nie [0,1,2,3],
            jeżeli chcemy zmienić sposób liczenia pozycji to w linijce 13
            przy argumencie start wartość zmieniamy na 1,a w linijce 19 i 25 przy modulo zmieniamy 2 na 1)
            w stosunku do tabeli ascii.
'''
def encryption(text):
    list_cipher = []

    for i, char in enumerate(text, start=0):
        # Sprawdzenie, czy znak jest literą
        if char.isalpha():
            # Sprawdzenie, czy to jest mała czy duża litera
            if char.islower():
                # Szyfrowanie dla małej litery
                if i % 2 == 0:
                    list_cipher.append(chr((ord(char) - ord('a') + 1) % 26 + ord('a')))
                else:
                    list_cipher.append(chr((ord(char) - ord('a') + 2) % 26 + ord('a')))
            else:
                # Szyfrowanie dla dużej litery
                if i % 2 == 0:
                    list_cipher.append(chr((ord(char) - ord('A') + 1) % 26 + ord('A')))
                else:
                    list_cipher.append(chr((ord(char) - ord('A') + 2) % 26 + ord('A')))
        else:
            # Zostawienie niezmienionych znaków, które nie są literami
            list_cipher.append(char)

    # Połączenie zaszyfrowanych znaków w jeden tekst
    encrypted_text = ''.join(list_cipher)
    return encrypted_text


def decryption(text):
    list_cipher = []

    for i, char in enumerate(text, start=0):
        # Sprawdzenie, czy znak jest literą
        if char.isalpha():
            # Sprawdzenie, czy to jest mała czy duża litera
            if char.islower():
                # Deszyfrowanie dla małej litery
                if i % 2 == 0:
                    list_cipher.append(chr((ord(char) - ord('a') - 1) % 26 + ord('a')))
                else:
                    list_cipher.append(chr((ord(char) - ord('a') - 2) % 26 + ord('a')))
            else:
                # Deszyfrowanie dla dużej litery
                if i % 2 == 0:
                    list_cipher.append(chr((ord(char) - ord('A') - 1) % 26 + ord('A')))
                else:
                    list_cipher.append(chr((ord(char) - ord('A') - 2) % 26 + ord('A')))
        else:
            # Zostawienie niezmienionych znaków, które nie są literami
            list_cipher.append(char)

    # Połączenie odszyfrowanych znaków w jeden tekst
    decrypted_text = ''.join(list_cipher)
    return decrypted_text

while True:

    question = input(" 1.Zaszyfrowanie  2.Odszyfrowanie\n"
                    "              1 czy 2? \n"
                     "                 ")

    try:
        if question == "1":
            text_to_encrypt = input("Podaj tekst do zaszyfrowania: ")
            encrypted_text = encryption(text_to_encrypt)
            print(encrypted_text)
            break

        elif question == "2":
            text_to_decrypt = input("Podaj tekst do odszyfrowania: ")
            decrypted_text = decryption(text_to_decrypt)
            print(decrypted_text)
            break


    except:
        if question != '1' or '2':
            raise ValueError


