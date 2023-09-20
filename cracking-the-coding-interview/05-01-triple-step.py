# Triple Step: A child is running up a staircase with n steps and can hop either
# 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many
# possible ways the child can run up the stairs.

# 💡
# Recordar: para los problemas de DP hay dos maneras, la recursiva con memoization
# que es top-down, y es la que más naturalmente me sale, comenzando desde el caso
# n y construyendo hacia abajo, n-1, n-2, ... hasta dar con los casos base,
# y la bottom-up, armando un array de soluciones desde el caso base 0, 1, 2, ...
# hasta el último, que sería la respuesta. Acá tener cuidado con los índices.
#
# En este problema, los casos base son tantos como número de saltos diferentes
# haya. Resulto eso el número de maneras de subir es la suma de dar un salto de
# cada tipo más el número de maneras de subir en el escalón en el que caigas.


# from functools import cache


# @cache  # <- This would remove the need of passing memo around
def triple_step(n_remaining_steps: int, memo: dict) -> int:
    if n_remaining_steps in memo:
        return memo[n_remaining_steps]
    if n_remaining_steps <= 0:
        return 0
    if n_remaining_steps == 1:
        return 1
    if n_remaining_steps == 2:
        return 2  # 1 + 1 | 2
    if n_remaining_steps == 3:
        return 4  # 1 + 1 + 1 | 1 + 2 | 2 + 1 | 3

    result = (
        triple_step(n_remaining_steps - 1, memo) +
        triple_step(n_remaining_steps - 2, memo) +
        triple_step(n_remaining_steps - 3, memo)
    )
    memo[n_remaining_steps] = result
    return result


def triple_step_2(n: int) -> int:
    result = [0] * n
    for i in range(n):
        if i == 0:
            value = 1
        elif i == 1:
            value = 2
        elif i == 2:
            value = 4
        else:
            value = result[i - 1] + result[i - 2] + result[i - 3]

        result[i] = value

    return result[n - 1]


for in_ in range(1, 50):
    result1 = triple_step(in_, memo={})
    result2 = triple_step_2(in_)
    print(f"{in_ = }, {result1}, {result2}")
