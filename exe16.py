area=float(input('Enter the size of area to be painted: '));
liters=0;
while True:
    if area <= 0:
        break
    else:
        area -= (3*18)
        liters +=1;
print(f'your will need of {liters} cans of ink');
print(f'tho price: {liters*80}');