value_hours=float(input('Enter the value of hour of work:'));
work_hours=float(input('Enter the total of hours worked:'));
salary=value_hours*work_hours;
Imposto_renda=salary*(11/100);
inss = salary*(8/100);
sindicato = salary*(5/100);
print(f'+ Salário Bruto : R$ {value_hours*work_hours}');
print(f'- IR (11%) : R$ {Imposto_renda}');
print(f'- INSS (8%) : R$ {inss}');
print(f'- Sindicato ( 5%) : R$ {sindicato}');
print(f'= Salário Liquido : R$ {salary-(Imposto_renda+inss+sindicato)}');