import pandas as pd


method = ['bbgp', 'gcmh', 'ks']
shape = ['full','tied', ]
kmeans = ['elkan']

opt1 = [[6,14,13,16,13,12],
[6,15,11,11,12,13],
[6,15,13,14,12,13],
[6,13,12,13,10,11],
[6,15,11,10,11,12],
[7,14,11,12,11,11],
[7,15,10,12,11,13],
[7,14,10,14,11,11],
[9,12,9,14,11,13],
[6,14,12,11,12,12],
[6,13,11,12,10,12],
[6,13,11,14,12,13],
[6,14,11,12,12,13],
[7,14,10,11,11,12],
[6,14,10,14,12,12],
[7,14,15,11,11,12]]


opt2 = [[8,9,8],
[8,9,7],
[8,9,8],
[8,8,8],
[8,9,8],
[8,9,7],
[8,9,7],
[8,9,8],
[8,8,7],
[8,9,7],
[9,9,7],
[8,9,8],
[8,9,7],
[8,7,8],
[8,9,7],
[8,9,7]]


for i in range(1, 17):
        labels = pd.DataFrame()
        a = 0
        b = 0
        for m in method:
               for s in shape:
                    PATH = '../LTE_CLUSTER/cluster/em_1d_' + m + '_' + s +  str(i) +'/em_' + str(opt1[i-1][a]) + '.csv'
                    print(PATH)
                    preLabel = pd.read_csv(PATH, ',')

                    if( m == 'ks'):
                        class_max = preLabel.groupby(['label'])[m.upper()].max()
                        class_max = class_max.sort_values(ascending=False).tolist()
                        j = 1
                        for cut in class_max:
                            preLabel.loc[preLabel[m.upper()] <= cut, 'label'] = (opt1[i-1][a]+1)-j
                            j += 1
                    else:
                        class_min = preLabel.groupby(['label'])[m.upper()].min()
                        class_min = class_min.sort_values(ascending=True).tolist()
                        j = 1
                        for cut in class_min:
                            preLabel.loc[preLabel[m.upper()] >= cut, 'label'] = (opt1[i-1][a]+1)-j
                            j += 1

                    labels['pos'] = preLabel['POS']
                    labels[m+s] = preLabel['label']
                    a += 1
               for k in kmeans:
                    PATH = '../LTE_CLUSTER/cluster/kmeans_1d_' + m + '_' + k + str(i) +'/Kmeans' + str(opt2[i-1][b]) + '.csv'

                    preLabel = pd.read_csv(PATH, ',')

                    if( m == 'ks'):
                        class_max = preLabel.groupby(['label'])[m.upper()].max()
                        class_max = class_max.sort_values(ascending=False).tolist()
                        j = 1
                        for cut in class_max:
                            preLabel.loc[preLabel[m.upper()] <= cut, 'label'] = (opt2[i-1][b]+1)-j
                            j += 1

                    else:
                        class_min = preLabel.groupby(['label'])[m.upper()].min()
                        class_min = class_min.sort_values(ascending=True).tolist()
                        j=1
                        for cut in class_min:
                            preLabel.loc[preLabel[m.upper()] >= cut, 'label'] = (opt2[i-1][b]+1)-j
                            j += 1

                    labels['pos'] = preLabel['POS']
                    labels['Km' + m+k] = preLabel['label']
                    b+=1
        labels.to_csv('../LTE_CLUSTER/merging_' + str(i) + 'OPT.csv', index= False)