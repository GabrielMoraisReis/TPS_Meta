import random
import math
from copy import deepcopy

#PD é a demanda de carga total (em MW)
# PL são as perdas de transmissão (em MW)

#G=800 gerações
#μ = 1 indivíduo
#λ = 30 indivíduos

#ou seja para cada pai deve-se produzir 30 filhos

#===== usar na equação 13 e 14 =====
#q1=500 
#q2=50
#===== usar na equação 13 e 14 =====

#seguindo essa lógica temos 13 unidades geradoras e cada uma deve ser executada com suas configurações, portanto cada unidade geradora gerará 30 filhos

class gerador:
    def __init__(self, valuep, minp, maxP, a, b, c, d, e, f) -> None:
        self.valueP = 0 #valor quando colocado substituido na função objetivo
        self.minP = 0 
        self.maxP = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.e = 0
        self.f = 0
        self.cost = 0
        self.fitness = 0





def checkLimit(child ,gerador): #Checa se o filho gerou um valor P que está dentro dos limites
	# enumerate all dimensions of the point
    if(child.valueP < gerador.minP or child.valueP > gerador.maxP):
        return False
    else:
	    return True


def setCost(children): 
    for i in range(len(children)):
        children[i].cost = (children[i].a*pow(children[i].valueP, 2)) + (children[i].b*children[i].valueP) + children[i].c + abs(children[i].e*math.sin(children[i].f(children[i].minP-children[i].valueP)))
    return children


def fitness_calc(individuos):
    fitness = []
    nota = 0
    for indiv in individuos:
        if (checkLimit(indiv)):
            indiv.fitness = indiv.valueP
        else:
            if indiv.valueP <= 0:
                indiv.fitness = indiv.valueP*0.01 #diminui a probabilidade de valores que não respeitam restrições serem escolhidos
            else:
                indiv.fitness = indiv.valueP/0.01 #diminui a probabilidade de valores que não respeitam restrições serem escolhidos
    return individuos



def restrictionTreatment(parent, childrenNumber): #Gera os 30 descendentes baseados no pai e retorna a lista com os descendentes
    children = []
    for i in range(childrenNumber):
        child = None
        while(child is None or not checkLimit(child ,parent)): #calcula o valor de P do novo indiviudo
            #child = gerador.valueP + 0.5*random.uniform(0,1)*(gerador.maxP*(gerador.valueP) - gerador.minP(gerador.valueP)) #função 1
            child = parent.valueP - 0.5*random.uniform(0,1)*(parent.maxP*(parent.valueP) - parent.minP(parent.valueP)) #função 2 acho que uma é de minimiazação e outra de maximização
        child = gerador(child,parent.minP, parent.maxP, parent.a, parent.b, parent.c, parent.e, parent.f)
        children.append(deepcopy(child))
    
    children = setCost(deepcopy(children)) #setamos o valor de custo calculado para cada individuo gerado
    children = fitness_calc(children)
    custoTotal = totalCost(deepcopy(children)) #calculamos o valor do custo total para a população atual
    pTotal = totalP(children) #calculamos o valor total de P para a população atual
    minF = 0
    q1=500 #tirado do artigo
    q2=50 #tirado do artigo
    pl = 0  #PL = 0 pois está escrito na doc do TP
    if(custoTotal < (pTotal - pl - 1800)):
        minF = custoTotal + q1*abs(pTotal - pl - 1800) 
    elif(custoTotal > (pTotal - 0 - 1800)):
        minF = custoTotal + q2*abs(pTotal - pl - 1800)
    #durante esse calculo de minF provavelmente é necessário armazenar o valor resultante em um array pra depois sabermos qual foi o minimo da função
    #esse valor do minF que será usado pra preencher as tabelas do TP provavelmente

    return children



# def restrictionTreatment(children): #por enquanto o newPopu só está com os valores de P da próxima população e não os individuos em si
#     newPopu = []
#     for gerador in geradores:
#         if(gerador.minP > gerador.valueP or gerador.maxP < gerador.valueP ):
#             #newIndividuo = gerador.valueP + 0.5*random.uniform(0,1)*(gerador.maxP*(gerador.valueP) - gerador.minP(gerador.valueP)) #função 1
#             newIndividuoP = gerador.valueP - 0.5*random.uniform(0,1)*(gerador.maxP*(gerador.valueP) - gerador.minP(gerador.valueP)) #função 2 acho que uma é de minimiazação e outra de maximização
#             newPopu.append(gerador(newIndividuoP, gerador.minP, gerador.maxP, gerador.a, gerador.b, gerador.c, gerador.e, gerador.f))
    
    
#     custoTotal = totalCost(newPopu)
#     pTotal = totalP(newPopu)
#     minF = 0
#     q1=500 #tirado do artigo
#     q2=50 #tirado do artigo
#     pl = 0  #PL = 0 pois está escrito na doc do TP
#     if(custoTotal < (pTotal - pl - 1800)):
#         minF = custoTotal + q1*abs(pTotal - pl - 1800) 
#     elif(custoTotal > (pTotal - 0 - 1800)):
#         minF = custoTotal + q2*abs(pTotal - pl - 1800)
#     #durante esse calculo de minF provavelmente é necessário armazenar o valor resultante em um array pra depois sabermos qual foi o minimo da função
#     #esse valor do minF que será usado pra preencher as tabelas do TP provavelmente

