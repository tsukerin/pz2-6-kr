import matplotlib.pyplot as plt

x1, y1 = [1000/9, 0], [0, 2000]
x2, y2 = [0, 1000], [0, 3000]
x3, y3 = [0,3000/105], [0, 1000/105]
x4, y4 = [0,1000], [0, 3000] # Задание точек графика
plt.fill_between([0,95.238095],[0,285.71429], color ="g") # Закрашивание внутренней части
plt.fill_between([95.238095,111.11],[285.71429,0],color = "g")
plt.plot(x1, y1, color='black') 
plt.plot(x2, y2, color='r')
plt.xlim(0,500) 
plt.ylim(0,500)
plt.arrow(0,0,300,10,head_width = 5) # Создание стрелки
plt.xlabel("arg x1")
plt.ylabel("arg x2")
plt.title("Решение экстремальных задач")
plt.plot()
plt.legend()
plt.show()