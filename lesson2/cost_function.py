import dataset
import matplotlib.pyplot as plt
import numpy as np
xs,ys = dataset.get_beans(100)

# 配置图像
plt.title("cost function", fontsize = 12)#设置图像名称
plt.xlabel("Bean Size")#设置横坐标的名字
plt.ylabel("Toxicity")#设置横坐标的名字

plt.scatter(xs,ys)

w = 0.1
y_pre = w*xs

plt.plot(xs,y_pre)
 
plt.show()