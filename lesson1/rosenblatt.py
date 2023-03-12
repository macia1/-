import dataset
from matplotlib import pyplot as plt
xs,ys = dataset.get_beans(100)
print(xs)
print(ys)

# 配置图像
plt.title("Size-Toxicity Function", fontsize = 12)
plt.xlabel("Bean Size")#设置横坐标的名字
plt.ylabel("Toxicity")#设置纵坐标的名字

plt.scatter(xs,ys)

# 豆豆的毒性
w = 0.5
# y=0.5*x
# 进行一百次训练
for m in range(100):
	for i in range(100):
		x = xs[i]
		y = ys[i]
		# 豆豆的毒性
		y_pre = w * x
		# 实际毒性与计算毒性的误差
		e = y - y_pre
		# 学习率
		alpha = 0.05
		w = w + alpha * e * x
y_pre = w * xs

print(y_pre)

plt.plot(xs, y_pre)


plt.show()