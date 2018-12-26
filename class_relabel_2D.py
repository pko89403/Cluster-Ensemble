import pandas as pd


method = ['bggc']
shape = ['full', 'diag', 'spherical', 'tied', ]


labels = pd.DataFrame()
for m in method:
       for s in shape:
            PATH = './2d_cutoff/em_' + m + '_' + s + '/em_10.csv'
            OUTPUT = './2d_cutoff/em_10_' +  m + s + '.csv'

            preLabel = pd.read_csv(PATH, ',')
            class_min = preLabel.groupby(['label'])['BGGP'].min()
            class_min = class_min.sort_values(ascending=True).tolist()

            i = 1
            for cut in class_min:
                preLabel.loc[preLabel['sum'] >= cut, 'label'] = 11-i
                i += 1

            labels['pos'] = preLabel['2L_POS']
            labels[m+s] = preLabel['label']
            preLabel.to_csv(OUTPUT,index=False)


labels.to_csv('./2d_cutoff/bbgc_relabel.csv')