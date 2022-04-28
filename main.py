import math
import openpyxl
from scipy.stats import chi2
import statistics
import matplotlib.pyplot as plt
from pandas import *
import numpy as np

# берем данные из таблички
data = read_csv('bank.csv')
data = data['balance'].tolist()
numbers = data

# Количество элементов
count = len(numbers)
print("Количество чисел: ", count)

# Мода и медиана
median = statistics.median(numbers)
mode = statistics.mode(numbers)
print("Медиана: ", median)
print("Мода: ", mode)


# Мин-макс числа, количество и длина интервалов
print("Минимальное число: ", min(numbers))
print("Максимальное число: ", max(numbers))
intervalCount = math.floor(1 + 3.322 * math.log10(count))
print("Количество интервалов: ", intervalCount)
intervalLength = math.ceil((max(numbers) - min(numbers)) / math.floor(intervalCount))
print("Длина интервала: ", intervalLength)

# Вывод интервалов
intervalMin = math.floor(min(numbers))
interval = [[0 for x in range(2)] for y in range(intervalCount)]
for i in range(0, intervalCount):
    interval[i][0] = intervalMin
    interval[i][1] = intervalMin + intervalLength
    intervalMin = intervalMin + intervalLength
print(interval)
print("\n")

# Количество элементов в каждом интервале
intervalElementsCount = [[] for y in range(intervalCount)]
for i in range(0, intervalCount):
    x = 0
    for j in range(0, count):
        if (numbers[j] < interval[i][1] and numbers[j] >= interval[i][0]):
            x = x + 1
    intervalElementsCount[i].append(x)
print(intervalElementsCount)

# Проверка количества элементов
totalElements = np.sum(intervalElementsCount)
print(f"\nВсего элементов {totalElements}")
print("\n")

# Среднее в каждом интервале
intervalMiddle = [[] for y in range(0, intervalCount)]
mid = 0
for i in range(0, intervalCount):
    mid = (interval[i][0] + interval[i][1]) / 2
    intervalMiddle[i].append(mid)
print(intervalMiddle)

# Выборочная средняя равна
xMiddle = 0
for i in range(0, intervalCount):
    xMiddle = xMiddle + (intervalMiddle[i][0] * intervalElementsCount[i][0])
xMiddle = xMiddle / count
print("\nВыборочная средняя равна", xMiddle)

# Выборочная дисперсия
z = [[] for y in range(0, intervalCount)]
for i in range(0, intervalCount):
    zmid = 0.0
    zmid = (intervalMiddle[i][0] - xMiddle) ** 2
    z[i].append(zmid)

print(z)

sigma = 0.0
for i in range(0, intervalCount):
    sigma = sigma + (z[i][0] * intervalElementsCount[i][0])
s2 = sigma / count
print("Выборочная дисперсия равна: ", s2)


t = [[0 for x in range(4)] for y in range(0, 29)]
t[0][0] = 5; t[0][1] = 2.78; t[0][2] = 4.60; t[0][3] = 8.61
t[1][0] = 6; t[1][1] = 2.57; t[1][2] = 4.03; t[1][3] = 6.86
t[2][0] = 7; t[2][1] = 2.45; t[2][2] = 3.71; t[2][3] = 5.96
t[3][0] = 8; t[3][1] = 2.37; t[3][2] = 3.50; t[3][3] = 5.41
t[4][0] = 9; t[4][1] = 2.31; t[4][2] = 3.36; t[4][3] = 5.04
t[5][0] = 10; t[5][1] = 2.26; t[5][2] = 3.25; t[5][3] = 4.78
t[6][0] = 11; t[6][1] = 2.23; t[6][2] = 3.17; t[6][3] = 4.59
t[7][0] = 12; t[7][1] = 2.20; t[7][2] = 3.11; t[7][3] = 4.44
t[8][0] = 13; t[8][1] = 2.18; t[8][2] = 3.06; t[8][3] = 4.32
t[9][0] = 14; t[9][1] = 2.16; t[9][2] = 3.01; t[9][3] = 4.22
t[10][0] = 15; t[10][1] = 2.15; t[10][2] = 2.98; t[10][3] = 4.14
t[11][0] = 16; t[11][1] = 2.13; t[11][2] = 2.95; t[11][3] = 4.07
t[12][0] = 17; t[12][1] = 2.12; t[12][2] = 2.92; t[12][3] = 4.02
t[13][0] = 18; t[13][1] = 2.11; t[13][2] = 2.90; t[13][3] = 3.97
t[14][0] = 19; t[14][1] = 2.10; t[14][2] = 2.88; t[14][3] = 3.92
t[15][0] = 20; t[15][1] = 2.093; t[15][2] = 2.861; t[15][3] = 3.883
t[16][0] = 25; t[16][1] = 2.064; t[16][2] = 2.797; t[16][3] = 3.745
t[17][0] = 30; t[17][1] = 2.045; t[17][2] = 2.756; t[17][3] = 3.659
t[18][0] = 35; t[18][1] = 2.032; t[18][2] = 2.720; t[18][3] = 3.600
t[19][0] = 40; t[19][1] = 2.023; t[19][2] = 2.708; t[19][3] = 3.558
t[20][0] = 45; t[20][1] = 2.016; t[20][2] = 2.692; t[20][3] = 3.527
t[21][0] = 50; t[21][1] = 2.009; t[21][2] = 2.679; t[21][3] = 3.502
t[22][0] = 60; t[22][1] = 2.001; t[22][2] = 2.662; t[22][3] = 3.464
t[23][0] = 70; t[23][1] = 1.996; t[23][2] = 2.649; t[23][3] = 3.439
t[24][0] = 80; t[24][1] = 1.001; t[24][2] = 2.640; t[24][3] = 3.418
t[25][0] = 90; t[25][1] = 1.987; t[25][2] = 2.633; t[25][3] = 3.403
t[26][0] = 100; t[26][1] = 1.984; t[26][2] = 2.627; t[26][3] = 3.392
t[27][0] = 120; t[27][1] = 1.980; t[27][2] = 2.627; t[27][3] = 3.374
t[28][0] = 0; t[28][1] = 1.960; t[28][2] = 2.576; t[28][3] = 3.291


