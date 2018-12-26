import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.mixture import GaussianMixture


dataSet = pd.read_csv('summary.additive_select.csv')

bbgp = dataSet['BBGP'].tolist()
ks = dataSet['KS'].tolist()
gcmh = dataSet['GCMH'].tolist()

bbgpRS = np.reshape(bbgp,[-1,1])

N = np.arange(3,4)

models = [None for i in range(len(N))]

for i in range(len(N)):
    models[i] = GaussianMixture(N[i]).fit(bbgpRS)

AIC = [m.aic(bbgpRS) for m in models]
BIC = [m.bic(bbgpRS) for m in models]
print(AIC, BIC)
M_best = models[np.argmin(AIC)]

fig = plt.figure(figsize=(10, 10))
fig.subplots_adjust(left=0.12, right=0.97,
                    bottom=0.21, top=0.9, wspace=0.5)
ax = fig.add_subplot(131)
M_best = models[np.argmin(AIC)]

x = np.linspace(0, 372, 373 )
x = np.reshape(x,[-1,1])
logprob = M_best.score_samples(x)
responsibilities = M_best.predict_proba(x)

pdf = np.exp(logprob)
pdf_individual = responsibilities * pdf[:, np.newaxis]

ax.hist(bbgpRS, 30, normed=True, histtype='stepfilled', alpha=0.8)
ax.plot(x, pdf, '-k')
ax.plot(x, pdf_individual, '--k')
ax.text(0.04, 0.96, "Best-fit Mixture",
        ha='left', va='top', transform=ax.transAxes)
ax.set_xlabel('$x$')
ax.set_ylabel('$p(x)$')

ax = fig.add_subplot(132)
ax.plot(N, AIC, '-k', label='AIC')
ax.plot(N, BIC, '--k', label='BIC')
ax.set_xlabel('n. components')
ax.set_ylabel('information criterion')
ax.legend(loc=2)

ax = fig.add_subplot(133)
p = M_best.predict_proba(x)
p = p[:, (0, 1, 2)]  # rearrange order so the plot looks better
p = np.cumsum(p,1).T
fuck = np.reshape(p[0],[-1,1])


x = np.linspace(0, 372, 373 )
ax.fill_between(x, 0, p[0], color='gray', alpha=0.3)
ax.fill_between(x, p[0], p[1], color='gray', alpha=0.5)
ax.fill_between(x, p[1], 1, color='gray', alpha=0.7)
ax.set_xlim(0, 372)
ax.set_ylim(0, 1)
ax.set_xlabel('$x$')
ax.set_ylabel(r'$p({\rm class}|x)$')

ax.text(-5, 0.3, 'class 1', rotation='vertical')
ax.text(0, 0.5, 'class 2', rotation='vertical')
ax.text(3, 0.3, 'class 3', rotation='vertical')

plt.show()
