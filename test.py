a = [-1, -2,  1, 2,-3, 3, 4, 5, 6, 7, 8, 9]
for x in a[:]:
    if x > 0:
        a.pop()

print(a)


def fun(a: int, b: dict):  # typescript
    print(a, b)

