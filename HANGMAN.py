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

# while True:
#     if len(slowo) >= 2:
#         druga_litera = input("Podaj drugą literę: ")
#         break
# print("Brawo zgadles!")
#
# if druga_litera in slowo:
#     indeks = [i for i, litera in enumerate(slowo) if litera == druga_litera]
#     for i in indeks:
#         oznaczenie = oznaczenie[:i] + druga_litera + oznaczenie[i+1:]
#     print(oznaczenie)
# else:
#     print("Ta litera się nie znajduje. Straciłeś jedno życie!")
#
#
# while True:
#     if len(slowo) >= 3 and "_" in oznaczenie:
#         trzecia_litera = input("Podaj trzecia literę: ")
#         break
# print("Brawo zgadles!")
#
# if trzecia_litera in slowo:
#     indeks = [i for i, litera in enumerate(slowo) if litera == trzecia_litera]
#     for i in indeks:
#         oznaczenie = oznaczenie[:i] + trzecia_litera + oznaczenie[i+1:]
#     print(oznaczenie)
# else:
#     print("Ta litera się nie znajduje. Straciłeś jedno życie!")
#
#
# while True:
#     if len(slowo) >= 4 and "_" in oznaczenie:
#         czwarta_litera = input("Podaj czwarta literę: ")
#         break
# print("Brawo zgadles!")
#
# if czwarta_litera in slowo:
#     indeks = [i for i, litera in enumerate(slowo) if litera == czwarta_litera]
#     for i in indeks:
#         oznaczenie = oznaczenie[:i] + czwarta_litera + oznaczenie[i+1:]
#     print(oznaczenie)
# else:
#     print("Ta litera się nie znajduje. Straciłeś jedno życie!")
#
# while True:
#     if len(slowo) >= 5:
#         piata_litera = input("Podaj piata literę: ")
#         break
# print("Brawo zgadles!")
#
# if piata_litera in slowo:
#     indeks = [i for i, litera in enumerate(slowo) if litera == piata_litera]
#     for i in indeks:
#         oznaczenie = oznaczenie[:i] + piata_litera + oznaczenie[i+1:]
#     print(oznaczenie)
# else:
#     print("Ta litera się nie znajduje. Straciłeś jedno życie!")
#
# while True:
#     if len(slowo) >= 6:
#         szosta_litera = input("Podaj szosta literę: ")
#         break
# print("Brawo zgadles!")
#
# if szosta_litera in slowo:
#     indeks = [i for i, litera in enumerate(slowo) if litera == szosta_litera]
#     for i in indeks:
#         oznaczenie = oznaczenie[:i] + szosta_litera + oznaczenie[i+1:]
#     print(oznaczenie)
# else:
#     print("Ta litera się nie znajduje. Straciłeś jedno życie!")
#
# while True:
#     if len(slowo) >= 7:
#         siodma_litera = input("Podaj siodma literę: ")
#         break
# print("Brawo zgadles!")
#
# if siodma_litera in slowo:
#     indeks = [i for i, litera in enumerate(slowo) if litera == siodma_litera]
#     for i in indeks:
#         oznaczenie = oznaczenie[:i] + siodma_litera + oznaczenie[i+1:]
#     print(oznaczenie)
# else:
#     print("Ta litera się nie znajduje. Straciłeś jedno życie!")
#
# while True:
#     if len(slowo) >= 8:
#         osma_litera = input("Podaj osma literę: ")
#         break
# print("Brawo zgadles!")
#
# if osma_litera in slowo:
#     indeks = [i for i, litera in enumerate(slowo) if litera == osma_litera]
#     for i in indeks:
#         oznaczenie = oznaczenie[:i] + osma_litera + oznaczenie[i+1:]
#     print(oznaczenie)
# else:
#     print("Ta litera się nie znajduje. Straciłeś jedno życie!")
#
# while True:
#     if len(slowo) >= 9:
#         dziewiata_litera = input("Podaj dziewiata literę! Świetnie ci idzie!: ")
#         break
# print("Brawo zgadles !")
#
# if dziewiata_litera in slowo:
#     indeks = [i for i, litera in enumerate(slowo) if litera == dziewiata_litera]
#     for i in indeks:
#         oznaczenie = oznaczenie[:i] + dziewiata_litera + oznaczenie[i+1:]
#     print(oznaczenie)
# else:
#     print("Ta litera się nie znajduje. Straciłeś jedno życie!")
#
# while True:
#     if len(slowo) >= 10:
#         dziesiata_litera = input("Podaj dziesiata literę! Jestes coraz blizej!: ")
#         break
# print("Brawo zgadles!")
#
# if dziesiata_litera in slowo:
#     indeks = [i for i, litera in enumerate(slowo) if litera == dziesiata_litera]
#     for i in indeks:
#         oznaczenie = oznaczenie[:i] + dziesiata_litera + oznaczenie[i+1:]
#     print(oznaczenie)
# else:
#     print("Ta litera się nie znajduje. Straciłeś jedno życie!")
#
# while True:
#     if len(slowo) >= 11:
#         jedenasta_litera = input("Podaj jedenasta literę: ")
#         break
# print("Brawo zgadles!")
#
# if jedenasta_litera in slowo:
#     indeks = [i for i, litera in enumerate(slowo) if litera == jedenasta_litera]
#     for i in indeks:
#         oznaczenie = oznaczenie[:i] + jedenasta_litera + oznaczenie[i+1:]
#     print(oznaczenie)
# else:
#     print("Ta litera się nie znajduje. Straciłeś jedno życie!")
#
# while True:
#     if len(slowo) >= 12:
#         dwunasta_litera = input("Podaj dwunasta literę: ")
#         break
# print("Brawo zgadles!")
#
# if dwunasta_litera in slowo:
#     indeks = [i for i, litera in enumerate(slowo) if litera == dwunasta_litera]
#     for i in indeks:
#         oznaczenie = oznaczenie[:i] + dwunasta_litera + oznaczenie[i+1:]
#     print(oznaczenie)
# else:
#     print("Ta litera się nie znajduje. Straciłeś jedno życie!")
#
# while True:
#     if len(slowo) >= 13:
#         trzynasta_litera = input("Podaj trzynasta literę: ")
#         break
# print("Brawo zgadles!")
#
# if trzynasta_litera in slowo:
#     indeks = [i for i, litera in enumerate(slowo) if litera == trzynasta_litera]
#     for i in indeks:
#         oznaczenie = oznaczenie[:i] + trzynasta_litera + oznaczenie[i+1:]
#     print(oznaczenie)
# else:
#     print("Ta litera się nie znajduje. Straciłeś jedno życie!")
#
# while True:
#     if len(slowo) >= 14:
#         czternasta_litera = input("Podaj czternasta literę: ")
#         break
# print("Brawo zgadles!")
#
# if czternasta_litera in slowo:
#     indeks = [i for i, litera in enumerate(slowo) if litera == czternasta_litera]
#     for i in indeks:
#         oznaczenie = oznaczenie[:i] + czternasta_litera + oznaczenie[i+1:]
#     print(oznaczenie)
# else:
#     print("Ta litera się nie znajduje. Straciłeś jedno życie!")
#
# while True:
#     if len(slowo) >= 15:
#         pietnasta_litera = input("Podaj trzecia literę: ")
#         break
# print("Brawo zgadles!")
#
# if pietnasta_litera in slowo:
#     indeks = [i for i, litera in enumerate(slowo) if litera == pietnasta_litera]
#     for i in indeks:
#         oznaczenie = oznaczenie[:i] + pietnasta_litera + oznaczenie[i+1:]
#     print(oznaczenie)
# else:
#     print("Ta litera się nie znajduje. Straciłeś jedno życie!")