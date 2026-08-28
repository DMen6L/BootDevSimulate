import pandas as pd

if __name__ == "__main__":
    # if a column is set as index_col it can't be used as normal column
    df: pd.DataFrame = pd.read_csv("./data/pokemon.csv", index_col="Name")

    # For large files it will be shortened
    # To print full large file use df.to_string()
    print(df)

    print()

    # Selection by column
    print(df["No"])

    print()

    # Select multiple columns
    print(df[["Weight", "Height"]])

    print()

    # Selection by row
    # Using loc with specified columns to choose
    print(df.loc["Charizard", ["Height", "Weight"]])

    print()

    # Select rows
    print(df.loc["Pikachu":"Snorlax", ["Height", "Weight"]])

    # Doing the same with iloc
    print(df.iloc[0:11:2, 0:3])
