#기본 문법으로 예측해보기
"""
import numpy as np
import pandas as pd

df = pd.DataFrame({'name': ['아이유', '아이즈원', '폴킴', '트와이스', '지코', '존박', '트와이스'],
                   'score': [1, 2, 3, 4, 5, 6, 7]}, columns=['name', 'score'])

df['rank_by_average'] = df['score'].rank(ascending=False)
df['rank_by_min'] = df['score'].rank(method='min', ascending=False)
df['rank_by_max'] = df['score'].rank(method='max', ascending=False)
df['rank_by_first'] = df['score'].rank(method='first', ascending=False)
df['rank_by_dense'] = df['score'].rank(method='dense', ascending=False)

print(df)

'''
#output (점수가 기준이라 순위가 뒤바뀜)
   name  score  rank_by_average  ...  rank_by_max  rank_by_first  rank_by_dense
0   아이유      1              7.0  ...          7.0            7.0            7.0
1  아이즈원      2              6.0  ...          6.0            6.0            6.0
2    폴킴      3              5.0  ...          5.0            5.0            5.0
3  트와이스      4              4.0  ...          4.0            4.0            4.0
4    지코      5              3.0  ...          3.0            3.0            3.0
5    존박      6              2.0  ...          2.0            2.0            2.0
6  트와이스      7              1.0  ...          1.0            1.0            1.0

[7 rows x 7 columns]

'''
"""
#텐서플로우 사용 선형? 비선형?

import pandas as pd
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split

tf.set_random_seed(777)

#데이터 불러오기
mydata = pd.read_csv('../collected_data/가수.csv', encoding = 'EUC-KR')

x = mydata['가수']
y = mydata['rank']
x = x.values.reshape(x.size, 1)
y = y.values.reshape(y.size, 1)

#학습 7 테스트 3비율로 나누기
#train_test_split 를 사용
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=0)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


#모델 학습
X = tf.placeholder(tf.float32, shape=[None, 1])
Y = tf.placeholder(tf.float32, shape=[None, 1])
W = tf.Variable(tf.random_normal(shape=[1, 1]))
b = tf.Variable(tf.random_normal(shape=[1]))
prediction = tf.matmul(X, W) + b

loss = tf.reduce_mean(tf.square(prediction - Y))
optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(loss)

score, score_update_op = tf.metrics.mean_squared_error(Y, prediction)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
sess.run(tf.local_variables_initializer())

epochs = 1001
for epoch_index in range(epochs):
    sess.run(train_op, feed_dict={X: x_train, Y: y_train})

    #모델 검증

    loss_value_train = sess.run(loss, feed_dict={X: x_train, Y: y_train})
    loss_value_test = sess.run(loss, feed_dict={X: x_test, Y: y_test})
    score_value_train = sess.run(score_update_op, feed_dict={X: x_train, Y: y_train})     
    score_value_test = sess.run(score_update_op, feed_dict={X: x_test, Y: y_test})
    print('epoch: {}/{}, train loss: {:.4f}, test loss: {:.4f}, train score: {:.4f}, test score: {:.4f}'.format(
        epoch_index+1, epochs, loss_value_train, loss_value_test, score_value_train, score_value_test))

#모델 예측

y_predict = sess.run(prediction, feed_dict={X: [[1491], [1501], [637]]})
print(y_predict)
print(y_predict.flatten()) 

"""
W1 = tf.get_variable('W1', shape=[1, 1], initializer=tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal(shape=[1]))
net = tf.matmul(X, W1) + b1
net = tf.nn.relu(net)

W2 = tf.get_variable('W2', shape=[1, 1], initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal(shape=[1]))
net = tf.matmul(net, W2) + b2
net = tf.nn.relu(net)

W3 = tf.get_variable('W3', shape=[1, 1], initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal(shape=[1]))
prediction = tf.matmul(net, W3) + b3

loss = tf.reduce_mean(tf.square(prediction - Y))
optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
sess.run(tf.local_variables_initializer())

epochs = 1001
for epoch_index in range(epochs):
    sess.run(train_op, feed_dict={X: x_train, Y: y_train})

#모델 검증

    loss_value_train = sess.run(loss, feed_dict={X: x_train, Y: y_train})
    loss_value_test = sess.run(loss, feed_dict={X: x_test, Y: y_test})     
    print('epoch: {}/{}, train loss: {:.4f}, test loss: {:.4f}'.format(
        epoch_index+1, epochs, loss_value_train, loss_value_test))

#모델 예측

y_predict = sess.run(prediction, feed_dict={X: [[1491], [1501], [637]]})
print(y_predict) #[[8.182088]]
print(y_predict.flatten()) #[8.182088]
print(y_predict.flatten()[0]) #8.182088
"""