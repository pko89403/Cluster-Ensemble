import pandas as pd
import statistics
from statistics import mode



folder = './1d_split_filtered/opt_result_relabel_last'
output = 'E:/논문데이터/simulation/' + folder + '/eval_result.csv'
eOut = open(output, 'w')

for num in range(2, 3):
    for s in range(1, 11):
        fName = 'E:/논문데이터/simulation/' + folder + '/merging_' + str(s) + 'OPT.csv'
        oName = 'E:/논문데이터/simulation/' + folder + '/merging_' + str(s) + 'OPT_out.csv'

        file = open(fName, 'r')
        out = open(oName, 'w')

        title = file.readline()

        tp = 0
        tn = 0
        fp = 0
        fn = 0

        for line in file:
            tmp = line.strip().split(',')

            pos = int(tmp[0])

            voters = tmp[1:]
            voters = list(map(int, voters))
            voting = 0

            try:
                voting = int(mode(voters))
            except statistics.StatisticsError:
                voting = 3

            if( pos  < 41000):
                if(voting == 1):
                    tp += 1
                else:
                    fn += 1
            else:
                if(voting == 1):
                    fp += 1
                else:
                    tn += 1

            res = str(pos) + ',' + str(voting) + '\n'
            out.write(res)
        # tp tn fp fn
        eOut.write('split,' + str(s) + ',cluster,' + str(num) + ',' + str(tp) + ',' + str(fn) + ',' + str(fp) + ',' + str(tn) + '\n')
        out.close()
eOut.close()