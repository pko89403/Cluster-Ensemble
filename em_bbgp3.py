import numpy as np
import pandas as pd
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
import seaborn as sns

CLUSTER=101
BIAS='BBGP'
for s in range(1, 11):
	simData = pd.read_csv('./filtered_input/summary.additive_select_split' + str(s) + '.csv', ',')

	OUTPUT = './1d_split/em_1d_bbgp_tied' + str(s) + '/'

	ks = simData['KS']
	bbgp = simData['BBGP']
	gcmh = simData['GCMH']
	name = simData['2L_POS']

	feature = pd.concat([bbgp], axis=1)
	logPATH = OUTPUT + 'em_' + BIAS + '_' + str(CLUSTER) + '.csv'
	logW = open(logPATH, 'w')


	for i in range(2, CLUSTER):
    		model = GaussianMixture(n_components=i, covariance_type='tied', max_iter=300)
    		simData['label'] = model.fit_predict(feature)

	    	bic = model.bic(feature)
   	 	logW.write(str(bic) + '\n')

    		simData.to_csv(OUTPUT + 'em_' + str(i) + '.csv')

	logW.close()