import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import matplotlib.dates as mdates

# 打开文件，查看数据分布
filename = 'sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    for index, colum_head in enumerate(head_row):
        print(index, colum_head)

    # 提取相关信息
    dates, prcps = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2],'%Y-%m-%d')
            prcp = float(row[3])

        except ValueError:
            print("missing value")
        else:
            dates.append(current_date)
            prcps.append(prcp)
# 可视化数据

# 绘制图表
plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, prcps, linewidth=1, color='red')

# 设置标题、标签
plt.title("Death Vally's weather 2018")
plt.xlabel('Date', fontsize=10)
plt.ylabel('Temperature(F)', fontsize=10)
plt.xticks(rotation=45)  # 旋转45°
plt.tick_params(axis='both', labelsize=15)

# 设置日期格式的x轴刻度
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.show()
