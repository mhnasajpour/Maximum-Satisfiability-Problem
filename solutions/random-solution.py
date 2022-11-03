import random


def get_objective_values(variables, clauses):
    satisfied_clauses = 0
    for clause in clauses:
        for var in clause:
            if (var > 0 and variables[var]) or (var < 0 and not variables[-var]):
                satisfied_clauses += 1
                break
    return satisfied_clauses


num_of_variables, num_of_clauses = map(int, input().split())
clauses = [list(map(int, input().split()))[:-1] for _ in range(num_of_clauses)]
variables = {var: bool(random.getrandbits(1))
             for var in range(1, num_of_variables+1)}

obj_val = get_objective_values(variables, clauses)

res = ''
for i in range(1, num_of_variables+1):
    res += '1' if variables[i] else '0'
print(f'After 1 level\nObject values is {obj_val}\n{res}')
