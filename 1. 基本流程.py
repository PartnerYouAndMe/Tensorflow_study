import tensorflow as tf

#创建两个常量op
n1=tf.constant([3,3])
n2=tf.constant([2],[3])
#创建一个矩阵乘法op, 把m1和m2传入
product=tf.matmul(n1,n2)
print(product)  #得到一个Tensor类型

#定义一个会话，启动默认图
sess=tf.Session()

result=sess.run(product)
print(result)
sess.close()

#另一种写法
with tf.Session() as sess:
    result=sess.run(product)
    print(result)
