import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 创建主窗口
root = tk.Tk()
root.title("离散信号显示")

# 创建 Figure 和 Axes 对象
fig = plt.Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)

# 创建 Canvas 并将 Figure 嵌入其中
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# 定义绘制离散信号的函数
def plot_discrete_signal1():
    ax.clear()
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    ax.stem(x, y)
    ax.set_title('离散信号 1')
    ax.set_xlabel('时间')
    ax.set_ylabel('幅度')
    canvas.draw()


def plot_discrete_signal2():
    ax.clear()
    x = [1, 2, 3, 4, 5]
    y = [1, 1, 1, 1, 1]
    ax.stem(x, y)
    ax.set_title('离散信号 2')
    ax.set_xlabel('时间')
    ax.set_ylabel('幅度')
    canvas.draw()


# 创建按钮
button1 = tk.Button(root, text="显示离散信号 1", command=plot_discrete_signal1)
button1.pack(side=tk.LEFT, padx=10, pady=10)

button2 = tk.Button(root, text="显示离散信号 2", command=plot_discrete_signal2)
button2.pack(side=tk.LEFT, padx=10, pady=10)

# 运行主循环
root.mainloop()
    