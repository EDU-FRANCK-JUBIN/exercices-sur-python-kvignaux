import math
n = int(input("Entrée un nombre > 50 "))
res = 0
e = 2.71828182845904523536
if n > 50:
    for k in range(0, n):
        res += 1/(math.factorial(n))
        print(res)
    print({res, e-res})
else:
    print("le nombre doit etre > 50")
