import dataset
import numpy as np
import plot_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

m = 100 
X,Y = dataset.get_beans(m)
plot_utils.show_scatter(X,Y)

model = Sequential()

#units:当前神经元数量
#sigmoid:激活函数类型
#input_dim:输入特征维度
model.add(Dense(units=2,activation='sigmoid',input_dim=2))
model.add(Dense(units=1,activation='sigmoid'))

#loss:代价函数  mean_squared_error(均方误差)
#optimizer:优化器  sgd(随机梯度下降算法)
#metrics:评估标准  accuracy(准确度)
model.compile(loss='mean_squared_error',optimizer=SGD(lr=0.05),metrics=['accuracy'])

#epochs:回合数量
#batch_size:批数量
model.fit(X,Y,epochs=3000,batch_size=10)

#预测
pres = model.predict(X)

plot_utils.show_scatter_surface(X,Y,model)