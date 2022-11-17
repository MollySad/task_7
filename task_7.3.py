rates = {'Sberbank': 55.8, 'VTB24': 53.91, 'Alphabank': 61}
min = 0

for kurs in rates.values():
    if min == 0 or kurs < min:
        min = kurs

for bank, kurs in rates.items():
    if kurs == min:
        print(f'{bank} -> {kurs}')