n, m, k = map(int, input().split())
if (n >= m) and (m >= k):
    print(n, m, k)
elif (n >= k) and (k >= m):
    print(n, k, m)
elif (m >= n) and (n >= k):
    print(m, n, k)
elif (m >= k) and (k >= n):
    print(m, k, n)
elif (k >= n) and (n >= m):
    print(k, n, m)
elif (k >= m) and (m >= n):
    print(k, m, n)
