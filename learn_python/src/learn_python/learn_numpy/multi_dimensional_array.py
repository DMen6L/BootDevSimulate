import numpy as np


def error_mult_dim_array() -> None:
    arr = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3], [4, 5, 6], [7, 8]],
    ]

    print("Trying numpy array from: ")
    print(arr)
    print()

    try:
        arr_np = np.array(arr)
        print(arr_np)

    except ValueError as error:
        print("Numpy returned an error: ")
        print(error)


def mult_dim_array() -> None:
    arr = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    ]

    print("Numpy array from: ")
    print(arr)
    print()

    arr_np = np.array(arr)

    print("Numpy array:")
    print(arr_np)

    print()

    print(f"Number of dimensions {arr_np.ndim}")
    print(f"Shape of the array {arr_np.shape}")

    # Get element at position 0, 0, 0
    # use [0, 0, 0] instead of [0][0][0]
    print(f"Getting elements fast at (0, 0, 0) -> {arr_np[0, 0, 0]}")


if __name__ == "__main__":
    print("1. Error with multi dimensional arrays.")
    print("2. Multi dimensional arrays example.")

    choice = int(input("Choice of action: "))

    if choice == 1:
        error_mult_dim_array()
    elif choice == 2:
        mult_dim_array()
