import pandas as pd


method = ['bbgp', 'gcmh', 'ks']
shape = ['full','tied', ]
kmeans = ['elkan']

opt1 = [[8,14,27,13,9,14],
[11,14,32,13,6,14],
[10,15,29,14,7,15],
[9,15,32,13,8,14],
[10,14,28,13,8,13],
[9,14,28,13,8,13],
[8,15,28,13,7,14],
[9,14,23,11,8,15],
[9,14,30,13,6,14],
[6,14,28,14,8,14]]

opt2 = [[8,8,7],
[8,8,7],
[8,8,8],
[8,7,7],
[8,8,7],
[8,7,7],
[8,8,7],
[8,5,7],
[8,8,7],
[8,8,7]]

for i in range(1, 11):
        labels = pd.DataFrame()
        a = 0
        b = 0
        for m in method:
               for s in shape:
                    PATH = './1d_split_filtered/1d_split/em_1d_' + m + '_' + s +  str(i) +'/em_' + str(opt1[i-1][a]) + '.csv'

                    preLabel = pd.read_csv(PATH, ',')

                    class_min = preLabel.groupby(['label'])[m.upper()].min()
                    class_min = class_min.sort_values(ascending=True).tolist()
                    j = 1
                    for cut in class_min:
                        preLabel.loc[preLabel[m.upper()] >= cut, 'label'] = (opt1[i-1][a]+1)-j
                        j += 1

                    labels['pos'] = preLabel['2L_POS']
                    labels[m+s] = preLabel['label']
                    a += 1
               for k in kmeans:
                    PATH = './1d_split_filtered/1d_split/kmeans_1d_' + m + '_' + k + str(i) +'/Kmeans' + str(opt2[i-1][b]) + '.csv'

                    preLabel = pd.read_csv(PATH, ',')

                    class_min = preLabel.groupby(['label'])[m.upper()].min()
                    class_min = class_min.sort_values(ascending=True).tolist()
                    j=1
                    for cut in class_min:
                        preLabel.loc[preLabel[m.upper()] >= cut, 'label'] = (opt2[i-1][b]+1)-j
                        j += 1

                    labels['pos'] = preLabel['2L_POS']
                    labels['Km' + m+k] = preLabel['label']
                    b+=1
        labels.to_csv('./1d_split_filtered/1d_split/merging_' + str(i) + 'OPT.csv', index= False)