#Определяем
if (count <= 20):
    n = count
elif 20 < count <= 50:
    if count % 10 == 0:
        n = count
    elif count % 5 == 0:
        n = count
    else:
        n = count - (count % 5)
elif 50 < count <= 100:
    if count % 10 == 0:
        n = count
    else:
        n = count - (count % 10)
elif (count <= 120 and count > 100):
    n = 120
else:
    n = 0
j = 0
for i in range(0, 29):
    if (n == t[i][0]):
        j = i
# Выбираем значение доверительной вероятности
gamma = int(input("Выберите значение гаммы: \n 1) y = 0.95 \n 2) y = 0,99 \n 3) y =  0.999 \n"))

# Доверительный интервал для генерального среднего
xIntervalMin = xMiddle - (t[j][gamma] * math.sqrt(sigma)) / math.sqrt(count)
xIntervalMax = xMiddle + (t[j][gamma] * math.sqrt(sigma)) / math.sqrt(count)
gamma = 0
if(gamma == 1):
    gamma = 0.95
elif(gamma == 2):
    gamma = 0.99
else:
    gamma = 0.999

print(xIntervalMin, "< x <", xIntervalMax)

# Доверительный интервал для генеральной дисперсии

d = [0 for i in range(intervalCount)]
for i in range(intervalCount):
    d[i] = intervalMiddle[i][0] - xMiddle

a = 0

for i in range(intervalCount):
    a = a + (d[i] * d[i] * d[i] * intervalElementsCount[i][0] / count)
a = a / math.pow(math.sqrt(sigma), 3)

df = count - 1
alfa1 = (1 - gamma) / 2
alfa2 = (1 + gamma) / 2
p1 = 1 - alfa1
p2 = 1 - alfa2

intervalSigma1 = (df*sigma)/chi2.ppf(p1, df)
intervalSigma2 = (df*sigma)/chi2.ppf(p2, df)

print(intervalSigma1, "<sigma<", intervalSigma2)

# Строим гистограмму
plt.hist(numbers, edgecolor='black', bins=intervalCount)
plt.title('Гистограма')
plt.xlabel('Значения')
plt.ylabel('Частоты')
plt.show()

# Эксцесс

z4 = [0 for y in range(0, intervalCount)]
x = 0
for i in range(0, intervalCount):
    z4[i] = (z[i][0])**2

m4 = 0

for i in range(0, intervalCount):
    m4 = m4 + z4[i]*intervalElementsCount[i][0]


m4 = m4/count


ek = m4/(sigma**2) - 3

print("Ek равно ",ek)

# Ассиметрия
z3 = [0 for y in range(0, intervalCount)]
x = 0
for i in range(0, intervalCount):
    z3[i] = (z[i][0])**(1.5)

m3 = 0

for i in range(0, intervalCount):
    m3 = m3 + z3[i] * intervalElementsCount[i][0]
m3 = m3/count
a3 = m3/(sigma**(1.5))

print("A3 равно ", a3)