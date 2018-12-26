import numpy as np
import pandas as pd
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
import seaborn as sns

CLUSTER=11
BIAS='KS'
for s in range(1, 11):
	simData = pd.read_csv('./summary.additive_select_split' + str(s) + '.csv', ',')

	OUTPUT = './1d_split/em_1d_ks_tied' + str(s) + '/'

	ks = simData['KS']
	bbgp = simData['BBGP']
	gcmh = simData['GCMH']
	name = simData['2L_POS']

	feature = pd.concat([ks], axis=1)
	logPATH = OUTPUT + 'em_' + BIAS + '_' + str(CLUSTER) + '.csv'
	logW = open(logPATH, 'w')

	for i in range(2, CLUSTER):
    		model = GaussianMixture(n_components=i, covariance_type='tied', max_iter=300)
    		simData['label'] = model.fit_predict(feature)

	    	bic = model.bic(feature)
   	 	aic = model.aic(feature)
   	 	logW.write(str(aic) + ',\t' + str(bic) + '\n')

    		fig = plt.figure()
    		sns.set_style('white')
    		plt.scatter(y=feature, x=simData['label'], c=simData['label'])
    		plt.xticks(range(0,i))
    		plt.savefig(OUTPUT + 'em_' + str(i) + '.png')
    		plt.close()

    		simData.to_csv(OUTPUT + 'em_' + str(i) + '.csv')

	logW.close()