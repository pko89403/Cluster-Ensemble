import pandas as pd


method = ['bbgp', 'gcmh', 'ks']
shape = ['full','tied', ]
kmeans = ['elkan']

opt1 = [[4,6,4,7,5,8],
[4,6,11,7,5,8],
[4,6,10,7,5,7],
[4,7,11,8,5,8],
[4,11,3,9,5,7],
[4,6,3,7,4,8],
[4,6,9,7,5,7],
[4,8,3,8,5,9],
[4,6,3,7,5,8],
[4,6,3,8,5,8]]


opt2 = [[5,5,5],
[5,5,5],
[5,5,5],
[5,5,5],
[5,5,5],
[5,5,5],
[5,5,5],
[5,5,5],
[5,5,5],
[5,5,5]]

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
        labels.to_csv('./1d_split_filtered/1d_split/merging_LOG/merging_' + str(i) + 'OPT.csv', index= False)