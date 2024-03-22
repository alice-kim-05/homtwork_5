number = int(input())
a = number // 1000
b = number % 10
c = number // 100 % 10
d = number % 100 // 10
if (a == b) and (c == d):
    print('настоящее')
else:
    print('кривое')