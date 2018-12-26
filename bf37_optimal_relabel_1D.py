import pandas as pd


method = ['bbgp', 'gcmh', 'ks']
shape = ['full','tied', ]
kmeans = ['elkan']

L2_EM = [9,13,8,13,10,13]
R2_EM = [8,14,8,14,11,13]
L3_EM = [10,14,8,14,10,12]
R3_EM = [11,13,10,14,9,13]

L2_KM = [8,8,7]
R2_KM = [8,8,7]
L3_KM = [8,8,7]
R3_KM = [8,8,7]


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
    labels.to_csv('../real/3R/merging_3R_OPT.csv', index= False)