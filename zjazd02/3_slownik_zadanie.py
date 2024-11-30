# dany jest słownik produktów dostępnych w domu

dostepne = {'mleko' : 5, 'jajko' : 12, 'maka' : 4, 'maslo' : 2, 'woda' : 10}

# dany jest slownik produktow potrzebnych do upieczenia ciasta

ciasto = {'jajko' : 4, 'maka' : 0.5, 'maslo' : 0.6, 'mleko' : 0.1}

# program liczy ile ciast można upiec z dostępnych składników i pokaże krytyczny składnik

liczba_ciast = 9999
skladnik_krytyczny = ''

for skladnik in ciasto:
    if dostepne[skladnik] // ciasto[skladnik] < liczba_ciast:
        liczba_ciast = dostepne[skladnik] // ciasto[skladnik]

print(liczba_ciast)