# 点数相乘
import pygal

from die import Die

# 创建实例
die_1 = Die()
die_2 = Die()

# 掷骰子
results= []
for roll_num in range(50000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die_1.num_sides * die_2.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果
hist = pygal.Bar()
hist.title = "Results of rolling two D6 50,000 times"
hist._x_title = "Result"
hist._y_title = "Frequency of result "
hist.x_labels = []
for value in range(1, die_1.num_sides * die_2.num_sides +1):
    hist.x_labels.append(value)

hist.add('D6 * D6', frequencies)
hist.render_to_file('9.svg')