import pandas as pd


method = ['bbgp', 'gcmh', 'ks']
shape = ['full', 'diag', 'spherical', 'tied', ]

evaluation = './1d_cutoff'

for i in range(1, 11):
    labels = pd.DataFrame()
    for m in method:
           for s in shape:
                PATH = './1d_split/em_1d_' + m + '_' + s +  str(i) +'/em_2.csv'
                OUTPUT = './1d_split/em_2_' +  m + s + str(i) + '.csv'

                preLabel = pd.read_csv(PATH, ',')

                class_min = preLabel.groupby(['label'])[m.upper()].min()
                class_min = class_min.sort_values(ascending=True).tolist()

                j = 1
                for cut in class_min:
                    preLabel.loc[preLabel[m.upper()] >= cut, 'label'] = 3-j
                    j += 1

                labels['pos'] = preLabel['2L_POS']
                labels[m+s] = preLabel['label']

                #preLabel.to_csv(OUTPUT,index=False)


    labels.to_csv('./1d_split/merging_em' + str(i) + '.csv', index= False)