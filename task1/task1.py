import csv


def read_csv(filename):
    edges = []
    root = None
    with open(filename, newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if rows[0][0].lower() == "root":
            root = int(rows[0][1])
            rows = rows[1:]  # убираем строку с корнем

        header = rows[0]
        parent_idx = header.index("parent")
        child_idx = header.index("child")

        for row in rows[1:]:
            edges.append((int(row[parent_idx]), int(row[child_idx])))

    return edges, root


def matrix(edges, root):
    vertices = sorted(set([u for u, v in edges] + [v for u, v in edges]))
    n = len(vertices)
    idx = {v: i for i, v in enumerate(vertices)}

    # Матрица смежности
    adj = [[0] * n for _ in range(n)]
    for u, v in edges:
        adj[idx[u]][idx[v]] = 1

    # r1 (управления)
    r1 = [[0] * n for _ in range(n)]
    for u, v in edges:
        r1[idx[u]][idx[v]] = 1

    # r2 (подчинения)
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

    # r5 (соподчинения)
    r5 = [[0] * n for _ in range(n)]
    for p, c in edges:
        siblings = [v for u, v in edges if u == p]
        for i in range(len(siblings)):
            for j in range(i + 1, len(siblings)):
                v1, v2 = siblings[i], siblings[j]
                r5[idx[v1]][idx[v2]] = 1
                r5[idx[v2]][idx[v1]] = 1

    return adj, r1, r2, r3, r4, r5, vertices, root


def print_matrix(name, M, vertices):
    print(f"\n{name}:")
    header = "   " + " ".join(f"{v:>2}" for v in vertices)
    print(header)
    for v, row in zip(vertices, M):
        print(f"{v:>2} " + " ".join(f"{x:>2}" for x in row))


def main():
    edges, root = read_csv("task1.csv")

    adj, r1, r2, r3, r4, r5, vertices, root = matrix(edges, root)

    print(f"\nКорень дерева: {root}")
    print_matrix("Матрица смежности", adj, vertices)
    print_matrix("r1 (управления)", r1, vertices)
    print_matrix("r2 (подчинения)", r2, vertices)
    print_matrix("r3 (опосредованного управления)", r3, vertices)
    print_matrix("r4 (опосредованного подчинения)", r4, vertices)
    print_matrix("r5 (соподчинения)", r5, vertices)

if __name__ == "__main__":
    main()
