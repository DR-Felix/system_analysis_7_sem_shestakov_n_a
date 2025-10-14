import csv
import math


def entropy_of_matrix(M):
    flat = [x for row in M for x in row]
    total = len(flat)
    if total == 0:
        return 0.0, 0.0

    ones = sum(flat)
    zeros = total - ones

    probs = []
    if ones > 0:
        probs.append(ones / total)
    if zeros > 0:
        probs.append(zeros / total)

    # Энтропия Шеннона
    H = -sum(p * math.log2(p) for p in probs)
    Hmax = math.log2(len(probs)) if len(probs) > 1 else 1
    h = H / Hmax if Hmax != 0 else 0.0

    return H, h


def complexity_entropy(matrices):
    H_values, h_values = [], []

    for M in matrices:
        H, h = entropy_of_matrix(M)
        H_values.append(H)
        h_values.append(h)

    H_total = sum(H_values) / len(H_values)
    h_total = sum(h_values) / len(h_values)

    return H_total, h_total


def main():
    adj = [
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    r1 = [
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    r2 = [
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
    ]

    r3 = [
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    r4 = [
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0],
    ]

    r5 = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    matrixes = (adj, r1, r2, r3, r4, r5)

    H, h = complexity_entropy(matrixes)

    print(f"Энтропия сложности H = {H:.4f}")
    print(f"Нормированная энтропия h = {h:.4f}")


if __name__ == "__main__":
    main()
