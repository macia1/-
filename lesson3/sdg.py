import dataset
import matplotlib.pyplot as plt
import numpy as np

xs,ys = dataset.get_beans(100)

#配置图像
plt.title("Size-Toxicity Function",fontsize=12)#设置图像名称
plt.xlabel("Bean Size")#设置横坐标名称
plt.ylabel("Toxicity")#设置纵坐标名称

plt.scatter(xs,ys)

w = 0.1
y_pre = w * xs

plt.plot(xs,y_pre)

plt.show()
# 方法一
# for _ in range(100):
# 	for i in range(100):
# 		x = xs[i]
# 		y = ys[i]
# 		#a=x^2
# 		#b=-2*x*y
# 		#c=y^2
# 		#斜率k=2aw+b
# 		k = 2*(x**2)*w + (-2*x*y)
# 		alpha = 0.1
# 		w = w - alpha*k
# 		plt.clf()#清空窗口
# 		plt.scatter(xs,ys)
# 		y_pre = xs*w
# 		plt.xlim(0,1)
# 		plt.ylim (0,1.2)
# 		plt.plot(xs,y_pre)
# 		plt.pause(0.01)#暂停0.01s

# 方法二: 批量梯度下降
# alpha = 0.1
# for _ in range(100):
# 	# 代价函数:e=(y-w*x)^2=x^2*w^2+(-2x*y)*w+y^2
# 	# a=x^2
# 	# b=-2x*y
# 	# 求斜率:k=2aw+b
# 	k = 2*np.sum(xs**2)*w + np.sum(-2*xs*ys)
# 	k = k/100
# 	w = w - alpha*k
# 	y_pre= w*xs
# 	#预测函数图像
# 	plt.clf()
# 	plt.xlim(0,1)
# 	plt.ylim(0,1.2)
# 	plt.plot(xs,y_pre)
# 	plt.scatter(xs,ys)
# 	plt.pause(0.01)

# 方法三:固定步长下降
alpha=0.1
step=0.01
for _ in range(100):
	# 代价函数:e=(y-w*x)^2=x^2*w^2+(-2x*y)*w+y^2
	# a=x^2
	# b=-2x*y
	# c=y^2
	# 求斜率:k=2aw+b
	k = 2*np.sum(xs**2)*w + np.sum(-2*xs*ys)
	k = k/100
	if k>0:
		w = w -step
	else:
		w = w + step
	y_pre=w*xs
	#预测函数图像
	plt.clf()
	plt.xlim(0,1)
	plt.ylim(0,1.2)
	plt.plot(xs,y_pre)
	plt.scatter(xs,ys)
	plt.pause(0.01)
#重新绘制预测图像
# plt.scatter(xs,ys)
# y_pre = w*xs
# plt.plot(xs,y_pre)
# plt.show()