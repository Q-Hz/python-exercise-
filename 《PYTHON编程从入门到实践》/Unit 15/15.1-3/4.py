from random import choice
import matplotlib.pyplot as plt


class RandomWalkTwo:
    """"重构random_walk"""
    def __init__(self, point_number):
        """指定点数，初始化坐标位置"""
        self.point_number = point_number
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """移动的方向和距离"""
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        """移动"""
        while True:
            x_step = self.get_step()
            y_step = self.get_step()
            self.x_values.append(x_step + self.x_values[-1])
            self.y_values.append(y_step + self.y_values[-1])
            if len(self.x_values) >= self.point_number:
                break


rw = RandomWalkTwo(5000)
rw.fill_walk()

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

