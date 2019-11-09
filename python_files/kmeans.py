from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

#get data from csv
Data = pd.read_csv('ksinger20data.csv', encoding = 'EUC-KR')
x = Data['가수']
y = Data['rank']

#Extract freature
feature = Data[['가수','rank']]
feature.head()


#create model and prediction
kmeans = KMeans(n_clusters=4, algorithm ='auto')
kmeans.fit(feature)
predict = pd.DataFrame(kmeans.predict(feature))
predict.columns=['predict']

#concatenate predict
r = pd.concat([feature, predict], axis=1)
print(r)
centers = pd.DataFrame(kmeans.cluster_centers_,columns=['가수','rank'])
center_x = centers['가수']
center_y = centers['rank']

#Visualize result
plt.scatter(r['가수'],r['rank'],c=r['predict'],alpha=0.5)
plt.scatter(center_x,center_y,s=50,marker='D',c='r')

#scatter plot
plt.grid(True)
plt.show()
