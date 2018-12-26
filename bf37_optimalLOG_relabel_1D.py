import pandas as pd


method = ['bbgp', 'gcmh', 'ks']
shape = ['full','tied', ]
kmeans = ['elkan']

L2_EM = [3,6,5,8,5,6]
R2_EM = [4,6,4,8,5,6]
L3_EM = [5,6,5,7,5,6]
R3_EM = [4,5,5,5,4,6]

L2_KM = [5,5,5]
R2_KM = [5,6,5]
L3_KM = [5,6,5]
R3_KM = [5,5,5]


labels = pd.DataFrame()
a = 0
b = 0
for m in method:
    for s in shape:
        PATH = '../real/3R/em_1d_' + m + '_' + s + '/em_' + str(R3_EM[a]) + '.csv'

        preLabel = pd.read_csv(PATH, ',')

        class_min = preLabel.groupby(['label'])[m.upper()].min()
        class_min = class_min.sort_values(ascending=True).tolist()
        j = 1
        for cut in class_min:
            print(cut, R3_EM[a], a)
            preLabel.loc[preLabel[m.upper()] >= cut, 'label'] = (R3_EM[a]+1)-j
            j += 1

            labels['pos'] = preLabel['POS']
            labels[m+s] = preLabel['label']
        a += 1
    for k in kmeans:
        PATH = '../real/3R/kmeans_1d_' + m + '_' + k + '/Kmeans' + str(R3_KM[b]) + '.csv'

        preLabel = pd.read_csv(PATH, ',')

        class_min = preLabel.groupby(['label'])[m.upper()].min()
        class_min = class_min.sort_values(ascending=True).tolist()
        j=1
        for cut in class_min:
            preLabel.loc[preLabel[m.upper()] >= cut, 'label'] = (R3_KM[b]+1)-j
            j += 1

            labels['pos'] = preLabel['POS']
            labels['Km' + m+k] = preLabel['label']
        b+=1
    labels.to_csv('../real/3R/merging_3R_OPT_LOG.csv', index= False)