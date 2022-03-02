import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.style.use('dark_background')
fig, axs = plt.subplots(2, 5, constrained_layout=True, figsize=(7, 3.2))

hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']


def hatches_plot(ax, h):
    ax.add_patch(Rectangle((0, 0), 2, 2, fill=False, hatch=h))
    ax.text(1, -0.5, f"' {h} '", size=15, ha="center")
    ax.axis('equal')
    ax.axis('off')

for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)



fig.show()