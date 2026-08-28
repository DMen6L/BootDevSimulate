import pandas as pd

if __name__ == "__main__":
    # DataFrame beginner friendly initiation
    data: dict[str, list[object]] = {
        "Name": ["user_1", "user_2", "user_3"],
        "Age": [18, 21, 29],
    }

    df: pd.DataFrame = pd.DataFrame(data, index=["A", "B", "C"])

    print(df)

    print()

    # Locating by indexing
    print(df.loc["A"])

    print()

    # Locating by integer indexes
    print(df.iloc[1])

    print()

    # Adding new column
    df["Job"] = ["Cook", "N/A", "Cashier"]

    print(df)

    print()

    # Add new row
    new_rows: pd.DataFrame = pd.DataFrame(
        [
            {"Name": "new_user1", "Age": 28, "Job": "Eng"},
            {"Name": "new_user2", "Age": 18, "Job": "New Hire"},
        ],
        index=["D", "E"],
    )

    df = pd.concat([df, new_rows])

    print(df)
