import numpy as np
from numpy.typing import NDArray
import pytest


def clear_screen() -> None:
    print("\033[2J\033[H", end="")


def single_dimensional_array() -> None:
    # Basically represent the same array
    arr_norm: list[int] = [1, 2, 3]
    arr_np: NDArray[np.integer] = np.array(arr_norm)

    print("Arrays: ")
    print(arr_norm)
    print(arr_np)

    print()

    print("Multiply by 2: ")
    print(arr_norm * 2)  # list gets longer
    print(arr_np * 2)  # array gets multiplied by a number

    print()

    # Different objects
    print("Types of the arrays: ")
    print(type(arr_norm))
    print(type(arr_np))


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


def slicing() -> None:
    array = np.array(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
    )

    # array[start:end:step]

    print("First row")
    print(array[0])

    print()

    print("Last row")
    print(array[-1])

    print()

    print("First three rows")
    print(array[0:3])

    print()

    print("Every second from first")
    print(array[0:4:2])  # can also use array[::2]

    print()

    print("Reverse the array")
    print(array[::-1])

    print()

    print("First column")
    print(array[:, 0])


def scalar_arithmetic() -> None:
    array = np.array([1, 2, 3])

    print("basic operations +1 -2 *3 /4 **5")
    print(array + 1)
    print(array - 2)
    print(array * 3)
    print(array / 4)
    print(array**5)

    print()


# Functions applied to the entire array without loops
def vectorized_math_funcs() -> None:
    array = np.array([1.44, 2.5, 3.9])

    print("Sqrt")
    print(np.sqrt(array))

    print()

    print("Round")
    print(np.round(array))

    print()

    print("Ceiling")
    print(np.ceil(array))

    print()

    print("PI")
    print(np.pi)


if __name__ == "__main__":
    print("1. Single dimensional arrays.")
    print("2. multy dimensional arrays, wrong shape.")
    print("3. multy dimensional arrays and the tools for work with them.")
    print("4. slicings.")
    print("5. scalar arithmetic.")
    print("6. Vectorized math functions.")

    choice: int = int(input("Choose an option: "))

    clear_screen()

    if choice == 1:
        single_dimensional_array()
    if choice == 2:
        error_mult_dim_array()
    if choice == 3:
        mult_dim_array()
    if choice == 4:
        slicing()
    if choice == 5:
        scalar_arithmetic()
    if choice == 6:
        vectorized_math_funcs()
