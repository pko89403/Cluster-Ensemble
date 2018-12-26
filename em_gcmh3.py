import numpy as np
import pandas as pd
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
import seaborn as sns

CLUSTER=101
BIAS='GCMH'
for s in range(1, 11):
	simData = pd.read_csv('./filtered_input/summary.additive_select_split' + str(s) + '.csv', ',')

	OUTPUT = './1d_split/em_1d_gcmh_full' + str(s) + '/'

	ks = simData['KS']
	bbgp = simData['BBGP']
	gcmh = simData['GCMH']
	name = simData['2L_POS']

	feature = pd.concat([gcmh], axis=1)
	logPATH = OUTPUT + 'em_' + BIAS + '_' + str(CLUSTER) + '.csv'
	logW = open(logPATH, 'w')

	for i in range(2, CLUSTER):
    		model = GaussianMixture(n_components=i, covariance_type='full', max_iter=300)
    		simData['label'] = model.fit_predict(feature)

	    	bic = model.bic(feature)
   	 	aic = model.aic(feature)
   	 	logW.write(str(bic) + '\n')

    		fig = plt.figure()
    		sns.set_style('white')
    		plt.scatter(x=[1]*len(feature), y=feature, c=simData['label'])
    		plt.xticks(range(0,i))
    		plt.savefig(OUTPUT + 'em_' + str(i) + '.png')
    		plt.close()

    		simData.to_csv(OUTPUT + 'em_' + str(i) + '.csv')

	logW.close()