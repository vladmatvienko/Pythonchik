Kolexpon = int(input('Количество экспонатов:'))
Vn1e = 5 #Время на один экспонат
Mvd = 8*60 #Минут в день
Exponday = int(Mvd/Vn1e) #Экспонатов в день
Chel = int(input('Количество лет человека: '))
Chel1 = Chel
Vchel = 0 #Сколько дней жил человек
Vsego = 0 #Кол-во экспонатов просмотренное человеком
while Chel>0:
    if Chel%4==0:
        Vchel += 366 # Високосный год
        Chel -= 1
    else:
        Vchel = Vchel+365 # Обычный год
        Chel -= 1
while Vchel>0:
        Vchel -= 1
        Vsego += Exponday
print('Количество лет понадобившееся для просмотра', Kolexpon, 'экспонатов:', (Kolexpon/Exponday/365))
print('Максимально количество экспонатов, которое увидел человек за', Chel1,  'лет:', Vsego)


    
    
    
