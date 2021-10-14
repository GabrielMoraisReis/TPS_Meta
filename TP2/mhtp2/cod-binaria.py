import numpy as np
import random
import copy

class individuo:
    def __init__(self, x, y, value) -> None:
        self.x = x #valor de x
        self.y = y #valor de y
        self.value = value #valor quando colocado substituido na função objetivo
        self.fitness = 0



# def numBits(precisao, limSup, limInf):
#     k = np.log2((limSup - limInf + 0.0001)/precisao)
#     print(k)
#     return k

# # def calc_precisao(maxX, minX, numBits):
# #     precisao = (maxX - minX)/(2**(numBits) - 1)
# #     return precisao

# def grayConverter(binaryString):
#     msb = binaryString[0] #most significant bit 
#     for i in range(len(teste)-1): #iterate through the entire binary
#         if(int(binaryString[i])^int(binaryString[i+1])): #XOR operation to calculate the next bit
#             msb = msb + '1'
#         else:
#             msb = msb + '0'
#     grayCode = msb
#     print(msb)
#     return grayCode

# def init_pop(l):
#     cromossomo = []
#     for i in l:
#         gene = []
#         for j in range(i):
#             gene.append(random.randint(0,1))
#         cromossomo.append(gene)
#     return cromossomo
        


    #numIndividuos = len(individuos
def evaluate(x1, x2):
    return (x1 - 10)**3 + (x2-20)**3

def calcula_restricao_func(x1, x2):
    g1 = -(x1 -5)**2 - (x2-5)**2 + 100
    g2 = (x1 - 6)**2 + (x2-5)**2 - 82.81
    if g1 <= 0 and g2 <= 0:
        return True
    return False

def cria_individuo():
    x1 = random.uniform(13, 100)
    x2 = random.uniform(0, 100)
    while not calcula_restricao_func(x1, x2):
        x1 = random.uniform(13, 100)
        x2 = random.uniform(0, 100)
    return x1, x2

def discrete_crossing(mom, dad):
    indivs = []
    cromossomo = []
    for i in range(2):
        for j in range(2):
            p = random.randint(0, 1) #p = 0 pega gene da mãe, p = 1 pega gene do pai
            if p == 0 and j == 0:
                x1 = mom.x
            elif p == 1 and j == 0:
                x1 = dad.x
            elif p == 0 and j == 1:
                x2 = mom.y
            elif p == 1 and j == 1:
                x2 = dad.y
        indivs.append(individuo(x1, x2, 0))
    return indivs[0], indivs[1]
    
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
                indiv.fitness = indiv.value/0.01
# tam_pop_init = 100
# popu =[]
# for i in range(tam_pop_init):
#     x1, x2 = cria_individuo()
#     value = evaluate(x1, x2)
#     popu.append(individuo(x1, x2, value))

# temp_popu = []

# for i in range(10000):
#     temp_popu = []
#     popu = propFitnessSelection(popu)
#     for j in range(len(popu) - 2, 2):
#         indiv1, indiv2 = discrete_crossing(popu[j], popu[j+1])
#         temp_popu.extend(indiv1, indiv2)
#         popu = uniformMutation(temp_popu)
#         for k in range(len(popu) - 1):
#             popu[k].value = evaluate(popu[k].x, popu[k].y)
        
#         #DEIXAMOS OS INDIVIDUOS QUE NÃO RESPEITAM AS RESTRIÇÕES VIVOS, POREM ELES NÃO SERÃO CONSIDERADOS NA SOLUÇÃO FINAL. ESTÃO PRESENTES PARA DAR VARIABILIDADE GENÉTICA



def propFitnessSelection(individuos):
    fitness_calc(individuos)
    numIndividuosSelecao = round(len(individuos)/2)
    T = 0
    S = 0
    newPopu = []
    for individuo in individuos:
        T = T + individuo.fitness
    for i in range(numIndividuosSelecao):
        print("aaaaaaaaaaaaaaaaaaaaaa" + str(T))
        r = random.randint(0,round(T))
        S = individuos[i].value + S
        if(S <= r):
            newPopu.append(copy.deepcopy(individuos[i]))
    return newPopu


def uniformMutation(individuos):
    p = 0.05 #probabilidade de adicionar ruído à um elemento do vetor, normalmente entre 0,1 
    v = []
    newPopu = []
    for individuo in individuos:
        randomNumber = random.uniform(0,1)
        if(p >= randomNumber):
            vX = random.uniform(0, 1)*(100-13)*(2*random.uniform(0, 1)-1)
            vY = random.uniform(0, 1)*(100-0)*(2*random.uniform(0, 1)-1)
            value = evaluate(individuo.x + vX, individuo.y + vY)
            newIndividuo = individuo(individuo.x + vX, individuo.y + vY, value)
            newPopu.append(copy.deepcopy(newIndividuo))
    return newPopu


# def def_prob(result_vec):
#     result_vec.sort()
#     prob_vec = []
#     prev = 1
#     casas = len(str(len(result_vec)))
#     rate = len(result_vec)/(10**(casas*2-2))
#     for i in range(result_vec):
#         prob_vec.append(prev - rate)
#         prev = prev - rate
    
tam_pop_init = 10
popu =[]
for i in range(tam_pop_init):
    x1, x2 = cria_individuo()
    value = evaluate(x1, x2)
    popu.append(individuo(x1, x2, value))

print(popu)

temp_popu = []

for i in range(10):
    popu = propFitnessSelection(popu)
    print(popu)
    for j in range(0, len(popu) - 2, 2):
        print(j)
        indiv1, indiv2 = discrete_crossing(popu[j], popu[j+1])
        popu.extend(indiv1, indiv2)
        print(popu)
        # popu = uniformMutation(temp_popu)
        # for k in range(len(popu) - 1):
        #     popu[k].value = evaluate(popu[k].x, popu[k].y)
        
        #DEIXAMOS OS INDIVIDUOS QUE NÃO RESPEITAM AS RESTRIÇÕES VIVOS, POREM ELES NÃO SERÃO CONSIDERADOS NA SOLUÇÃO FINAL. ESTÃO PRESENTES PARA DAR VARIABILIDADE GENÉTICA
