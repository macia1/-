import dataset
import matplotlib.pyplot as plt
import numpy as np
#获取豆豆大小和毒性
xs,ys = dataset.get_beans(100)

#配置图像
#配置图像标题
plt.title("Size-Toxicity Function",fontsize=12)
#配置图像横坐标名称
plt.xlabel("Bean Size")
#配置图像纵坐标名称
plt.ylabel("Toxicity")
#绘制散点图
plt.scatter(xs,ys)

w = 0.1
y_pre = w * xs
#绘制预测线
plt.plot(xs,y_pre)

#展示图像
plt.show()

#均方误差
es = (ys-y_pre)**2
sum_e = np.sum(es)
sum_e = (1/100)*sum_e
print(sum_e)

# 模拟w不同时方差变化
es = []
ws = np.arange(0,3,0.1)
for w in ws:
	y_pre = w*xs
	e = (1/100)*np.sum((ys - y_pre)**2)
	print("w:"+str(w)+" e:" + str(e))
	es.append(e)

#用抛物线顶点坐标公式求解最低点的w
w_min = np.sum(xs*ys)/np.sum(xs*xs)
print("e最小点w的值:"+str(w_min))

#绘制w和方差e的图像（代价函数图像）
plt.title("Cost Function",fontsize=12)
plt.xlabel("w")
plt.ylabel("e")
plt.plot(ws,es)
plt.show()

#将计算出的最低w带回预测函数
plt.title("Size-Toxicity(w value is min)",fontsize=12)
plt.xlabel("Bean size")
plt.ylabel("Toxicity")
#真实对应关系
plt.scatter(xs,ys)

y_pre = w_min*xs

#预测曲线
plt.plot(xs,y_pre)

plt.show()
