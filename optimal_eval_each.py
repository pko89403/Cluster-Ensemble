import pandas as pd

eachList = ['bbgpfull','bbgptied','Kmbbgpelkan','gcmhfull','gcmhtied','Kmgcmhelkan','ksfull','kstied','Kmkselkan']
for i in range(1,11):

    fileName = 'E:/paper/simulation/1d_split_filtered/1d_split/merging_LOG/merging_' + str(i) + 'OPT.csv'
    file = pd.read_csv(fileName)
    trueList = file.loc[file['pos'] < 41000]
    falseList = file.loc[file['pos'] > 41000]
	
    for j in eachList:
        tp = len(trueList.loc[trueList[j] == 1])
        fn = len(trueList.loc[trueList[j] != 1])
        fp = len(falseList.loc[falseList[j] == 1])
        tn = len(falseList.loc[falseList[j] != 1])
        print(tp, fn, fp, tn)