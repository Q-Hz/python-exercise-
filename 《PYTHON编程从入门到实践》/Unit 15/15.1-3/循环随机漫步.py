# 运用random_walk类创建一个可视化随机漫步图
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个RandomWalk类的实例
# 只要程序处于活动状态，就不断模拟随机漫步
while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, )
    plt.show()

    keep_running = input("Make another walk?(y/n) ")
    if keep_running == 'n':
        break