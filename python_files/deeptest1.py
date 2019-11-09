import pandas as pd
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt

tf.set_random_seed(777)

#데이터 불러오기
mydata = pd.read_csv('../collected_data/가수.csv', encoding = 'EUC-KR')


y = mydata['rank']
X = mydata['가수']

X = X.values.reshape(X.size, 1)
y = y.values.reshape(y.size, 1)

ohe = OneHotEncoder(categorical_features=[0]) # 인텍스 '0'의 데이터를 원핫인코딩함
ohe = ohe.fit_transform(X).toarray() # 원핫인코딩으로 명목변수 변경 후 numpy로 변경
X = ohe
print(X.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=0)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


#placeholder로 자리유지
#생성될 때 값을 가지지 않고 자리유지하는 개념
X = tf.placeholder(tf.float32, [None, 823])
Y = tf.placeholder(tf.float32, [None, 1])

#가중치와 바이어스를 변수로 선언
W = tf.Variable(tf.random_normal([823, 1]))
b = tf.Variable(tf.random_normal([1]))

#활성화 함수로 시그모이드사용
y_out = tf.sigmoid(tf.matmul(X, W) + b)
#손실함수로 '교차 엔트로피 오차' 사용
cost = -tf.reduce_mean(Y * tf.log(y_out) + (1 - Y) * tf.log(1 - y_out))
#경사하강법으로 최소값 찾기
#이미 구현된 경사하강법 라이브러리 사용
#손실함수의 최소값을 구한다.
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

#예측 결과, 정확도 계산
#시그모이드의 결과는 0과 1이사이의 값 이므로 0.5가 넘으면 1로본다.
#실제 y가 1일 때 예측값 1이면 cost감소 예측값 0이면 cost증가
predicted = tf.cast(y_out > 0.5, dtype=tf.float32)
#예측한 값을 정답과 비교 후 평균낸다.
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))
#accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer()) #초기화 후 세션에 전

    for step in range(30):   #반복횟수 간격은 step100으로 설정
        sess.run(train, feed_dict={X: X_train, Y: y_train})
        
        if step % 10 == 0:
            print(step, sess.run(cost, feed_dict={X: X_train, Y: y_train}), sess.run(W))

    # 정확도
    h, c, a = sess.run([y_out, predicted, accuracy], feed_dict={X: X_train, Y: y_train})
    ta = sess.run(accuracy, feed_dict={X: X_test, Y: y_test})
   # print("\y_out: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)
    print("\nTrain Accuracy: ", a,"\nTest Accuracy: ", ta)
    #print(sess.run(accuracy, feed_dict={X: X_test, Y: y_test}))
    #X = np.array([], dtype='f')
    #X = X.reshape(1,50)

    #x_predict = sess.run(predicted, feed_dict={Y: [[1491], [1501], [637]]})
    #print(x_predict)
    #print(x_predict.flatten())