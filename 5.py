weight = float(input('Вес человека (в фунтах) - ')) / 2.205
height = float(input('Рост человека (в дюймах) - ')) * 2.54 / 100
IMT = round(weight/(height ** 2), 2)
print(weight, height, IMT)
if IMT < 16:
    print('Выраженный дефицит массы тела')
elif 16 <= IMT <= 18.49:
    print('Недостаточная масса тела')
elif 18.5 <= IMT <= 24.99:
    print('Норма')
elif 25 <= IMT <= 29.99:
    print('Избыточная масса тела')
elif 30 <= IMT <= 34.99:
    print('Ожирение первой степени')
elif 30 <= IMT <= 34.99:
    print('Ожирение второй степени')
elif IMT >= 40:
    print('Ожирение третьей степени')