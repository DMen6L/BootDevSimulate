import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([5, 10, 15, 20, 25])

    plt.grid(
        axis="y",
        linewidth=2,
        color="pink",
        linestyle="dashed",
    )

    plt.plot(x, y)
    plt.show()
