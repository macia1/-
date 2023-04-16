from keras.datasets import mnist
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import matplotlib.pyplot as plt
from keras.utils import to_categorical
from keras.layers import Conv2D
from keras.layers import AveragePooling2D
from keras.layers import Flatten


# 加载测试数据
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# 第一个样本的值
print(Y_train[0])
# 绘制样本, 绘图模式 灰度图(gray )
plt.imshow(X_train[0], cmap='gray')
plt.show()

X_train = X_train.reshape(60000, 28, 28, 1)/255.0
X_test = X_test.reshape(10000, 28, 28, 1)/255.0

Y_train = to_categorical(Y_train, 10)
Y_test = to_categorical(Y_test, 10)

model = Sequential()
# filters 卷积核/过滤器数量
# kernel_size 卷积核尺寸
# strides 步长
# input_shape 输入形状
# padding 填充模式
# activation 激活函数
model.add(Conv2D(filters=6, kernel_size=(5, 5), strides=(1, 1),
          input_shape=(28, 28, 1), padding='valid', activation='relu'))
model.add(AveragePooling2D(pool_size=(2, 2)))
model.add(Conv2D(filters=16, kernel_size=(5, 5), strides=(
    1, 1), padding='valid', activation='relu'))
model.add(AveragePooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(units=120, activation='relu'))
model.add(Dense(units=84, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

# loss:代价函数  categorical_crossentropy(多分类交叉熵代价函数) 多分类处理
# optimizer:优化器  sgd(随机梯度下降算法)
# metrics:评估标准  accuracy(准确度)
model.compile(loss='categorical_crossentropy',
              optimizer=SGD(lr=0.05), metrics=['accuracy'])

# epochs:回合数量
# batch_size:批数量
# 送入训练
model.fit(X_train, Y_train, epochs=100, batch_size=4096)

# 评估测试集
loss, accuracy = model.evaluate(X_test, Y_test)
print("loss:"+str(loss))
print("accuracy:"+str(accuracy))
