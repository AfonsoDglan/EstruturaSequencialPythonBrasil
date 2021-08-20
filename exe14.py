weigth_fish=float(input('Enter the weight total of fishes: '));
excess = weigth_fish - 50;
mulct = 4 * excess;
if excess < 0:
    print('Not there was excess');
else:
    print(f'Escess => {excess}');
    print(f'mulct => {mulct}');