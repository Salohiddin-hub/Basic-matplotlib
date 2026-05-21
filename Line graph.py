import matplotlib.pyplot as plt
import numpy as np
x=np.array([2023, 2024, 2025, 2026])
y=np.array([15, 25, 30, 20])
y2=np.array([12, 5, 7, 19])
y3=np.array([5, 7, 1, 40])
line_style=dict(marker="v",
               markersize=10,
               markerfacecolor="yellow",
               markeredgecolor="black",
               linestyle="solid",
               linewidth=10)
plt.grid(axis="y",
         linewidth=2,
         color="blue",
         linestyle="dashed")

plt.title("Class size", fontsize=20,
                        family="Arial",
                        fontweight="bold",
                        color="red")
plt.xlabel("Year", fontsize=20,
                   family="Arial",
                   fontweight="bold")
plt.ylabel("Students", fontsize=20,
                       family="Arial",
                       fontweight="bold")
plt.plot(x, y,  color="black", **line_style)
plt.plot(x, y2, color="green", **line_style)
plt.plot(x, y3, color="yellow", **line_style)
plt.show()