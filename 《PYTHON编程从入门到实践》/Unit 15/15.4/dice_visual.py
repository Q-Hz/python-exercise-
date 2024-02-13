# 两个骰子
import pygal

from die import Die

# 创建两个实例
die_1 = Die()
die_2 = Die()

# 掷骰子多次，存储到一个列表
results = []
for roll_num in range(1001):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
freguencies = []
for value in range(2,die_1.num_sides+die_2.num_sides+1):
    freguency = results.count(value)
    freguencies.append(freguency)

# 可视化结果
hist = pygal.Bar()
hist.x_labels = []  # 初始化
for label in range(2, die_1.num_sides + die_2.num_sides + 1):
    hist.x_labels.append(label)
hist.title = "Result of rolling two D6 dice 1000 times"
hist._x_title = "Result"
hist._y_title = "Frequency of result"

hist.add('D6 + D6', freguencies)
hist.render_to_file('dice_visual.svg')