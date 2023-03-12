import dataset
import matplotlib.pyplot as plt
import numpy as np

m = 100
xs,ys = dataset.get_beans(m)
#配置图像
plt.title("Size-Toxicity Function",fontsize=12)#配置标题
plt.xlabel("Bean Size")
plt.ylabel("Toxicity")

plt.scatter(xs,ys)

w = 0.1
b = 0.1
y_pre = w*xs + b

plt.plot(xs,y_pre)

plt.show()

for _ in range(500):
	for i in range(100):
		x = xs[i]
		y = ys[i]
		#a=x^2
		#b=-2*x*y
		#c=y^2
		#斜率k=2aw+b
		dw = 2*x**2*w+2*x*b - 2*x*y
		db = 2*b+2*x*w-2*y
		alpha = 0.1
		w = w - alpha*dw
		b=b-alpha*db

	plt.clf()#清空窗口
	plt.scatter(xs,ys)
	y_pre = w*xs + b
	plt.xlim(0,1)
	plt.ylim(0,1.2)
	plt.plot(xs,y_pre)
	plt.pause(0.01)#暂停0.01s
