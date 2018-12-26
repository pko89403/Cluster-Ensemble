import pandas as pd

method = ['bbgp', 'gcmh', 'ks']
shape = ['full', 'tied', ]
kmeans = ['elkan']

for i in range(1, 17):
    labels = pd.DataFrame()

    for m in method:
        for s in shape:
            PATH = '../LTE_CLUSTER/cluster/em_1d_' + m + '_' + s + str(i) + '/em_' + m.upper() + '_101.csv'
            em = open(PATH, 'r')
            emList = []
            for line in em:
                emList.append(line.strip().split(',\t')[0])

            em.close()
            print('em' + m + s, len(emList))
            labels['em' + m + s] = emList

        for k in kmeans:
            PATH = '../LTE_CLUSTER/cluster/kmeans_1d_' + m + '_' + k + str(i) + '/KMEANS_' + m.upper() + '_' + str(i) + '.csv'
            kmean = open(PATH, 'r')
            kmeansList = []
            for line in kmean:
                kmeansList.append(line.strip())

            kmean.close()
            labels['kmeans' + m + k] = kmeansList

    labels.to_csv('../LTE_CLUSTER/model_measure' + str(i) + '.csv', index=False)