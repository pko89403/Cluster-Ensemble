import pandas as pd
import statistics
from statistics import mode



folder = './1d_split_filtered/data'

cutOffs = [  [22.36680126,19.89733,98.128],
            [20.53607467,20.02002,93.786],
            [22.2442648,19.30419,95.851],
            [20.14733744,19.59071,94.986],
            [21.44674312,19.79123,92.956],
            [21.17997408,20.69631,96.744],
            [22.93729035,18.01989,95.209],
            [17.61926294,18.62175,96.165],
            [22.0574646,18.61274,97.885],
            [21.04910525,19.99288,97.352]   ]

for s in range(1, 11):
    fName = 'E:/논문데이터/simulation/' + folder + '/summary.additive_select_split' + str(s) + '.csv'

    file = open(fName, 'r')

    title = file.readline()

    tp = 0
    tn = 0
    fp = 0
    fn = 0
    cutOff = float(cutOffs[s-1][1])         # 0 = bbgp, 1 = gcmh, 2 = ks


    for line in file:
        tmp = line.strip().split(',')

        pos = int(tmp[1])
        val = float(tmp[4]) # 2 = bbgp, 3 = ks, 4 = gcmh

        if( pos  < 41000):
            if(cutOff <= val):
                tp += 1
            else:
                fn += 1
        else:
            if(cutOff <= val):
                fp += 1
            else:
                tn += 1

    print(tp, fn, fp, tn)
        # tp tn fp fn
