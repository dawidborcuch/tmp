

slownik_zakupow = {'marchew' : 3, 'ryz' : 5, 'woda' : 3}

print(slownik_zakupow['marchew'])
print(slownik_zakupow.values())

slownik_zakupow['serek'] = 4
slownik_zakupow['marchew'] += 1
print(slownik_zakupow)

for produkt in slownik_zakupow:
    print(f' chcesz kupić {produkt} w ilosci {slownik_zakupow[produkt]}')

for produkt in slownik_zakupow.keys():
    print(f' chcesz kupić {produkt} w ilosci {slownik_zakupow[produkt]}')

for cena in slownik_zakupow.values():
    print(cena)

for produkt, cena in slownik_zakupow.items():
    print(produkt, cena)