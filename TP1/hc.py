import math
import random


def evaluate(x,y):
    return x**2

def tweak(limits, v, r):
    n = -1000000
    for i in range(len(v)):
        while(not(limits[i][0] <= n + v[i] and n + v[i] <= limits[i][1])):
            n = random.uniform(-r[i], r[i])
        v[i] = v[i] + n
    return v

limits = [[0, 10],[0,0]] #linha 1 = limites de x, linha2 = limite de y. Coluna 0 = limite inf; Coluna 1 = limite sup

v = [0, 0]
for i in range(len(limits)):
    r = random.uniform(0, 1)
    v[i] = (limits[i][1] - limits[i][0]) * r + limits[i][0]
solution = evaluate(v[0], v[1])
rate = 2
r = [(limits[0][1] - limits[0][0])/rate, (limits[1][1] - limits[1][0])/rate]
for i in range(1000):
    tenta = tweak(limits, v, r)
    result = evaluate(v[0], v[1])
    if result < solution:
        solution = result
        v = tenta

f = open("sol2b.txt", "a")
saida = str(v[0]) + ", " + str(v[1]) + ", " + str(solution) + "\n"
print(saida)
#f.write(saida)
f.close()
