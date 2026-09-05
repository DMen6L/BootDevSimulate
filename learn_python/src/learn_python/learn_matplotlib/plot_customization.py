from os import wait

from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    x = np.array([2024, 2025, 2026, 2027])
    y1 = np.array([15, 20, 30, 20])
    y2 = np.array([33, 27, 19, 25])

    # Saving line style as dictionary for reproducting the same style over multiple plots
    # marker can be = [. o v *] and more
    # markersize can be shortened as ms
    # markerfacecolor can be color name, RGB and HEX values
    # markerfacecolor can also be shortened as mfc
    # markeredgecolor can also be shortened as mec
    line_style = {
        "marker": ".",
        "markersize": 10,
        "markerfacecolor": "red",
        "markeredgecolor": "green",
        "linestyle": "solid",
        "linewidth": 2,
    }

    plt.title(
        "Class size",
        fontsize=20,
        family="Arial",
        fontweight="bold",
        color="blue",
    )

    plt.xlabel(
        "Year",
        fontsize=20,
        family="Arial",
        fontweight="bold",
        color="gray",
    )
    plt.ylabel(
        "Frogs",
        fontsize=20,
        family="Arial",
        fontweight="bold",
        color="gray",
    )

    # axis can be [x, y, both]
    plt.tick_params(axis="both", colors="gray")

    plt.plot(x, y1, color="black", **line_style)
    plt.plot(x, y2, color="green", **line_style)

    plt.xticks(x)

    plt.show()
