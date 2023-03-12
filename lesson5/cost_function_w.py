import dataset
import matplotlib.pyplot as plt
import numpy as np

m = 100

#配置图像
plt.title("Size-Toxicity Function",fontsize=12)#配置标题
plt.xlabel("Bean Size")
plt.ylabel("Toxicity")
plt.xlim(0,1)
plt.ylim(0,1.5)

plt.scatter(xs,ys)
plt.show()