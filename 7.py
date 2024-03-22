N, K, M = map(int, input().split())
a = abs(M-K)-1
b = N-a-2
if a >= b:
    print (b)
else:
    print (a)