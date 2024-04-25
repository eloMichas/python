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


text_to_encrypt = input("Podaj tekst do zaszyfrowania: ")
encrypted_text = encryption(text_to_encrypt)
print("Zaszyfrowany tekst:", encrypted_text)
