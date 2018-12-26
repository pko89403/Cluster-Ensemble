import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import sys

simData = pd.read_csv('./bbgp_Kmeans8.csv', ',')

bbgp = simData['BBGP']
label = simData['label']

fig = plt.figure()
sns.set_style('white')
plt.scatter(x=[1]*len(bbgp), y=bbgp, c=label)
plt.xticks([])
plt.savefig('./bbgp_Kmeans8.csv.png')
plt.close()

