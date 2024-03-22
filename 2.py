xc, yc, r, x, y = map(int, input().split())
a = abs(x - xc)
b = abs(y - yc)
d = a**2 + b**2
if d < (r**2):
    print('внутри окружности')
elif d == (r**2):
    print("на окружности")
elif d > (r**2):
    print('вне окружности')