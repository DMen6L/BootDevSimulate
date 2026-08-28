import pandas as pd

if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv("./data/pokemon.csv")

    # Drop irrelevant columns
    # df = df.drop(columns=["Legendary"])

    # Drop if missing a value
    # df = df.dropna(subset=["Type2"])
    # df = df.fillna({"Type2": "None"})

    # Fix inconsistent values
    # df["Type1"] = df["Type1"].replace(
    #     {
    #         "Grass": "GRASS",
    #         "Fire": "FIRE",
    #         "Water": "WATER",
    #     }
    # )

    # Standardize text
    # df["Name"] = df["Name"].str.lower()

    # Fix data types
    # df["Legendary"] = df["Legendary"].astype(bool)

    # Remove duplicate values
    df = df.drop_duplicates()

    print(df)
