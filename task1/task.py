import csv
from typing import List, Tuple

def main(filename: str) -> Tuple[List[List[int]], List[List[int]], List[List[int]], List[List[int]], List[List[int]]]:
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    if rows[0][0].lower() == "root":
        root = int(rows[0][1])
        rows = rows[1:]

    header = rows[0]
    parent_idx = header.index("parent")
    child_idx = header.index("child")

    edges = [(int(row[parent_idx]), int(row[child_idx])) for row in rows[1:]]

    vertices = sorted(set([u for u, v in edges] + [v for u, v in edges]))
    n = len(vertices)
    idx = {v: i for i, v in enumerate(vertices)}

    # Матрица смежности
    adj = [[0] * n for _ in range(n)]
    for u, v in edges:
        adj[idx[u]][idx[v]] = 1

    # r1 (непосредственное управление)
    r1 = [[0] * n for _ in range(n)]
    for u, v in edges:
        r1[idx[u]][idx[v]] = 1

    # r2 (непосредственное подчинение)
    r2 = [[r1[j][i] for j in range(n)] for i in range(n)]

    # r3 (опосредованное управление)
    r3 = [row[:] for row in r1]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if r3[i][k] and r3[k][j]:
                    r3[i][j] = 1

    # r4 (опосредованное подчинение)
    r4 = [[r3[j][i] for j in range(n)] for i in range(n)]

    # r5 (соподчинение)
    r5 = [[0] * n for _ in range(n)]
    for p, c in edges:
        siblings = [v for u, v in edges if u == p]
        for i in range(len(siblings)):
            for j in range(i + 1, len(siblings)):
                v1, v2 = siblings[i], siblings[j]
                r5[idx[v1]][idx[v2]] = 1
                r5[idx[v2]][idx[v1]] = 1

    return adj, r1, r2, r3, r4, r5


if __name__ == "__main__":
    adj, r1, r2, r3, r4, r5 = main("task1.csv")
    for name, M in zip(["adj", "r1", "r2", "r3", "r4", "r5"], [adj, r1, r2, r3, r4, r5]):
        print(f"{name}:")
        for row in M:
            print(row)
        print()
