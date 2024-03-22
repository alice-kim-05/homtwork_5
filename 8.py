N = int(input())
galleon = N // (17 * 29)
sikl = (N - (galleon * 17 * 29)) // 29
knat = N - (galleon * 17 * 29) - (sikl * 29)
if galleon > 0:
    print(galleon, 'галлеонов')
if sikl > 0:
    print(sikl, 'сиклей')
if knat > 0:
    print(knat, 'кнатов')
