import dataset
from matplotlib import pyplot as plt
xs,ys=dataset.get_beans(100)
print(xs)
print(ys)

#图像展示
plt.title("Size-Toxicity Function",fontsize=12)#图像标题
plt.xlabel("Bean size")#横坐标名称
plt.ylabel("Toxicity")#纵坐标名称
#绘制散点图
plt.scatter(xs,ys)

#y=0.5*x
w = 0.5
y_pre = w * xs
print(y_pre)
#绘制线 arg1自变量，arg2因变量
plt.plot(xs,y_pre)

plt.show()