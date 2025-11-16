import json
import os

def compute_kernel(ranking_a_json, ranking_b_json):
    def build_matrix(ranking):
        elements = [x for cl in ranking for x in (cl if isinstance(cl, list) else [cl])]
        idx = {x:i for i,x in enumerate(elements)}
        n = len(elements)
        M = [[0]*n for _ in range(n)]
        for cluster in ranking:
            cluster_list = cluster if isinstance(cluster, list) else [cluster]
            for x in cluster_list:
                i = idx[x]
                for prev in ranking:
                    prev_list = prev if isinstance(prev, list) else [prev]
                    if prev_list == cluster_list: break
                    for y in prev_list: M[i][idx[y]] = 1
                for y in cluster_list: M[i][idx[y]] = 1
        return M, elements

    A = json.loads(ranking_a_json)
    B = json.loads(ranking_b_json)

    YA, elems = build_matrix(A)
    YB, _ = build_matrix(B)

    def transpose(M): return [list(row) for row in zip(*M)]
    def and_matrix(M1,M2): return [[M1[i][j]&M2[i][j] for j in range(len(M1))] for i in range(len(M1))]
    def or_matrix(M1,M2): return [[M1[i][j]|M2[i][j] for j in range(len(M1))] for i in range(len(M1))]

    combined = or_matrix(and_matrix(YA,YB), and_matrix(transpose(YA),transpose(YB)))

    return [[elems[i], elems[j]] for i in range(len(elems)) for j in range(i+1, len(elems)) if combined[i][j]==0]

def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(folder, "Ранжировка A.json"), "r", encoding="utf-8") as f:
        ranking_a_json = f.read()
    with open(os.path.join(folder, "Ранжировка B.json"), "r", encoding="utf-8") as f:
        ranking_b_json = f.read()

    kernel = compute_kernel(ranking_a_json, ranking_b_json)

    with open(os.path.join(folder, "Ядро противоречий AB.json"), "w", encoding="utf-8") as f:
        json.dump(kernel, f, ensure_ascii=False, indent=2)

    print("Ядро противоречий сохранено!")

if __name__ == "__main__":
    main()
