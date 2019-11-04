import pandas as pd
import tensorflow as tf
import numpy as np

#xy = pd.read_csv('rank6.csv', encoding = 'EUC-KR') #csv파일 받아오기 np랑pd랑 리스트 자리기 다른
xy = np.loadtxt('rank6.csv', delimiter=',', dtype=np.int32)
print(xy) #세로 기본행렬
print(xy.T) #가로행렬로 변경

x_data = xy.T[:0:-1] #x_data 자르기
y_data = xy.T[:,[-1]] #y_data 자르기

print(x_data)
print("================")
print(y_data)
