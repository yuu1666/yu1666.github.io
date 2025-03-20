import numpy as np
import matplotlib.pyplot as plt

# 生成连续余弦信号
t_continuous = np.linspace(0, 2 * np.pi, 1000)
y_continuous = np.cos(t_continuous)

# 生成离散阶跃信号
t_discrete = np.arange(-5, 6)
y_discrete = np.heaviside(t_discrete, 1)

# 绘制连续余弦信号
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(t_continuous, y_continuous)
plt.title('Continuous Cosine Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

# 绘制离散阶跃信号
plt.subplot(1, 2, 2)
plt.stem(t_discrete, y_discrete)
plt.title('Discrete Step Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()