import pandas as pd

method = ['bbgp', 'gcmh', 'ks']
shape = ['full', 'tied', ]
kmeans = ['elkan']

for i in range(1, 11):
    labels = pd.DataFrame()

    for m in method:
        for s in shape:
            PATH = './1d_split_filtered/1d_split/em_1d_' + m + '_' + s + str(i) + '/em_' + m.upper() + '_101.csv'
            em = open(PATH, 'r')
            emList = []
            for line in em:
                emList.append(line.strip().split(',\t')[0])

            em.close()
            print('em' + m + s, len(emList))
            labels['em' + m + s] = emList

        for k in kmeans:
            PATH = './1d_split_filtered/1d_split/kmeans_1d_' + m + '_' + k + str(i) + '/KMEANS_' + m.upper() + '_' + str(i) + '.csv'
            kmean = open(PATH, 'r')
            kmeansList = []
            for line in kmean:
                kmeansList.append(line.strip())

            kmean.close()
            labels['kmeans' + m + k] = kmeansList

    labels.to_csv('./1d_split_filtered/1d_split/model_measure' + str(i) + '.csv', index=False)