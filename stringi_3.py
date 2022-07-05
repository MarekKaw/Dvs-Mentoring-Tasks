imie = input("Podaj swoje imię: ")

print("Cześć {}! ".format(imie))
wiek = input("Podaj proszę swój wiek: ")
kraj = input("W jakim kraju mieszkasz? ")
print("{}, czyli mieszkasz w kraju o nazwie {} i masz {} lata. ".format(imie, kraj, wiek))
czyPoprawnie = input("Czy dane są zapisane poprawnie? Napisz tak lub nie: ")
if czyPoprawnie == "tak":
    print("Zapisujemy Twoje dane")

else:
    print("Wprowadź dane od początku")
