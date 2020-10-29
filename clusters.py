import pyodbc 
import random
import generate_numbers_v2
from Get_numbers_v2 import get_numbers
import PlaceNember
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.exceptions import ConvergenceWarning
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd

# Считает все warning как error
import warnings
warnings.filterwarnings("error")

def clustering(numbers, dop_number):
    # проверяем числа и считаем Number и Place
    # P = []
    # N = []
    # for i in numbers:
    #     p, n = PlaceNember.PlaceNumber(dop_number, i)
    #     P.append(p)
    #     N.append(n)
    P, N = PlaceNember.getPlaceNumberList(numbers, dop_number)

    df = pd.DataFrame(pd.Series(numbers), columns=['number'])
    df['N'] = pd.Series(N)
    df['P'] = pd.Series(P)

    # построим 4 кластера на основе этих параметров
    try:
        kmeans = KMeans(4).fit(df[['N','P']])
    except:
        tmp = pd.DataFrame()
        return tmp, tmp, tmp, tmp

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    #выведем группы кластеров
    df['cluster'] = pd.Series(labels)
    cluster0 = df[df['cluster'] == 0]
    cluster1 = df[df['cluster'] == 1]
    cluster2 = df[df['cluster'] == 2]
    cluster3 = df[df['cluster'] == 3]
    # print(cluster0)
    # print(30 * '_')
    # print(cluster1)
    # print(30 * '_')
    # print(cluster2)
    # print(30 * '_')
    # print(cluster3)

    return cluster0,cluster1,cluster2,cluster3

def visualization_clusters(cluster0,cluster1,cluster2,cluster3):
    # визуализация кластеров
    plt.figure()
    plt.title("Визуализация кластеров")
    plt.plot(cluster0['N'],cluster0['P'], 'bo', label='class1')
    plt.plot(cluster1['N'],cluster1['P'], 'go', label='class2')
    plt.plot(cluster2['N'],cluster2['P'], 'ro', label='class3')
    plt.plot(cluster3['N'],cluster3['P'], 'yo', label='class4')
    plt.legend(loc=0)
    plt.xlabel('N')
    plt.ylabel('P')
    plt.show()

# тестирование функций
# cl0, cl1, cl2, cl3 = clustering(get_numbers(20), 931771)
# visualization_clusters(cl0, cl1, cl2, cl3)