import matplotlib.pyplot as plt
import numpy as np

f = open("sol2b.txt", "r")
lines = f.readlines()
x = []
y = []
sol = []
for line in lines:
    line = line.strip("\n")
    line = line.split(", ")
    x.append(float(line[0]))
    y.append(float(line[1]))
    sol.append(float(line[2]))

print("MIN={:.10f}".format(np.min(sol)))
print("MAx={:.10f}".format(np.max(sol)))
print("Mean={:.10f}".format(np.mean(sol)))
print("STD={:.10f}".format(np.std(sol)))

plt.boxplot(sol, vert=False)
plt.xlabel("Valor função obejtivo")
plt.title("Hill Climbing 2-b")
plt.show()
