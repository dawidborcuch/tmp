# dane = ['imie', 'nazwisko', 'wiek']
#
# for dana in dane:
#     name = input(f'Podaj {dana}: ')
#
# print(name)



# dane = input('Podaj dane: ').split()
# print(dane)

# program, który przyjmie dane dla X pracowników
# program zwraca słownik {id : słownik danych}

liczba_pracownikow = int(input("Podaj liczbę pracowników: "))
pracownicy = {}

for i in range(1, liczba_pracownikow + 1):
    print(f"\nWprowadzanie danych dla pracownika {i}:")
    imie = input("Imię: ")
    nazwisko = input("Nazwisko: ")
    wiek = int(input("Wiek: "))
    stanowisko = input("Stanowisko: ")
    wynagrodzenie = float(input("Wynagrodzenie: "))

    pracownicy[i] = {
        "imie": imie,
        "nazwisko": nazwisko,
        "wiek": wiek,
        "stanowisko": stanowisko,
        "wynagrodzenie": wynagrodzenie
    }

print(pracownicy)

