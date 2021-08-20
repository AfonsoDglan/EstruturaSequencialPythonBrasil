area=float(input('Enter the size of area to be painted: '));
area += area * (10/100);
area2 = area;
area3 = area;
liters_1=0;
while True:
    if area <= 0:
        break
    else:
        area -= (6*18)
        liters_1 +=1;
print(f'Comprar apenas latas de 18 litros: {liters_1}');
print(f'Comprar apenas latas de 18 litros preço: {liters_1*80}');
liters_2=0
while True:
    if area2 <= 0:
        break
    else:
        area2 -= (6*3.6)
        liters_2 += 1;
print(f'Comprar apenas latas de 3,6 litros: {liters_2}');
print(f'Comprar apenas latas de 3,6 litros preço: {liters_2*25}');
liters_3=0
latas=0;
while True:
    if area3 <= 0:
        break;
    elif area3 > (6*18):
        area3 -= (6*18);
        liters_3 += 1;
    else:
        area3 -= (6*3.6);
        latas += 1;
print(f'misturar latas e galões, {liters_3} latas de 18 litros e {latas} latas de 3,6 litros');
print(f'Preço: {(liters_3*80)+(latas*25)}');

