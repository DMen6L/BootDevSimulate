import numpy as np

if __name__ == "__main__":
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
