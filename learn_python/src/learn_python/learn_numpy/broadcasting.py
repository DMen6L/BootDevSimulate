import numpy as np


def error_broadcasting() -> None:
    # impossible to broadcast since shapes do not match and the corresponding row or column isn't 1 dimensional
    array1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    array2 = np.array([[1], [2], [3], [4]])

    print("Arrays:")
    print(f"Array 1: {array1}")
    print(f"Array 2: {array2}")

    print()

    try:
        print(array1 * array2)
    except ValueError as error:
        print(f"Broadcast failed bacause: {error}")


def broadcasting() -> None:
    array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
    array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

    print("Broadcasing arrays:")
    print(f"Array 1: {array1}")
    print(f"Array 2: {array2}")

    print()

    print("Shapes:")
    print(f"Array 1: {array1.shape}")
    print(f"Array 2:{array2.shape}")

    print()

    print(f"Broadcast result: {array1 * array2}")


if __name__ == "__main__":
    print("1. Errors when broadcasting.")
    print("2. Broadcasing example.")

    choice = int(input("Choice of action: "))

    if choice == 1:
        error_broadcasting()
    elif choice == 2:
        broadcasting()
