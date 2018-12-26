import pandas as pd
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import numpy as np
import seaborn


def cutoff_youdens_j(fpr,tpr,thresholds):
    j_scores = tpr-fpr
    j_ordered = sorted(zip(j_scores,thresholds))
    return j_ordered[-1][1]


for i in range(1, 11):
    dataSet = pd.read_csv("./1d_split_filtered/data_filtered/summary.additive_select_split" + str(i) + ".csv")
    bbgp = dataSet[['BBGP', 'SELECT']]
    ksPval = dataSet[['KS', 'SELECT']]
    gcmh = dataSet[['GCMH', 'SELECT']]
    bbgp.sort_values(by=['BBGP']).reset_index(drop=True)
    ksPval.sort_values(by=['KS']).reset_index(drop=True)
    gcmh.sort_values(by=['GCMH']).reset_index(drop=True)

    scores = bbgp['BBGP']
    true_labels = bbgp['SELECT']

    ### actual code for roc + threshold charts start here
    # compute fpr, tpr, thresholds and roc_auc
    fpr, tpr, thresholds = roc_curve(true_labels, scores)

    roc_auc = auc(fpr, tpr)  # compute area under the curve

    plt.figure()
    plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % (roc_auc))
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")

    # create the axis of thresholds (scores)
    ax2 = plt.gca().twinx()
    ax2.plot(fpr, thresholds, markeredgecolor='r', linestyle='dashed', color='r')
    ax2.set_ylabel('Threshold', color='r')
    #ax2.set_ylim([thresholds[-1], thresholds[0]])
    #ax2.set_xlim([fpr[0], fpr[-1]])

    plt.savefig('bbgp_roc_and_threshold_' + str(i) + '.png')
    plt.close()
    print(cutoff_youdens_j(fpr, tpr, thresholds))

