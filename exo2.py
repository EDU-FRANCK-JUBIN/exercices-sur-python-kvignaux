nb = int(input("Entrée un nombre: "))
if (nb < 3):
    print("Aucun, il est premier")


resPremiers = []

for i in range(2, nb):
    if(nb % i == 0):
        resPremiers.append(i)


if len(resPremiers) == 0:
    print("Aucun, il est premier")
else:
    print("Diviseur propres sans repetition : " + str(resPremiers))
