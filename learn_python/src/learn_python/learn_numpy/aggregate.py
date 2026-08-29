import numpy as np

if __name__ == "__main__":
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
