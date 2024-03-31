
    #Program polega na utworzeniu paru funkcji działających
    #na prawdziwym pliku .txt z użyciem Regular expression

#import Regular expression
import re

#Otwarcie pliku .txt
with open('C:\\Users\\mlawn\\Desktop\\lista_mail.txt', 'r') as file:
    list = file.read()

#Funkcja ma za zadanie sprawdzenie czy podany mail jest
#w pliku
def check_mail(mail):

    if mail in list:
        print('Mail w bazie maili')
    else:
        print('Nie ma go w bazie!')

#Funkcja ma za zadanie, dodanie nowego maila do pliku
def add_mail(mail):

    with open('C:\\Users\\mlawn\\Desktop\\lista_mail.txt', 'a') as file:
        list = file.write('\n' + mail)

#Funkcja wypisuje maile, z podaną domeną
def mail_domain(domain):

    list_2 = []
    splited_list = re.split(r'\r?\n',list)
    for i in splited_list:
        index = i.find('@')
        if i[index + 1:] == domain:
            list_2.append(i)
    print('\n'.join(list_2))

#Funkcja usuwa podane maile
def remove_mail(mail_to_remove):

    try:
        splited_list = re.split(r'\r?\n',list)
        list_2 = [i for i in splited_list]
        list_2.remove(mail_to_remove)
        ultimate_list = '\n'.join(list_2)

        with open('C:\\Users\\mlawn\\Desktop\\lista_mail.txt', 'w') as file:
            file.write(ultimate_list)
    except:
        print('Mail już został usunięty lub go w ogóle nie było :)')


    #Przugotowane funkcję gotowe do użycia :)

#add_mail('kacpi12@gmail.com')

#check_mail('ula.wil12@op.pl')

#mail_domain('gmail.com')

#remove_mail('jawor@onet.pl')

#print(list)