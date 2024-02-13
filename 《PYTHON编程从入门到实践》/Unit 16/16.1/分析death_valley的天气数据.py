# 分析death_valley的天气数据(最高温、最低温)

import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

# 打开文件，查看数据分布
filename = 'death_valley_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    for index, colum_head in enumerate(head_row):
        print(index, colum_head)

    # 提取相关信息
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2],'%Y-%m-%d')
            high = int(row[6])
            low = int(row[7])
        except ValueError:
            print("missing value")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 可视化数据

# 绘制图表
plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, linewidth=1, color='red')
plt.plot(dates, lows, linewidth=1, color='green')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.3)

# 设置标题、标签
plt.title("Death Vally's weather 2018")
plt.xlabel('Date', fontsize=10)
plt.ylabel('Temperature(F)', fontsize=10)
plt.xticks(rotation=45)  # 旋转45°
plt.tick_params(axis='both', labelsize=15)
plt.yticks(np.arange(min(lows), max(highs)+10, 10))  # 设置纵坐标的刻度间隔为10

plt.show()
