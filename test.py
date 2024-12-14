import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# different from yours, see below
x = np.arange(1, 5)
y = np.arange(1, 6)
z = np.arange(1, 5)
# x = y = z = np.linspace(-2, 2, 41)
print('x=', x)
print('y=', y)
print('z=', z)
X, Y, Z = np.meshgrid(x, y, z)
print('X=', X)
print('Y=', Y)
print('Z=', Z)
values = X ** 3 * Y ** 2 * Z

# values = np.log(X * X * X * Y * Y * Z)
# values = values * values

# values = X * X * X * Y * Y * Z
# values = 2 * X * X - Y * Y + 1 / (Z * Z + 1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('P')
ax.set_ylabel('C')
ax.set_zlabel('B')
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
# ax.

scatter = ax.scatter(X, Y, Z, c=values, s=values, cmap='spring_r')
fig.colorbar(scatter, ax=ax)

plt.show()
