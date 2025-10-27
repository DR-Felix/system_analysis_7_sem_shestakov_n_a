import csv
from typing import List

def main(file: str) -> List[List[int]]:
    edges = []
    with open(file, newline="") as f:
        reader = csv.reader(f)
        for u, v in reader:
            edges.append((int(u), int(v)))

    n = max(max(u, v) for u, v in edges)
    matrix = [[0] * n for _ in range(n)]

    for u, v in edges:
        matrix[u - 1][v - 1] = 1
        matrix[v - 1][u - 1] = 1  # неориентированный граф

    return matrix


if __name__ == "__main__":
    mat = main("task0.csv")
    for row in mat:
        print(row)
