first, second, third = map(int, input().split())
if (first == second) and (second == third):
    print(3)
elif (first == second) or (second == third) or (first == third):
    print(2)
elif (first != second) and (second != third):
    print(0)