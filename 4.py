n = int(input())
if n % 10 == 0 or 5 <= n % 10 <= 9 :
    print(n, 'попугаев')
elif n == 11 or n == 12 or n == 13 or n == 14:
    print(n, 'попугаев')
elif 2 <= n % 10 <= 4:
    print(n, 'попугая')
elif n % 10 == 1:
    print(n, 'попугай')


