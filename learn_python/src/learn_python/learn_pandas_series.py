import pandas as pd

if __name__ == "__main__":
    data: list[int] = [100, 102, 104, 200, 202]

    # 1. Indexing can be changed
    series: pd.Series = pd.Series(data, index=["a", "b", "c", "d", "e"])

    print(f"Series: \n {series}")

    print()

    # Not existing labels give KeyError
    print(f"Getting element by lable: {series.loc['a']}")

    print()

    # series.loc also allow to update the values
    series.loc["c"] = 200

    print(series)

    print()

    # series.iloc is for locating elements by integer values
    print(f"Value at iloc 0: {series.iloc[0]}")

    print()

    print(f"Return values in the series >= 200: \n{series[series >= 200]}")

    calories: dict[str, int] = {
        "Day 1": 1750,
        "Day 2": 2100,
        "Day 3": 1700,
    }

    series_dict = pd.Series(calories)

    print(f"Series from dictionary: {series_dict}")
