import matplotlib.pyplot as plt
import numpy as np

x1, y1 = [1000/9, 0], [0, 2000]
x2, y2 = [0, 1000], [0, 3000]
x3, y3 = [0,3000/105], [0, 1000/105]
x4, y4 = [0,1000], [0, 3000] # Задание точек графика
plt.fill_between([0,95.238095],[0,285.71429], color ="silver") # Закрашивание внутренней части
plt.fill_between([95.238095,111.11],[285.71429,0],color = "silver")
plt.plot(x1, y1, color='black') 
plt.plot(x2, y2, color='r')
plt.xlim(-20,500) 
plt.ylim(-20,500)
plt.arrow(0,0,300,10,head_width = 5) # Создание стрелки
plt.text(271, 23, "z(30;1)", fontsize=10)
plt.text(67, 378, "y=2000-18x", fontsize=10, rotation=95)
plt.text(140, 397, "y=3x", fontsize=10, rotation=68)
x1_green = np.linspace(-3, 3, 100)
plt.plot(x1_green, -30 * x1_green, linestyle='-.', color='green')
plt.xlabel("arg x1")
plt.ylabel("arg x2")
plt.title("Решение экстремальных задач")
plt.plot()
plt.legend()
plt.show()