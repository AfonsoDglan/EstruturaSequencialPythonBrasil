need = float(input('Enter the need of file in MB: '));
velocity = float(input('Enter the velocity of internet in Mbps: '));
time = need/ (velocity/8);
print(f'The time of download will be {time}s');
