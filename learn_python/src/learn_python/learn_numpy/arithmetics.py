import numpy as np
from numpy.typing import NDArray


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


def el_wise_ops() -> None:
    array1: NDArray[np.integer] = np.array([1, 2, 3])
    array2: NDArray[np.integer] = np.array([4, 5, 6])

    print("Element wise operations on arrays")
    print(f"Array 1: {array1}")
    print(f"Array 1: {array2}")

    print()

    print(f"array1 + array2: {array1 + array2}")
    print(f"array1 - array2: {array1 - array2}")
    print(f"array1 * array2: {array1 * array2}")
    print(f"array1 / array2: {array1 / array2}")
    print(f"array1 ** array2: {array1**array2}")


if __name__ == "__main__":
    print("1. Scalar arithmetic.")
    print("2. Vectorized math funcs.")
    print("3. Element wise math.")

    choice = int(input("Choice of action: "))

    if choice == 1:
        scalar_arithmetic()
    elif choice == 2:
        vectorized_math_funcs()
    elif choice == 3:
        el_wise_ops()
