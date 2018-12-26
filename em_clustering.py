from sklearn.mixture import GaussianMixture
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
simData = pd.read_csv('./simulation.scaled.csv', ',')
ks = simData['KS']
bbgp = simData['BBGP']
gcmh = simData['GCMH']
name = simData['2L_POS']

feature = pd.concat([bbgp, ks, gcmh], axis=1)

for n in range(2, 500):
    model = GaussianMixture(n_components=n, covariance_type='full', init_params='random')
    model.fit(feature)
    predict =pd.DataFrame(model.predict(feature))
    predict.columns = ['predict']

    result = pd.concat([name, feature, predict], axis=1)
    result.to_csv('./em.full/GaussianMixture' + str(n) + '.csv')

    fig = plt.figure()
    ax = Axes3D(fig)

    ax.scatter(xs=result['KS'], ys=result['BBGP'], zs = result['GCMH'], c = result['predict'], s=10, alpha=0.5, edgecolor='none')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    plt.savefig('./em.full/EM_CLUSTERING_KS_BBGP_GCMH_' + str(n) + '.png')
    plt.close(fig)
