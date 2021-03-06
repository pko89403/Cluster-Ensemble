import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.utils import check_random_state

random_state = np.random.RandomState(0)
simData = pd.read_csv('./summary.additive_select.csv', ',')

CLUSTER=1000
BIAS = 'KS'
OUTPUT = './kmeans_1d_ks/'


ks = simData['KS']
bbgp = simData['BBGP']
gcmh = simData['GCMH']
name = simData['2L_POS']

feature = pd.concat([ks], axis=1)

# K-MEANS Algorithm

init_C = range(2,CLUSTER)
inertias = []

# Elbow methd, x = class Num // y = inertia : Sum of squared distances - Elbow Method For Optimal

for k in init_C:
    model = KMeans(n_clusters=k)
    model.fit(feature)
    inertias.append(model.inertia_)
plt.plot(init_C, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')

inerPATH = OUTPUT + 'KMEANS_' + BIAS + '_' + str(CLUSTER) + '.png'
plt.savefig(inerPATH)
plt.close()

x = feature[BIAS]
for n in range(2, CLUSTER):
    model = KMeans(n_clusters=n,random_state=random_state, n_jobs=4, max_iter=300)
    feature['label'] = model.fit_predict(feature)

    result = pd.concat([name, feature], axis=1)
    result.to_csv(OUTPUT + 'Kmeans' + str(n) + '.csv')

    fig = plt.figure()
    sns.set_style('white')
    plt.scatter(x=x, y=feature['label'], c=model.labels_.astype(float))
    plt.savefig(OUTPUT + 'KMEANS_' + str(n) + '.png')
    plt.close()

