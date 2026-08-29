import numpy as np

if __name__ == "__main__":
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
