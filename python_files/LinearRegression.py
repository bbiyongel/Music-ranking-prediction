import tensorflow as tf
import pandas as pd

# X and Y data
#데이터 불러오기
mydata = pd.read_csv('../collected_data/가수.csv', encoding = 'EUC-KR')

x = mydata['가수']
y = mydata['rank']
#x = x.values
x = list(map(int, x.values))
y = list(map(int, y.values))
#x = x.values.reshape(x.size, 0)
#y = y.values.reshape(y.size, 1)


X = tf.placeholder(tf.float32, shape=[None])
Y = tf.placeholder(tf.float32, shape=[None])

W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# Our hypothesis XW+b
hypothesis = X * W + b

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.05)
train = optimizer.minimize(cost)

# Launch the graph in a session.
sess = tf.Session()
# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

# Fit the line
for step in range(2001):
    cost_val, W_val, b_val, _ = sess.run([cost, W, b, train],
            feed_dict={X: x, Y: y})
    if step % 20 == 0:
        print(step, cost_val, W_val, b_val)

#Testing our model
print(sess.run(hypothesis, feed_dict={X:[1491]}))
print(sess.run(hypothesis, feed_dict={X: [637]}))
