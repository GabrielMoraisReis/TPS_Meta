import random
import copy
class individuo:
    def __init__(self, x, y, value) -> None:
        self.x = x #valor de x
        self.y = y #valor de y
        self.value = value #valor quando colocado substituido na função objetivo
        self.fitness = 0

def evaluate(x1, x2):
    return (x1 - 10)**3 + (x2-20)**3

def calcula_restricao_func(x1, x2):
    g1 = -(x1 -5)**2 - (x2-5)**2 + 100
    g2 = (x1 - 6)**2 + (x2-5)**2 - 82.81
    if g1 <= 0 and g2 <= 0:
        return True
    return False

def cria_individuo():
    x1 = random.uniform(-50, 100)
    x2 = random.uniform(-100, 50)
    while not calcula_restricao_func(x1, x2):
        x1 = random.uniform(-50, 100)
        x2 = random.uniform(-100, 50)
    return x1, x2

def fitness_calc(individuos):
    fitness = []
    nota = 0
    for indiv in individuos:
        if (calcula_restricao_func(indiv.x, indiv.y)):
            indiv.fitness = indiv.value
        else:
            if indiv.value <= 0:
                indiv.fitness = indiv.value*0.01 #diminui a probabilidade de valores que não respeitam restrições serem escolhidos
            else:
                indiv.fitness = indiv.value/0.01 #diminui a probabilidade de valores que não respeitam restrições serem escolhidos
    return individuos

# def propFitnessSelection(individuos):
#     fitness_calc(individuos)
#     numIndividuosSelecao = round(len(individuos)/2)
#     T = 0
#     S = 0
#     newPopu = []
#     count = 0
#     iteration = 0
#     for individuo in individuos:
#         T = T + individuo.fitness
#     while iteration<len(individuos) and count < numIndividuosSelecao:
#         #print("aaaaaaaaaaaaaaaaaaaaaa" + str(T))
#         if T < 0:
#             r = random.randint(round(T), 0)
#         else:
#             r = random.randint(0,round(T))
#         S = individuos[iteration].value + S
#         if(S <= r):
#             newPopu.append(copy.deepcopy(individuos[iteration]))
#             count += 1
#         iteration += 1

#     return newPopu

def tournmentSelection(popu):
    tam_new_pop = 200
    new_pop = []
    winner = None
    fitness_calc(popu)
    for i in range(tam_new_pop):
        x1 = popu[random.randint(0,len(popu)-1)]
        x2 = popu[random.randint(0,len(popu)-1)]
        if x1.fitness == x2.fitness:
            one_or_two = random.randint(0,1)
            if one_or_two == 0:
                winner = x1
            else:
                winner = x2
        elif x1.fitness > x2.fitness:
            winner = x2
        else:
            winner = x1
        new_pop.append(winner)
    return(new_pop)

def discrete_crossing(mom, dad):
    indivs = []
    cromossomo = []
    for i in range(2):
        for j in range(2):
            p = random.randint(0, 1) #p = 0 pega gene da mãe, p = 1 pega gene do pai
            if p == 0 and j == 0:
                x1 = mom.x
                #print("X1 mom")
            elif p == 1 and j == 0:
                x1 = dad.x
                #print("x1 dad")
            elif p == 0 and j == 1:
                x2 = mom.y
                #print("x2 mom")
            elif p == 1 and j == 1:
                x2 = dad.y
                #print("x2 dad")
        indivs.append(individuo(x1, x2, 0))
    return indivs[0], indivs[1]

def uniformMutation(individuos):
    p = 0.05 #probabilidade de adicionar ruído à um elemento do vetor, normalmente entre 0,1 e 5%
    v = []
    newPopu = []
    for indivi in individuos:
        randomNumber = random.uniform(0,1)
        if(p >= randomNumber):
            vX = random.uniform(0, 1)*(100-(-50))*(2*random.uniform(0, 1)-1)
            vY = random.uniform(0, 1)*(50-(-100))*(2*random.uniform(0, 1)-1)
            value = evaluate(indivi.x + vX, indivi.y + vY)
            indivi = individuo(indivi.x + vX, indivi.y + vY, value)
    return individuos


tam_pop_init = 200
popu =[]
for i in range(tam_pop_init):
    x1, x2 = cria_individuo()
    value = evaluate(x1, x2)
    popu.append(individuo(x1, x2, value))

#print(popu)
temp_popu = []
num_iter = 1000
for i in range(1000):
    temp_popu = tournmentSelection(popu).copy()

    for j in range(0, len(temp_popu)-2, 2):
        #print("Len", len(temp_popu))
        #print("J", j)
        temp_popu[j], temp_popu[j+1] = discrete_crossing(temp_popu[j], temp_popu[j+1])
        #print("Len 2", len(temp_popu))
        temp_popu = uniformMutation(temp_popu)
        #print("Len 3", len(temp_popu))
        for indiv in temp_popu:
            indiv.value = evaluate(indiv.x, indiv.y)
        #print("Len 4", len(temp_popu))
    popu = temp_popu.copy()

best = popu[0]
for person in popu:
    if person.value < best.value and calcula_restricao_func(person.x, person.y):
        best = person

#print("A melhor configuracao e x1= {}; x2 = {}; resultado = {}".format(best.x, best.y, best.value))

f = open("sol1b.txt", "a")
saida = str(best.x) + ", " + str(best.y) + ", " + str(best.value) + "\n"
#print(saida)
f.write(saida)
f.close()