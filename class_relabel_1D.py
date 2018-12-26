import pandas as pd


method = ['bbgp', 'gcmh', 'ks']
shape = ['full','tied', ]
kmeans = ['elkan']



for i in range(1, 11):
    for c in range(2, 101):
        labels = pd.DataFrame()

        for m in method:
               for s in shape:
                    PATH = './1d_split_filtered/1d_split/em_1d_' + m + '_' + s +  str(i) +'/em_' + str(c) + '.csv'

                    preLabel = pd.read_csv(PATH, ',')

                    class_min = preLabel.groupby(['label'])[m.upper()].min()
                    class_min = class_min.sort_values(ascending=True).tolist()
                    j = 1
                    for cut in class_min:
                        preLabel.loc[preLabel[m.upper()] >= cut, 'label'] = (c+1)-j
                        j += 1

                    labels['pos'] = preLabel['2L_POS']
                    labels[m+s] = preLabel['label']

               for k in kmeans:
                    PATH = './1d_split_filtered/1d_split/kmeans_1d_' + m + '_' + k + str(i) +'/Kmeans' + str(c) + '.csv'

                    preLabel = pd.read_csv(PATH, ',')

                    class_min = preLabel.groupby(['label'])[m.upper()].min()
                    class_min = class_min.sort_values(ascending=True).tolist()
                    j=1
                    for cut in class_min:
                        preLabel.loc[preLabel[m.upper()] >= cut, 'label'] = (c+1)-j
                        j += 1

                    labels['pos'] = preLabel['2L_POS']
                    labels['Km' + m+k] = preLabel['label']

        labels.to_csv('./1d_split_filtered/1d_split/merging_' + str(i) + '_em' + str(c) + '.csv', index= False)