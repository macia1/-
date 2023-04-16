from keras.datasets import mnist
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import matplotlib.pyplot as plt
from keras.utils import to_categorical

# 加载测试数据
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
print("X_train.shape:"+str(X_train.shape))
print("Y_train.shape:"+str(X_train.shape))
print("X_test.shape:"+str(X_train.shape))
print("Y_test.shape:"+str(X_train.shape))

# 第一个样本的值
print(Y_train[0])
# 绘制样本, 绘图模式 灰度图(gray )
plt.imshow(X_train[0], cmap='gray')
plt.show()

X_train = X_train.reshape(60000, 784)/255.0
X_test = X_test.reshape(10000, 784)/255.0

Y_train = to_categorical(Y_train, 10)
Y_test = to_categorical(Y_test, 10)
model = Sequential()
# units:当前神经元数量
# sigmoid:激活函数类型
# input_dim:输入特征维度
model.add(Dense(units=256, activation='relu', input_dim=784))
model.add(Dense(units=256, activation='relu'))
model.add(Dense(units=256, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

# loss:代价函数  categorical_crossentropy(多分类交叉熵代价函数) 多分类处理
# optimizer:优化器  sgd(随机梯度下降算法)
# metrics:评估标准  accuracy(准确度)
model.compile(loss='categorical_crossentropy',
              optimizer=SGD(lr=0.05), metrics=['accuracy'])

# epochs:回合数量
# batch_size:批数量
model.fit(X_train, Y_train, epochs=100, batch_size=4096)

# 评估
loss, accuracy = model.evaluate(X_test, Y_test)
print("loss:"+str(loss))
print("accuracy:"+str(accuracy))
