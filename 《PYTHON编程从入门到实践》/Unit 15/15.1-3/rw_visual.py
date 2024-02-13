# 运用random_walk类创建一个可视化随机漫步图
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个RandomWalk类的实例
rw = RandomWalk()
rw.fill_walk()


'''
# 设置绘图窗口的尺寸
plt.figure(dpi=180, figsize=(10, 6))
'''


# 进行颜色映射，画出散点图
'''point_numbers = list(range(rw.num_points))'''
plt.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.Blues, edgecolors='none', s=13)

# 标记起点和终点
plt.scatter(0, 0, color='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], color='red', edgecolors='none', s=100)

# 隐藏坐标轴
plt.xticks([])
plt.yticks([])

plt.show()
