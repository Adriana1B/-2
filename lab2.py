# Визначення булевих змінних
p = [True, True, False, False]
q = [True, False, True, False]
r = [True, False, False, True]

# Функція для обчислення fn = p^(q або r)
def fn(p, q, r):
    result = []
    for i in range(len(p)):
        result.append(p[i] and (q[i] or r[i]))
    return result

# Виведення заголовка таблиці
print(" p | q | r | fn ")
print("----------------")
# Виведення значень змінних та результату
for i in range(len(p)):
    print(f" {p[i]} | {q[i]} | {r[i]} | {fn(p, q, r)[i]} ")
