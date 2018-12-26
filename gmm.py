
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.mixture import GaussianMixture


dataSet = pd.read_csv("summary.additive_select.csv")

bbgp = dataSet['BBGP'].tolist()
ks = dataSet['KS'].tolist()
gcmh = dataSet['GCMH'].tolist()

bbgpRS = np.reshape(bbgp,[-1,1])


N = np.arange(2,100)

models = [None for i in range(len(N))]

for i in range(len(N)):
    models[i] = GaussianMixture(N[i]).fit(bbgpRS)

AIC = [m.aic(bbgpRS) for m in models]
BIC = [m.bic(bbgpRS) for m in models]

fig = plt.figure(figsize=(5, 5))
fig.subplots_adjust(left=0.12, right=0.97,
                    bottom=0.21, top=0.9, wspace=0.5)
ax = fig.add_subplot(111)
M_best = models[np.argmin(AIC)]
print(np.argmin(AIC))
x = np.linspace(0, 372, 10000 )
x = np.reshape(x,[-1,1])
logprob = M_best.score_samples(x)
responsibilities = M_best.predict_proba(x)

pdf = np.exp(logprob)
pdf_individual = responsibilities * pdf[:, np.newaxis]

ax.hist(bbgpRS, 30, normed=True, histtype='stepfilled', alpha=0.4)
ax.plot(x, pdf, '-k')
ax.plot(x, pdf_individual, '--k')
ax.text(0.04, 0.96, "Best-fit Mixture",
        ha='left', va='top', transform=ax.transAxes)
ax.set_xlabel('$x$')
ax.set_ylabel('$p(x)$')

plt.show()
