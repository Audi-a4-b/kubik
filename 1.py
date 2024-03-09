import math
import matplotlib.pyplot as plt
import numpy as np

rah = [0, 0, 0, 0, 0, 0, 0]
x = [1, 2, 3, 4, 5, 6, 7]
n = 10000
arr = []
suma1 = 0
suma2 = 0

for i in range(n):
    arr.append(np.random.randint(1, 8))

for i in arr:
    if i == 1:
        rah[0] += 1
    if i == 2:
        rah[1] += 1
    if i == 3:
        rah[2] += 1
    if i == 4:
        rah[3] += 1
    if i == 5:
        rah[4] += 1
    if i == 6:
        rah[5] += 1
    if i == 7:
        rah[6] += 1



for el in arr:
    suma1 += el
    suma2 += el ** 2

matspod = suma1 / n
kvadr = suma2 / n
disp = kvadr - matspod ** 2

serkvad = math.sqrt(disp)

print("Математичне сподівання -> ", matspod, "\nДисперсія -> ", disp, "\nСереднє кв. відхилення -> ", serkvad)

for i, count in enumerate(rah, 1):
    print(f"Число {i} випало {count} разів")

fig, ax = plt.subplots()


ax.bar(x, [count / n for count in rah])


plt.show()
