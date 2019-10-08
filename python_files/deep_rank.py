#불필요한 문자가 제거된 데이터는 문자열이기 때문에
#머신러닝을 위해 임의로 숫자로 된 라벨을 붙임

import pandas as pd
from collections import Counter
import numpy as np
mydataset = pd.read_csv('dataset2.csv', encoding = 'EUC-KR')
print(mydataset.shape)

#빈도수를 보자
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
#print(mydatalist)

new_list = []

for i in range(0, len(mydatalist)):
        
    temp = []
    temp.append(mydatalist[i])
    temp.append(i)
    new_list.append(temp)


new_list = np.array(new_list)
slice_col = list(new_list[:,0]) #열만 자르기
#인덱스 저장
#data = pd.DataFrame(new_list)
#data.to_csv('index_num.txt', mode='a', encoding='utf-8',header=None)

for data_cg in data4:
    #문자열을 숫자로(라벨 붙이기)
    temp2 = []
    temp2.append(slice_col.index(str(data_cg)))#인덱스 찾기
    #파일 이름을 인덱스 번호로 바꿔주고 저장, 새로운 dataset만들기
    data = pd.DataFrame(temp2)
    data.to_csv('가수.txt', mode='a', encoding='utf-8',header=None)
