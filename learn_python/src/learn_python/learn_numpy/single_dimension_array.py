import numpy as np
from numpy.typing import NDArray

if __name__ == "__main__":
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
