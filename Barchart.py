import matplotlib.pyplot as plt
import numpy as np
categories=["fruits", "vegetables", "protein", "diary"]
values=[4, 3, 2, 1]
# plt.bar(categories, values, color="green")
plt.barh(categories, values, color="green")
plt.title("Diary consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")
plt.show()