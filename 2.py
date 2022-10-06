Katet1 = int(input('Введите катет:'))
Katet2 = int(input('Введите катет:'))
Gipotenuza = int(input('Введите гипотенузу:'))
Perimetr = Katet1+Katet2+Gipotenuza
if Katet1+Katet2>Gipotenuza:
    print('Uипотенуза не может быть меньше суммы двух катетов')
else:
    print('Площадь равна:', (Katet1*Katet2)/2)
    print('Периметр равен:', Perimetr)
