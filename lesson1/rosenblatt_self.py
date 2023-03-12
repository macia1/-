import dataset
from matplotlib import pyplot as plt
xs,ys = dataset.get_beans(100)
print(xs)
print(ys)

#绘制图像
#绘制图像名称
plt.title("Size-Toxicity Function",fontsize=12)
#设置横坐标名称
#豆豆大小
plt.xlabel("Bean size")
#设置纵坐标名称
#豆豆毒性
plt.ylabel("Toxicity")
#绘制散点图
plt.scatter(xs,ys)

#y=0.5*x
#学习率
alpha = 0.05
w = 0.5
for m in range(100):
	# 进行一次调整
	for i in range(100):
		x = xs[i]
		y = ys[i]
		#预测结果
		y_pre = w*x
		#预测误差
		e = y - y_pre
		#调整后的新w
		w = w + e * x
		#展示每次结果
y_pre = w * xs
#绘预测制线 arg1自变量,arg2因变量
plt.plot(xs,y_pre)


#展示最终图像
plt.show()