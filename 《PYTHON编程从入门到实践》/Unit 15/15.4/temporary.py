# 模拟掷骰子
from die import Die
import matplotlib.pyplot as plt

# 创建一个D6
die = Die()

# 掷几次骰子， 并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
plt.bar(list(range(1, die.num_sides + 1)), frequencies)
plt.title("Results of rolling one D6 1000 times.")
plt.xlabel("Result")
plt.ylabel("Frequency of Result")

plt.show()