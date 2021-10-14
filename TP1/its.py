import math
import random

def evaluate(x,y):
    return math.sin(x+y) + pow(x-y, 2) - 1.5*x +2.5*y +1

def tweak(limits, v, r):
    n = -1000000
    for i in range(len(v)):
        while(not(limits[i][0] <= n + v[i] and n + v[i] <= limits[i][1])):
            n = random.uniform(-r[i], r[i])
        v[i] = v[i] + n
    return v

def hill(limits, v):
    solution = evaluate(v[0], v[1])
    rate = 5
    r = [(limits[0][1] - limits[0][0])/rate, (limits[1][1] - limits[1][0])/rate]
    for i in range(1000):
        tenta = tweak(limits, v, r)
        result = evaluate(v[0], v[1])
        if result < solution:
            solution = result
            v = tenta
    return (solution, v)

def pertuba(limits, v, r, visited):
    n = -1000000
    while(v in visited):
        for i in range(len(v)):
            while(not(limits[i][0] <= n + v[i] and n + v[i] <= limits[i][1])):
                n = random.uniform(-r, r)
            v[i] = v[i] + n
    return v

limits = [[-1.5, 4],[-3,4]] #linha 1 = limites de x, linha2 = limite de y. Coluna 0 = limite inf; Coluna 1 = limite sup
v = [None, None] #melhor combinação x,y

# gera solução inicial
for i in range(len(limits)):
    r = random.uniform(0, 1)
    v[i] = (limits[i][1] - limits[i][0]) * r + limits[i][0]

visited = [] #será usada para garantir que a busca local retorne uma solução numa bacia de atração já visitada.
visited.append(v)
solution = evaluate(v[0], v[1]) #melhor valor da função objetivo

#busca local s0
v_l = [None, None]
solution_l, v_l = hill(limits, v)
if solution_l < solution:
    solution = solution_l
    v = v_l
    visited.append(v)
print(v)
pertubation = 0.005 #número 
for i in range(50):
    v_l = pertuba(limits, v, pertubation, visited )
    print(v_l)
    visited.append(v_l)
    solution_l, v_l = hill(limits, v_l) #busca local
    if solution_l < solution: #criterio de aceitação
        solution = solution_l
        v = v_l
        visited.append(v)

#
f = open("sol2b.txt", "a")
saida = str(v[0]) + ", " + str(v[1]) + ", " + str(solution) + "\n"
print(saida)
#f.write(saida)
f.close()

