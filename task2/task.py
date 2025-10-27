import math
from typing import List, Tuple
from task1.task import main as task1_main  # импортируем ЛР1

def calc_entropy(matrix: List[List[bool]]) -> float:
    n = len(matrix)
    ent = 0.0
    for i in range(n):
        out_deg = sum(matrix[i])
        if out_deg > 0:
            p = out_deg / (n - 1)
            ent -= p * math.log2(p)
    return ent

def main(filename: str) -> Tuple[float, float]:
    adj, r1, r2, r3, r4, r5 = task1_main("../task1/" + filename)

    matrices = [r1, r2, r3, r4, r5]
    n = len(r1)
    H_total = sum(calc_entropy(M) for M in matrices)
    c = 1 / (math.e * math.log(2))
    H_ref = c * n * len(matrices)
    h_total = H_total / H_ref

    return round(H_total, 1), round(h_total, 2)


if __name__ == "__main__":
    H, h = main("../task2/task2.csv")
    print(f"H = {H}, h = {h}")
