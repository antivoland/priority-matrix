import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
from matplotlib.widgets import Button, Slider

u_pow = 3
i_pow = 2
b_pow = 1

u = np.arange(1, 5)
i = np.arange(1, 6)
b = np.arange(1, 4)
print('x=', u)
print('y=', i)
print('z=', b)

U, I, B = np.meshgrid(u, i, b)
print('U=', U)
print('I=', I)
print('B=', B)

values = U ** u_pow * I ** i_pow * B ** b_pow
print('VALUES!', values)

fig = plt.figure()
# ax = Axes3D()
ax = fig.add_subplot(projection='3d')
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.zaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xlabel('Urgency')
ax.set_ylabel('Impact')
ax.set_zlabel('Blocks')

scatter = ax.scatter(U, I, B, cmap='spring_r')

u_slider_pos = fig.add_axes([0.05, 0.25, 0.0225, 0.63])
u_slider = Slider(
    # ax=plt.axes([0.2, 0.01, 0.65, 0.03]),
    ax=u_slider_pos,
    label='Urgency',
    valmin=-10,
    valmax=10,
    valstep=.05,
    orientation="vertical",
    valinit=u_pow
)

i_slider_pos = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
i_slider = Slider(
    # ax=plt.axes([0.2, 0.01, 0.65, 0.03]),
    ax=i_slider_pos,
    label='Impact',
    valmin=-10,
    valmax=10,
    valstep=.05,
    orientation="vertical",
    valinit=i_pow
)

b_slider_pos = fig.add_axes([0.15, 0.25, 0.0225, 0.63])
b_slider = Slider(
    ax=b_slider_pos,
    label='Blocks',
    valmin=-10,
    valmax=10,
    valstep=.05,
    orientation="vertical",
    valinit=b_pow
)


def redraw(val):
    print("REDRAW")
    # plt.clf()

    new_values = (U ** u_slider.val * I ** i_slider.val * B ** b_slider.val).reshape(1, -1)[0]
    print("NEW VALUES: ", new_values)
    norm = new_values / max(new_values)
    # print("max: ", max(new_values))
    # print("norm: ", norm)
    scatter.set_sizes(norm * 3000)

    print('F_NORM', norm)
    res = list(map(lambda v: (v, 1 - v, 0, 0.3 + v * 0.7), norm ** (1 / 3)))
    print('res', res)

    scatter.set_color(res)

    plt.draw()


u_slider.on_changed(redraw)
i_slider.on_changed(redraw)
b_slider.on_changed(redraw)

redraw(0)

plt.show()
