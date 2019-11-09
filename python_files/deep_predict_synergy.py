#텐서플로우 사용 선형? 비선형?
import pandas as pd
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

tf.set_random_seed(777)

#데이터 불러오기
mydata = pd.read_csv('../collected_data/index_all.csv', encoding = 'EUC-KR')

x = mydata[['가수', '작사', '작곡', '편곡']]
y = mydata['rank']
#x = x.values.reshape(x.size, 1)
y = y.values.reshape(y.size, 1)

print(x.shape)
print(y.shape)
#학습 7 테스트 3비율로 나누기
#train_test_split 를 사용
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=0)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

#모델 학습

X = tf.placeholder(tf.float32, shape=[None, 4])
Y = tf.placeholder(tf.float32, shape=[None, 1])
W = tf.Variable(tf.random_normal(shape=[4, 1]))
b = tf.Variable(tf.random_normal(shape=[1]))
prediction = tf.matmul(X, W) + b


loss = tf.reduce_mean(tf.square(prediction - Y))
optimizer = tf.train.AdamOptimizer(learning_rate=0.05)
train_op = optimizer.minimize(loss)

score, score_update_op = tf.metrics.mean_squared_error(Y, prediction)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
sess.run(tf.local_variables_initializer())

test_graph= []
train_graph= []

epochs = 150
for epoch_index in range(epochs):
    sess.run(train_op, feed_dict={X: x_train, Y: y_train})

    #모델 검증
    
    loss_value_train = sess.run(loss, feed_dict={X: x_train, Y: y_train})
    loss_value_test = sess.run(loss, feed_dict={X: x_test, Y: y_test})

    test_graph.append(loss_value_test)
    train_graph.append(loss_value_train)
    
    score_value_train = sess.run(score_update_op, feed_dict={X: x_train, Y: y_train})     
    score_value_test = sess.run(score_update_op, feed_dict={X: x_test, Y: y_test})
    print('epoch: {}/{}, train loss: {:.4f}, test loss: {:.4f}, train score: {:.4f}, test score: {:.4f}'.format(
        epoch_index+1, epochs, loss_value_train, loss_value_test, score_value_train, score_value_test))

#모델 예측
temp1 = int(0) #가수
temp2 = int(1491) #작곡
temp3 = int(1491) #작사
temp4 = int(837) #편곡
temp_data = ((temp1, temp2, temp3, temp4), )
temp_arr = np.array(temp_data, dtype=np.float32)
x_data = temp_arr[0:4]

y_predict = sess.run(prediction, feed_dict={X: x_data})
print(y_predict)
print(y_predict.flatten()) 

#print('Accuracy :', accuracy.eval({X:x_test, Y:y_test}))

test_num = range(len(test_graph))
train_num = range(len(train_graph))

plt.plot(test_num, test_graph, 'r--')
plt.plot(train_num, train_graph, 'b-')
plt.legend(['loss_value_test','loss_value_train'])
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()
