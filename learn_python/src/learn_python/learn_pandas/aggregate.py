import pandas as pd

if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv("./data/pokemon.csv")

    # Whole dataframe
    print(df.mean(numeric_only=True))
    print()
    print(df.sum(numeric_only=True))
    print()
    print(df.min(numeric_only=True))
    print()
    print(df.max(numeric_only=True))
    print()
    print(df.count())

    print()

    # For single columns
    print(df["Height"].mean())
    print()
    print(df["Height"].sum())
    print()
    print(df["Height"].min())
    print()
    print(df["Height"].max())
    print()
    print(df["Height"].count())

    print()

    # Grouping
    group = df.groupby("Type1")

    print(group["Height"].mean())
    print()
    print(group["Height"].sum())
    print()
    print(group["Height"].min())
    print()
    print(group["Height"].max())
    print()
    print(group["Height"].count())
    print()
