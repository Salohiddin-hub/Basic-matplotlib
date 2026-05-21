import matplotlib.pyplot as plt
import numpy as np
categories=["Freshmen", "Juniors", "Middle", "Senior"]
values=np.array([300, 250, 275, 225])
colors=["red", "blue", "yellow", "green"]
plt.pie(values, labels=categories,
        colors=colors,
        autopct="%1.1f%%",
        explode=[0.1, 0.1, 0.1, 0.1],
        shadow=True,
        startangle=0)
plt.title("Salohiddin's academy")
plt.show()