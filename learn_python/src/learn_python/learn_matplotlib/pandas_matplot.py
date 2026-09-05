import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv("./data/pokemon.csv")
    df = df.drop_duplicates()

    type_count = df["Type1"].value_counts(ascending=True)

    types: list[str] = type_count.index.astype(str).to_list()
    count = type_count.to_numpy(dtype=float)

    plt.barh(types, count, color="skyblue", edgecolor="black")

    plt.title("# of pokemon by Type1")
    plt.xlabel("Count")
    plt.ylabel("Type")

    plt.tight_layout()

    plt.show()