#     return newPopu

# def calcula_restricao_func(indiv):
#     g1 = -(x1 -5)**2 - (x2-5)**2 + 100
#     g2 = (x1 - 6)**2 + (x2-5)**2 - 82.81
#     if g1 <= 0 and g2 <= 0:
#         return True
#     return False
























parent = 1
children = 30
childrenNumber = int(children/parent)





def uniformMutation(individuos):
    p = 0.05 #probabilidade de adicionar ruído à um elemento do vetor, normalmente entre 0,1 e 5%
    v = []
    newPopu = []
    for indivi in individuos:
        randomNumber = random.uniform(0,1)
        if(p >= randomNumber):
            vX = random.uniform(0, 1)*(100-13)*(2*random.uniform(0, 1)-1)
            vY = random.uniform(0, 1)*(100-0)*(2*random.uniform(0, 1)-1)
            value = evaluate(indivi.x + vX, indivi.y + vY)
            indivi = individuo(indivi.x + vX, indivi.y + vY, value)
            #newIndividuo = individuo(indivi.x + vX, indivi.y + vY, value)
            #newPopu.append(copy.deepcopy(newIndividuo))
    return individuos




def totalCost(children):
    totalCost = 0
    for i in range(len(children)):
        totalCost = totalCost + children[i].cost
    return totalCost

def totalP(geradores):
    totalValueP = 0
    for gerador in geradores:
        totalValueP = totalValueP + gerador.valueP
    return totalValueP



geradores = []
#=============================== Iniciar população
geradores.append(gerador(random.uniform(0,680), 0, 680, 0.00028, 8.1, 550, 300 , 0.035))
geradores.append(gerador(random.uniform(0,360), 0, 360, 0.00056, 8.1, 309, 200, 0.042))
geradores.append(gerador(random.uniform(0,360), 0, 360, 0.00056, 8.1, 307, 150, 0.042))
geradores.append(gerador(random.uniform(60,180), 60, 180, 0.00324, 7.74, 240, 150, 0.063))
geradores.append(gerador(random.uniform(60,180), 60, 180, 0.00324, 7.74, 240, 150, 0.063))
geradores.append(gerador(random.uniform(60,180), 60, 180, 0.00324, 7.74, 240, 150, 0.063))
geradores.append(gerador(random.uniform(60,180), 60, 180, 0.00324, 7.74, 240, 150, 0.063))
geradores.append(gerador(random.uniform(60,180), 60, 180, 0.00324, 7.74, 240, 150, 0.063))
geradores.append(gerador(random.uniform(60,180), 60, 180, 0.00324, 7.74, 240, 150, 0.063))
geradores.append(gerador(random.uniform(40,120), 40, 120, 0.00284, 8.6, 126, 100, 0.084))
geradores.append(gerador(random.uniform(40,120), 40,120, 0.00284, 8.6, 126, 100, 0.084))
geradores.append(gerador(random.uniform(55,120), 55, 120, 0.00284, 8.6, 126, 100, 0.084))
geradores.append(gerador(random.uniform(55,120), 55, 120, 0.00284, 8.6, 126, 100, 0.084))









k = 1 #(i) iniciar o contador de número de gerações, k = 1; 



#σi’(j) = σi(j)  exp [τ’ N(0,1) + τ  Nj(0,1)] #começo a perder as esperanças

#σ vai ser um vetor de desvios padrões, cada posição desse vetor será o desvio padrão da geração em questão


#τ =  1/raiz(2raiz(n))
#τ’ = 1/raiz(2n)
#n = número de parametros a serem otimizados(provavelmente são a,b,c,e,f , ou seja, n = 5)

def autoAdaptation(newPopu): #os parametros da nova população vão chegar com os parametros dos pais e serão sobrescritos
    n = 5
    for individuo in newPopu:
        individuo.a = newPopu.a * math.exp((1/math.sqrt(2*n)) * random.uniform(0,1) + (1/math.sqrt(2*math.sqrt(n))) * random.uniform(0,1))
        individuo.b = newPopu.b * math.exp((1/math.sqrt(2*n)) * random.uniform(0,1) + (1/math.sqrt(2*math.sqrt(n))) * random.uniform(0,1))
        individuo.c = newPopu.c * math.exp((1/math.sqrt(2*n)) * random.uniform(0,1) + (1/math.sqrt(2*math.sqrt(n))) * random.uniform(0,1))
        individuo.e = newPopu.e * math.exp((1/math.sqrt(2*n)) * random.uniform(0,1) + (1/math.sqrt(2*math.sqrt(n))) * random.uniform(0,1))
        individuo.f = newPopu.f * math.exp((1/math.sqrt(2*n)) * random.uniform(0,1) + (1/math.sqrt(2*math.sqrt(n))) * random.uniform(0,1))
    return newPopu


#onde os xi’s são dados pelo i-ésimo objeto variável (solução do problema)
#σ vai ser um vetor de desvios padrões, cada posição desse vetor será o desvio padrão da geração em questão
