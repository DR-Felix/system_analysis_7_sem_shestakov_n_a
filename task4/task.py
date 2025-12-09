# task4/task.py
import json

def linear_interp(x0, y0, x1, y1, x):
    """Линейная интерполяция между точками (x0,y0) и (x1,y1)."""
    if x1 == x0:
        return y0
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

def membership(value, points):
    """Вычисляет степень принадлежности value функции, заданной точками."""
    for i in range(len(points)-1):
        x0, y0 = points[i]
        x1, y1 = points[i+1]
        if x0 <= value <= x1:
            return linear_interp(x0, y0, x1, y1, value)
    # если вне диапазона
    if value < points[0][0]:
        return points[0][1]
    if value > points[-1][0]:
        return points[-1][1]
    return 0

def fuzzify(temp_value, temp_terms):
    """Фаззификация температуры."""
    fuzzified = {}
    for term in temp_terms:
        fuzzified[term['id']] = membership(temp_value, term['points'])
    return fuzzified

def apply_rules(fuzz_temp, rules, output_terms):
    """Применение правил Мамдани и объединение нечетких множеств."""
    s_values = set()
    for term in output_terms:
        for x, _ in term['points']:
            s_values.add(x)
    s_values = sorted(s_values)

    mu_result = {s:0 for s in s_values}

    for rule in rules:
        input_term, output_term = rule
        activation = fuzz_temp.get(input_term, 0)
        # применяем минимакс (Мамдани)
        output_points = next(t['points'] for t in output_terms if t['id'] == output_term)
        for s, mu_s in output_points:
            mu_result[s] = max(mu_result[s], min(activation, mu_s))

    return mu_result

def defuzzify_first_max(mu_result):
    """Дефаззификация методом первого максимума."""
    max_mu = max(mu_result.values())
    for s in sorted(mu_result.keys()):
        if mu_result[s] == max_mu:
            return s
    return 0

def main(temp_json, output_json, rules_json, current_temp):
    temp_terms = json.loads(temp_json)['температура']
    output_terms = json.loads(output_json)['температура']
    rules = json.loads(rules_json)

    fuzz_temp = fuzzify(current_temp, temp_terms)
    mu_result = apply_rules(fuzz_temp, rules, output_terms)
    result = defuzzify_first_max(mu_result)
    return result

if __name__ == "__main__":
    current_temp = 21.0  # пример: текущая температура
    with open('example1.json', 'r', encoding='utf-8') as f:
        temp_json = f.read()
    with open('example2.json', 'r', encoding='utf-8') as f:
        output_json = f.read()
    with open('example3.json', 'r', encoding='utf-8') as f:
        rules_json = f.read()

    result = main(temp_json, output_json, rules_json, current_temp)
    print("Оптимальное значение управления:", result)
