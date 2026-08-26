import numpy as np
from numpy.random import Generator
from numpy.typing import NDArray


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


def comparison_ops() -> None:
    scores = np.array([91, 55, 74, 96, 44, 100])

    print("Comparison operators on array")
    print(scores)

    print()

    print(f"= 100: {scores == 100}")
    print(f">= 60: {scores >= 60}")
    print(f"< 60: {scores < 60}")

    print()

    # Assign all elements < 60 to 0
    scores[scores < 60] = 0

    print(f"assigning 0 if < 60: {scores}")


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


def aggr_funcs() -> None:
    array = np.array(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
        ]
    )

    print(f"Array for aggregation: {array}")

    print()

    print(f"Sum: {np.sum(array)}")
    print(f"Mean: {np.mean(array)}")
    print(f"STD: {np.std(array)}")
    print(f"VAR: {np.var(array)}")
    print(f"MIN: {np.min(array)}")
    print(f"MAX: {np.max(array)}")
    print(f"MIN position: {np.argmin(array)}")
    print(f"MAX position: {np.argmax(array)}")

    print()

    print(f"Sum columns: {np.sum(array, axis=0)}")
    print(f"Sum rows: {np.sum(array, axis=1)}")


def filtering() -> None:
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


def randoms() -> None:
    rng: Generator = np.random.default_rng()

    print("Random values")
    print(f"1 < and < 7: {rng.integers(low=1, high=7)}")
    print(f"1 < and < 101, of size 3: {rng.integers(low=1, high=101, size=3)}")
    print(
        f"1 < and < 101, of size (3, 2): {rng.integers(low=1, high=101, size=(3, 2))}"
    )

    print()

    print(f"floating randoms: {np.random.uniform(low=-1, high=1, size=2)}")

    print()

    array = np.array([1, 2, 3, 4, 5])

    print(f"Array for shuffle: {array}")

    rng.shuffle(array)

    print(f"Array shuffled: {array}")
    print(f"Random choice from array(size=2): {rng.choice(array, size=2)}")


if __name__ == "__main__":
    print("1. Single dimensional arrays.")
    print("2. multy dimensional arrays, wrong shape.")
    print("3. multy dimensional arrays and the tools for work with them.")
    print("4. slicings.")
    print("5. scalar arithmetic.")
    print("6. Vectorized math functions.")
    print("7. Element wise operations.")
    print("8. Comparison operators.")
    print("9. Broadcase errors.")
    print("10. Broadcast examle.")
    print("11. Aggregation.")
    print("12. Filtering.")
    print("13. Randoms.")

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
    if choice == 7:
        el_wise_ops()
    if choice == 8:
        comparison_ops()
    if choice == 9:
        error_broadcasting()
    if choice == 10:
        broadcasting()
    if choice == 11:
        aggr_funcs()
    if choice == 12:
        filtering()
    if choice == 13:
        randoms()
