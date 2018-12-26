import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.utils import check_random_state

random_state = np.random.RandomState(0)

CLUSTER=101
BIAS = 'BBGP'

for s in range(1,11):
	simData = pd.read_csv('./filtered_input/summary.additive_select_split' + str(s) + '.csv', ',')
	OUTPUT = './1d_split/kmeans_1d_bbgp_elkan' + str(s) + '/'

	ks = simData['KS']
	bbgp = simData['BBGP']
	gcmh = simData['GCMH']
	name = simData['2L_POS']

	feature = pd.concat([bbgp], axis=1)

	# K-MEANS Algorithm

	init_C = range(2,CLUSTER)
	inertias = []

	inerPATH = OUTPUT + 'KMEANS_' + BIAS + '_' + str(s) + '.csv'
	inertiaW= open(inerPATH, 'w')

	x = feature[BIAS]
	for n in range(2, CLUSTER):
		model = KMeans(n_clusters=n,random_state=random_state, n_jobs=4, algorithm='elkan', max_iter=300)
		feature['label'] = model.fit_predict(feature)
		inertiaW.write(str(model.inertia_)+'\n')
		result = pd.concat([name, feature], axis=1)
		result.to_csv(OUTPUT + 'Kmeans' + str(n) + '.csv')

		fig = plt.figure()
		sns.set_style('white')
		plt.scatter(x=[1]*len(x), y=x, c=model.labels_.astype(float))
		plt.savefig(OUTPUT + 'KMEANS_' + str(n) + '.png')
		plt.close()

	inertiaW.close()
