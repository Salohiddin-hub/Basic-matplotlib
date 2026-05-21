import matplotlib.pyplot as plt
import numpy as np
x1=np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y1=np.array([50, 58, 60, 61, 63, 64, 65, 71, 82, 83])
x2=np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y2=np.array([55, 59, 64, 67, 69, 70, 65, 74, 86, 90])
plt.scatter(x1, y1, color="blue",
                    alpha=0.5,
                    s=200,
                    label="Class A")
plt.scatter(x2, y2, color="Green",
                    alpha=0.5,
                    s=200,
                    label="Class B")
plt.title("Test scores")
plt.xlabel("Hours studied")
plt.ylabel("Grades")
plt.legend()
plt.show()
