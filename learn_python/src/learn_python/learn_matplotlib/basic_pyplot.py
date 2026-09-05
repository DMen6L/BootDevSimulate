import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # Using numpy arrays is faster
    x = np.array([13, 14, 15, 16])
    y = np.array([156, 161, 170, 178])

    # Passing single value puts the values on y axis
    # The x axis values in case of single passed value will start from 0.0
    plt.plot(x, y)

    plt.show()
