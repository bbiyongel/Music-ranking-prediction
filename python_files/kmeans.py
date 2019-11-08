from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

#get data from csv
Data = pd.read_csv('../collected_data/kmeandata.csv', encoding = 'EUC-KR')
x = Data['rank']
y = Data['가수']

#Extract freature
feature = Data[['rank','가수']]
feature.head()


#create model and prediction
kmeans = KMeans(n_clusters=4, algorithm ='auto')
kmeans.fit(feature)
predict = pd.DataFrame(kmeans.predict(feature))
predict.columns=['predict']

#concatenate predict
r = pd.concat([feature, predict], axis=1)
print(r)

centers = pd.DataFrame(kmeans.cluster_centers_,columns=['rank','가수'])
center_x = centers['rank']
center_y = centers['가수']

#Visualize result
plt.scatter(r['rank'],r['가수'],c=r['predict'],alpha=0.5)
plt.scatter(center_x,center_y,s=50,marker='D',c='r')

#scatter plot
plt.grid(True)
plt.show()
