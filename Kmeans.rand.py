import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
simData = pd.read_csv('./simulation.scaled.csv', ',')

ks = simData['KS']
bbgp = simData['BBGP']
gcmh = simData['GCMH']
name = simData['2L_POS']

feature = pd.concat([bbgp, ks, gcmh], axis=1)



# K-MEANS Algorithm
"""
ks = range(2,500)
inertias = []

for k in ks:
    model = KMeans(n_clusters=k)
    model.fit(feature)
    inertias.append(model.inertia_)

plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.savefig('KMEANS_KS_BBGP_GCMH_500.png')
"""
for n in range(2, 500):
    model = KMeans(n_clusters=n, init='random', n_jobs=3)
    model.fit(feature)
    predict =pd.DataFrame(model.predict(feature))
    predict.columns = ['predict']

    result = pd.concat([name, feature, predict], axis=1)
    result.to_csv('./Kmeansr/Kmeans' + str(n) + '.csv')

    fig = plt.figure()
    ax = Axes3D(fig)

    ax.scatter(xs=result['KS'], ys=result['BBGP'], zs = result['GCMH'], c = result['predict'], s=10, alpha=0.5, edgecolor='none')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    plt.savefig('./Kmeansr/KMEANS_KS_BBGP_GCMH_' + str(n) + '.png')
    plt.close()
