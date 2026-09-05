import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    categories = ["Freshmen", "Sophmores", "Juniors", "Seniors"]
    values = np.array([300, 250, 275, 225])
    colors = ["red", "green", "blue", "yellow"]

    plt.pie(
        values,
        labels=categories,
        autopct="%1.1f%%",
        colors=colors,
        explode=[0, 0, 0, 0.1],
        shadow=True,
        startangle=90,
    )

    plt.title("New College")

    plt.show()
