import numpy as np
import pandas as pd
from sklearn.preprocessing import minmax_scale
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
import seaborn as sns

random_state = np.random.RandomState(0)
simData = pd.read_csv('./summary.additive_select.csv', ',')

CLUSTER=4
BIAS = 'BGGC'
OUTPUT = './'

# min-max
simData['KSN'] = minmax_scale(simData['KS'].values.tolist())
simData['BBGPN'] = minmax_scale(simData['BBGP'].values.tolist())
simData['GCMHN'] = minmax_scale(simData['GCMH'].values.tolist())

simData.to_csv('./simData_additive.csv')

ks = simData['KSN']
bbgp = simData['BBGPN']
gcmh = simData['GCMHN']
name = simData['2L_POS']

feature = pd.concat([bbgp, gcmh],axis=1)
logPATH = OUTPUT + 'em_' + BIAS + '_' + str(CLUSTER) + '.csv'
logW = open(logPATH, 'w')

for n in range(2, CLUSTER):
    model = GaussianMixture(n_components=n, covariance_type='spherical', max_iter=300)
    simData['label'] = model.fit_predict(feature)
    print(model.means_)
    bic = model.bic(feature)
    aic = model.aic(feature)
    logW.write(str(aic) + ',\t' + str(bic) + '\n')

    fig = plt.figure()
    sns.set_style('white')
    plt.scatter(x=feature['BBGPN'], y=feature['GCMHN'], c=simData['label'])
    plt.savefig(OUTPUT + 'em_' + str(n) + '.png')
    plt.close()

    simData['FS'] = simData['BBGPN'] + simData['GCMHN']

    centroid = simData.groupby('label')['FS'].mean().sort_values()
    simData['cmean'] = simData['FS'].groupby(simData['label']).transform('mean')

    cLabel = n
    for i in centroid:
        simData.loc[simData['cmean'] == i, 'label'] = cLabel
        cLabel -= 1

    simData = simData.drop('cmean', 1)
    simData = simData.drop('FS', 1)

    simData.to_csv(OUTPUT + 'em_' + str(n) + '.csv', index=False)


logW.close()
