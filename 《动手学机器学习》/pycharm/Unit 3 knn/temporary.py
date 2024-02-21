import matplotlib.pyplot as plt
import numpy as np
import os

# 读入MNISt数据集
m_x = np.loadtxt('mnist_x.txt', delimiter=' ')
m_y = np.loadtxt('mnist_y.txt')

# 数据集可视化
data = np.reshape(np.array(m_x[0], dtype=int), [28, 28])
plt.figure()
plt.imshow(data, cmap='gray')
plt.show()

# 将数据集分为训练集和测试集
ratio = 0.8
split = int(len(m_x) * ratio)

# 打乱数据
np.random.seed(0)
idx = np.random.permutation(np.arange(len(m_x)))  # 将len（m_x)个数随机排列
m_x = m_x[idx]  # 对原数组随机排列，且保证排列后每一个数据与标签仍一一对应
m_y = m_y[idx]
x_train, x_test = m_x[:split], m_x[split:]
y_train, y_test = m_y[:split], m_y[split:]

