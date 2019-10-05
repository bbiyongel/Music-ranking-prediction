import pandas as pd
from collections import Counter

mydataset = pd.read_csv('dataset.csv', encoding = 'EUC-KR')
print(mydataset.shape)

#빈도수를 보자
mydatalist = []
data1 = mydataset['작곡']
mydatalist += list(data1)
data2 = mydataset['작사']
mydatalist += list(data2)
data3 = mydataset['편곡']
mydatalist += list(data3)
data4 = mydataset['가수']
mydatalist += list(data4)
print(len(mydatalist))

counts = Counter(mydatalist)
print(counts)
