import matplotlib.pyplot as plt
import numpy as np

step = 0.5
fontsize = 9
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x = np.arange(0, 12 + step, step)
x1 = np.arange(0, 9 + step, step)
x2 = np.arange(0, 12 + step, step)
x3 = np.arange(12, 22 + step, step)
x4 = np.arange(9, 13 + step, step)
x5 = 22
x6 = np.arange(22, 30 + step, step)
x7 = np.arange(22, 31 + step, step)
x8 = np.arange(31, 39 + step, step)
x9 = np.arange(31, 36 + step, step)
x10 = np.arange(39, 42 + step, step)

y = 1 + x * 0
y1 = 2 + x1 * 0
y2 = 3 + x2 * 0
y3 = 4 + x3 * 0
y4 = 5 + x4 * 0
y5 = 6 + x5 * 0
y6 = 7 + x6 * 0
y7 = 8 + x7 * 0
y8 = 9 + x8 * 0
y9 = 10 + x9 * 0
y10 = 11 + x10 * 0

plt.text(0, 1.1, '(p(0),p(1) 5', fontsize=fontsize)
ax.plot(x, y, 'k')
plt.text(0, 2.1, '(p(0),p(2) 2', fontsize=fontsize)
ax.plot(x1, y1, 'k')
plt.text(0, 3.1, '(p(0),p(6) 3', fontsize=fontsize)
ax.plot(x2, y2, 'k')
plt.text(12, 4.1, '(p(1),p(3) 9', fontsize=fontsize)
ax.plot(x3, y3, 'k')
plt.text(9, 5.1, '(p(2),p(4) 1', fontsize=fontsize)
ax.plot(x4, y4, 'k')
plt.text(22, 6.1, '(p(3),p(4)', fontsize=fontsize)
ax.plot(x5, y5, 'k.')
plt.text(22, 7.1, '(p(3),p(7) 4', fontsize=fontsize)
ax.plot(x6, y6, 'k')
plt.text(22, 8.1, '(p(4),p(5) 2', fontsize=fontsize)
ax.plot(x7, y7, 'k')
plt.text(31, 9.1, '(p(5),p(6) 5', fontsize=fontsize)
ax.plot(x8, y8, 'k')
plt.text(31, 10.1, '(p(5),p(7) 5', fontsize=fontsize)
ax.plot(x9, y9, 'k')
plt.text(39, 11.1, '(p(6),p(7) 3', fontsize=fontsize)
ax.plot(x10, y10, 'k')
plt.minorticks_on()
plt.title('Рисунок 1')
plt.grid(True)

plt.xticks(np.arange(0, 48, 2), np.arange(0, 48, 2))
plt.yticks(np.arange(0, 13, 1), np.arange(0, 13, 1))
plt.xlabel('Время')
plt.ylabel('Работы')
plt.show()
fig.savefig("рисунок 1.png", dpi=300, qualite=100)

x = np.arange(0, 12 + step, step)
x1 = np.arange(9, 18 + step, step)
x2 = np.arange(27, 39 + step, step)
x3 = np.arange(12, 22 + step, step)
x4 = np.arange(18, 22 + step, step)
x5 = 22
x6 = np.arange(34, 42 + step, step)
x7 = np.arange(22, 31 + step, step)
x8 = np.arange(31, 39 + step, step)
x9 = np.arange(37, 42 + step, step)
x10 = np.arange(39, 42 + step, step)

fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
y = 1 + x * 0
y1 = 2 + x1 * 0
y2 = 3 + x2 * 0
y3 = 4 + x3 * 0
y4 = 5 + x4 * 0
y5 = 6 + x5 * 0
y6 = 7 + x6 * 0
y7 = 8 + x7 * 0
y8 = 9 + x8 * 0
y9 = 10 + x9 * 0
y10 = 11 + x10 * 0

plt.text(0, 1.1, '(p(0),p(1) 5', fontsize=fontsize)
ax1.plot(x, y, 'k')
plt.text(9, 2.1, '(p(0),p(2) 2', fontsize=fontsize)
ax1.plot(x1, y1, 'k')
plt.text(27, 3.1, '(p(0),p(6) 3', fontsize=fontsize)
ax1.plot(x2, y2, 'k')
plt.text(12, 4.1, '(p(1),p(3) 9', fontsize=fontsize)
ax1.plot(x3, y3, 'k')
plt.text(18, 5.1, '(p(2),p(4) 1', fontsize=fontsize)
ax1.plot(x4, y4, 'k')
plt.text(22, 6.1, '(p(3),p(4)', fontsize=fontsize)
ax1.plot(x5, y5, 'k.')
plt.text(34, 7.1, '(p(3),p(7) 4', fontsize=fontsize)
ax1.plot(x6, y6, 'k')
plt.text(22, 8.1, '(p(4),p(5) 2', fontsize=fontsize)
ax1.plot(x7, y7, 'k')
plt.text(31, 9.1, '(p(5),p(6) 5', fontsize=fontsize)
ax1.plot(x8, y8, 'k')
plt.text(37, 10.1, '(p(5),p(7) 5', fontsize=fontsize)
ax1.plot(x9, y9, 'k')
plt.text(39, 11.1, '(p(6),p(7) 3', fontsize=fontsize)
ax1.plot(x10, y10, 'k')
plt.minorticks_on()
plt.title('Рисунок 2')
plt.grid(True)

plt.xticks(np.arange(0, 48, 2), np.arange(0, 48, 2))
plt.yticks(np.arange(0, 13, 1), np.arange(0, 13, 1))
plt.xlabel('Время')
plt.ylabel('Работы')
plt.show()
fig1.savefig("рисунок 2.png", dpi=300, qualite=100)
