import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

f = open("TP3Meta\solA.txt", "r")
lines = f.readlines()
treino = []
teste = []
decisao = []
for line in lines:
    line = line.strip("\n")
    line = line.split(", ")
    treino.append(float(line[0]))
    teste.append(float(line[1]))

print("MIN={:.10f}".format(np.min(treino)))
print("MAx={:.10f}".format(np.max(treino)))
print("Mean={:.10f}".format(np.mean(treino)))
print("STD={:.10f}".format(np.std(treino)))

print("MIN={:.10f}".format(np.min(teste)))
print("MAx={:.10f}".format(np.max(teste)))
print("Mean={:.10f}".format(np.mean(teste)))
print("STD={:.10f}".format(np.std(teste)))

plt.boxplot(treino, vert=False)
plt.xlabel("Valor função obejtivo treino")
plt.title("Configuracao 1")
plt.show()

plt.boxplot(teste, vert=False)
plt.xlabel("Valor função obejtivo teste")
plt.title("Configuracao 1")
plt.show()
