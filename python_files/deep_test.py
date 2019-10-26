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

