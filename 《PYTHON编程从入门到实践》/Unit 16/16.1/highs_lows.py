# 从csv数据中提取最高气温和最低气温
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

filename = 'sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[8])  # 转换为整数
            low = int(row[9])  # 转换为整数
        except ValueError:
            print(current_date, "missing value")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# 绘制图形
plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, color='red', linewidth=0.5)
plt.plot(dates, lows, color='blue', linewidth=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形格式
plt.title("Daily temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=10)
plt.ylabel("Temperature(f)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=8)
plt.xticks(rotation=45)  # 绘制斜的日期标签

# 设置纵坐标的刻度间隔为10
plt.yticks(np.arange(min(lows), max(highs)+10, 10))

# 调整图形布局
plt.subplots_adjust(bottom=0.15)
plt.subplots_adjust(left=0.15)


plt.show()

