pin = input('Введите PIN-код:\n')
k = int(pin)
a = k // 1000
b = k // 100 % 10
c = k % 100 // 10
d = k % 10
if len(pin) == 4:
    if (k <= 1900) or (k >= 2050):
        if (a != b) and (a != c) and (a != d) and (b != c) and (b != d) and (c != d):
            print('OK')
        else:
            print('ERROR')
    else:
        print('ERROR')
else:
    print('ERROR')
