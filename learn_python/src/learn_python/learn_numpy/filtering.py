import numpy as np

if __name__ == "__main__":
    ages = np.array(
        [
            [21, 17, 19, 20, 16, 30],
            [39, 22, 13, 20, 21, 99],
        ]
    )

    teens = ages[ages < 18]
    adults = ages[(ages >= 18) & (ages < 65)]
    evens = ages[ages % 2 == 0]

    print(f"Array of work: {ages}")
    print(f"< 18: {teens}")
    print(f">= 18 and < 65: {adults}")
    print(f"Evens: {evens}")

    print()

    preserve_adults = np.where(ages >= 18, ages, 0)

    print(f"Preserving shape(>= 18 and < 65): {preserve_adults}")
