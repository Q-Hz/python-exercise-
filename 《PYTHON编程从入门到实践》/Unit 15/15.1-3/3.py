# 模拟花粉在水滴表面的运行路径
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建实例
rw = RandomWalk()
rw.fill_walk()

# 绘制折线图
plt.plot(rw.x_values, rw.y_values, linewidth=1)
plt.scatter(0, 0, color='black', s=40)
plt.scatter(rw.x_values[-1], rw.y_values[-1], color='red', s=40)

# 坐标轴和标题
plt.title("Simulation of the path of pollen in watter")
plt.xlabel("X")
plt.ylabel("Y")

# 坐标轴刻度标记的大小
plt.tick_params(axis='both', labelsize=10)

plt.show()