import pandas as pd

if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv("./data/pokemon.csv")

    # Getting by condition on height
    tall_pokemon = df[df["Height"] >= 2]

    print(tall_pokemon)

    print()

    happy_pokemon = df[df["Weight"] > 100]

    print(happy_pokemon)

    print()

    legendary_pokemon = df[df["Legendary"] == 1]

    print(legendary_pokemon)

    print()

    water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]

    print(water_pokemon)
