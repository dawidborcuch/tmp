NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# suma = zbior1 | zbior2
# przeciecie = zbior1 & zbior2
# roznica = zbior1 - zbior2
# roznica_symetryczna = zbior1 ^ zbior2

# sprawdźmy ile osób chorowało w ostatnim roku na krzykach
print(chorzy_rok & krzyki)

# sprawdź ile osób z krzyków chorowało w ostatnim roku
print(krzyki & chorzy_rok)

# sprawdź ile osób chorowalo w ostatnim miesiacu w centrum
print(centrum & chorzy_miesiac)

# sprawdz ile osób mieszka w sumie w centrum i na krzykach
print(centrum | krzyki)

# pesele żeńskie mają ostatnią cyfrę parzystą, męskie - nieparzystą
# zrób nowe zbiory dla kobiet i mężczyzn w NFZ

pesele_meskie = set()
pesele_zenskie = set()

for pesel in NFZ:
    if float(pesel) % 2 == 0:
        pesele_zenskie.add(pesel)
    if float(pesel) % 2 != 0:
        pesele_meskie.add(pesel)


print(pesele_zenskie)
print(pesele_meskie)

# usuwanie duplikatów
lista = [1,2,3,1,2,3]
print(list(set(lista)))