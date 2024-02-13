# 散点图，显示前五个整数的立方
import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_values = [y**2 for y in x_values]
plt.scatter(x_values, y_values, color=(1, 0, 0), s=20)

# 标题，坐标轴
plt.title("Cube", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Cube of Values", fontsize=14)

# 刻度标记大小
plt.tick_params(axis='both', labelsize=14)

plt.show()


# 散点图 显示前5000个数的平方
import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [y**3 for y in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.twilight, s=20)

# 标题，坐标轴
plt.title("Cube", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of values", fontsize=14)

# 坐标轴刻度大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig('Cube.png')