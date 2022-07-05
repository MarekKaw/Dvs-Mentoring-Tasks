# czyPoprawnie = "nie"
flag = True
while True:
    imie = input("Podaj swoje imię: ")
    print("Cześć {}! ".format(imie))
    wiek = int(input("Podaj proszę swój wiek: "))
    kraj = input("W jakim kraju mieszkasz? ")
    print("{}, czyli mieszkasz w kraju o nazwie {} i masz {} lata. ".format(imie, kraj, wiek))
    czyPoprawnie = input("Czy dane są zapisane poprawnie? Napisz tak lub nie: ")
    if czyPoprawnie == "nie":
        print("Wprowadź dane od początku")
    elif czyPoprawnie == "tak":
        print("Zapisujemy Twoje dane")
        #flag = False
        break
