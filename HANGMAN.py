import sys
wisielec = input("Podaj słowo do odgadnięcia!: ")
print("Uwazaj masz tylko 5 zyc !")
if isinstance(wisielec, str):
    slowo = wisielec
    dlugosc = len(slowo)
    oznaczenie = "_" * dlugosc

print(oznaczenie)

licznik_zycia = 5

while True:
    if len(slowo) >= 1:
        pierwsza_litera = input("Podaj litere!: ")

    if pierwsza_litera in slowo:
        indeks = [i for i, litera in enumerate(slowo) if litera == pierwsza_litera]
        for i in indeks:
            oznaczenie = oznaczenie[:i] + pierwsza_litera + oznaczenie[i+1:]
        print(oznaczenie)
        print("Brawo, zgadles!")
    else:
        print("Takiej litery nie ma!. Straciłeś jedno życie!")
        licznik_zycia -= 1
        print("Twoja aktualna liczba zyc to!:" + str(licznik_zycia))

    if oznaczenie == slowo:
        print("Gratulacje, odgadłeś słowo!")
        break

    if licznik_zycia == 0:
        print("Straciłeś wszystkie życia. Koniec gry!")
        break
