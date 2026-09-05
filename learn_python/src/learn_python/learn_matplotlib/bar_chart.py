import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    categories = ["Grains", "Fruit", "Vegetables", "Protein", "Diary", "Sweets"]
    values = np.array([4, 3, 2, 5, 3, 1])

    plt.bar(categories, values, color="red")
    # plt.barh(categories, values, color="red")

    plt.title("Daily consuption")
    plt.xlabel("Food")
    plt.ylabel("Quantity")

    plt.show()
