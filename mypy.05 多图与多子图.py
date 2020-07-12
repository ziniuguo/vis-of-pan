import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 1, 0.1)

y1 = np.exp(x)
y2 = np.exp(2 * x)
y3 = np.exp(1.5 * x)

plt.figure(1)
plt.subplot(1, 2, 1)
plt.plot(x, y1, color="r", linestyle="-", marker="^", linewidth=1)

plt.xlabel("x")
plt.ylabel("y1")

plt.figure(2)  # 生成第二个图，且当前要处理的图为fig.2
plt.plot(x, y2, color="k", linestyle="-", marker="s", linewidth=1)  # 画图，fig.2是一张整图，没有子图，默认subplot（1， 1， 1，）

plt.xlabel("x")
plt.ylabel("y2")

plt.figure(1)  # 当前要处理的图为fig.1,而且当前图是fig.1的左图
plt.subplot(1, 2, 2) #当前图像变为fig.1的右图
plt.plot(x, y3, color="b", linestyle="-", marker="v", linewidth=1)

plt.xlabel("x")
plt.ylabel("y3")


plt.show()
