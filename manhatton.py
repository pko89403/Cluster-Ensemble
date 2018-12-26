
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataSet = pd.read_csv("summary.additive_select.csv")
dataSet.sort_values(by=['2L_POS'])
print(dataSet)
dataSet['ind'] = range(len(dataSet))
dataSet['val'] = -np.log10(dataSet['KS'])

plt.scatter(x=dataSet['ind'].values, y=dataSet['val'].values, color='blue', alpha=0.1, s = 1)
plt.xlim([0, len(dataSet)])
plt.ylim(([0, 10]))
plt.show()

