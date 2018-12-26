import pandas as pd
import statistics
from statistics import mode

folder = '1d_cutoff'
clusters = 16
for num in range(2, 11):
    fName = 'E:/논문데이터/simulation/' + folder + '/merging_em' + str(num) + '.csv'
    oName = 'E:/논문데이터/simulation/' + folder + '/eval_each' + str(num) + '_out.csv'
    file = open(fName, 'r')
    out = open(oName, 'w')

    title = file.readline()

    tp = [0] * clusters
    fn = [0] * clusters
    fp = [0] * clusters
    tn = [0] * clusters
    for line in file:
        tmp = line.strip().split(',')
        pos = int(tmp[0])

        for cluster in range(1, clusters):
            voting = int(tmp[cluster])

            if( pos  < 41000):
                if(voting == 1):
                    tp[cluster] += 1
                else:
                    fn[cluster] += 1
            else:
                if(voting == 1):
                    fp[cluster] += 1
                else:
                    tn[cluster] += 1
    # tp tn fp fn
    for cluster in range(1, clusters):
        out.write(str(tp[cluster]) + ',' + str(fn[cluster]) + ',' + str(fp[cluster]) + ',' + str(tn[cluster]) + '\n')
    out.close()