#불필요한 문자가 제거된 데이터는 문자열이기 때문에
#머신러닝을 위해 임의로 숫자로 된 라벨을 붙임

import pandas as pd
from collections import Counter
import numpy as np
mydataset = pd.read_csv('../collected_data/dataset2.csv', encoding = 'EUC-KR')
print(mydataset.shape)


mydatalist = []
data1 = list(mydataset['작곡'])
mydatalist += data1
data2 = list(mydataset['작사'])
mydatalist += data2
data3 = list(mydataset['편곡'])
mydatalist += data3
data4 = list(mydataset['가수'])
mydatalist += data4
mydatalist = list(set(mydatalist))

new_list = []

for i in range(0, len(mydatalist)):
        
    temp = []
    temp.append(mydatalist[i])
    new_list += temp

new_list = list(map(str, new_list))
new_list = sorted(new_list)


#인덱스 저장
#data = pd.DataFrame(new_list)
#data.to_csv('index_num.txt', mode='a', encoding='utf-8',header=None)


for data_cg in data4:
    #문자열을 숫자로(라벨 붙이기)
    temp2 = []
    temp2.append(new_list.index(str(data_cg)))#인덱스 찾기
    #이름을 인덱스 번호로 바꿔주고 저장, 새로운 dataset만들기
    data = pd.DataFrame(temp2)
    data.to_csv('가수.txt', mode='a', encoding='utf-8',header=None)
