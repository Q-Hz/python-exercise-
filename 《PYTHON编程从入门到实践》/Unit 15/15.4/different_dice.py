# 掷一个六面和一个十面的骰子
import pygal

from die import Die

# 创建实例
die_1 = Die()
die_2 = Die(10)

# 存储结果
results = []
for roll_num in range(1, 50001):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(2, die_1.num_sides + die_2.num_sides):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# 可视化结果
hist = pygal.Bar()
hist.title = "Result of rolling a D6 and D10 50,000 times"
hist.x_title = "result"
hist.y_title = "Frequency of result"
hist.x_labels = []
for value in range(2, die_1.num_sides + die_2.num_sides):
    hist.x_labels.append(value)

hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice.svg')