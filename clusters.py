import pyodbc 
import random
import GenerateNumbers
import Get_numbers
import PlaceNember
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd

# запускаем генератор чисел и записываем их в бд
# GenerateNumbers.generate_nembers()

# достаем из бд нужное кол-во цифр
results = Get_numbers.get_numbers(100)

# проверяем числа и считаем Number и Place
dop_number = 931771
P = []
N = []
for i in results:
    p, n = PlaceNember.PlaceNumber(dop_number, i)
    P.append(p)
    N.append(n)

df = pd.DataFrame(pd.Series(results), columns=['number'])
df['N'] = pd.Series(N)
df['P'] = pd.Series(P)
print(df)

# построим 4 кластера на основе этих параметров
kmeans = KMeans(4).fit(df[['N','P']])

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

#выведем группы кластеров
df['cluster'] = pd.Series(labels)
cluster0 = df[df['cluster'] == 0]
cluster1 = df[df['cluster'] == 1]
cluster2 = df[df['cluster'] == 2]
cluster3 = df[df['cluster'] == 3]
print(cluster0)
print(30 * '_')
print(cluster1)
print(30 * '_')
print(cluster2)
print(30 * '_')
print(cluster3)

# визуализация кластеров
plt.plot(cluster0['N'],cluster0['P'], 'bo', label='class1')
plt.plot(cluster1['N'],cluster1['P'], 'go', label='class2')
plt.plot(cluster2['N'],cluster2['P'], 'ro', label='class3')
plt.plot(cluster3['N'],cluster3['P'], 'yo', label='class4')
plt.legend(loc=0)
plt.xlabel('N')
plt.ylabel('P')
plt.show()