import numpy as np
from numpy.random import Generator


if __name__ == "__main__":
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
