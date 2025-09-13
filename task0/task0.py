import csv

def load_csv(file: str):
    edges = []
    f = open(file, newline="")
    reader = csv.reader(f)
    for i in reader:
        u, v = map(int, i)
        edges.append((u, v))
    f.close()
    return edges

def build_matrix(edges):
    n = max(max(u, v) for u, v in edges)
    matrix = [[0] * (n + 1) for i in range(n + 1)]
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1  # подразумеваем, что граф неориентированный
    return matrix

def main():
    filename = "task0.csv"
    edges = load_csv(filename)
    matrix = build_matrix(edges)
    for i in matrix[1:]:
        print(i[1:])

if __name__ == "__main__":
    main()
