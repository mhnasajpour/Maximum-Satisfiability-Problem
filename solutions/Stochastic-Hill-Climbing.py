import random


class Stochastic_Hill_Climbing:
    def __init__(self, num_of_variables, num_of_clauses, clauses):
        self.num_of_variables = num_of_variables
        self.num_of_clauses = num_of_clauses
        self.clauses = clauses
        self.variables = {var: bool(random.getrandbits(1))
                          for var in range(1, num_of_variables+1)}
        self.best = (0, {})

    def process(self, level=-1):
        cp_level = level
        while level:
            neighbors, objective_values = self.get_neighbors(self.variables)
            for i in range(self.num_of_variables):
                if objective_values[i] > self.best[0]:
                    self.best = (objective_values[i], neighbors[i])
            if self.best[0] == self.num_of_clauses:
                break
            self.variables = self.select_individual(
                neighbors, objective_values)
            level -= 1
        return cp_level if cp_level > 0 else -level

    def get_objective_values(self, variables):
        satisfied_clauses = 0
        for clause in self.clauses:
            for var in clause:
                if (var > 0 and variables[var]) or (var < 0 and not variables[-var]):
                    satisfied_clauses += 1
                    break
        return satisfied_clauses

    def select_individual(self, neighbors, objective_values):
        randnum = random.randint(0, sum(objective_values))
        temp = 0
        for index, obj_val in enumerate(objective_values):
            temp += obj_val
            if randnum <= temp:
                return neighbors[index]

    def get_neighbors(self, variables):
        neighbors = [variables.copy() for _ in range(self.num_of_variables)]
        objective_values = []
        for i in range(self.num_of_variables):
            neighbors[i][i+1] = not neighbors[i][i+1]
            objective_values.append(self.get_objective_values(neighbors[i]))
        return neighbors, objective_values

    def result(self):
        obj_val = self.best[0]
        result = ''
        for i in range(1, self.num_of_variables+1):
            result += '1' if self.variables[i] else '0'
        return obj_val, result


num_of_variables, num_of_clauses = map(int, input().split())
clauses = [list(map(int, input().split()))[:-1] for _ in range(num_of_clauses)]
shc = Stochastic_Hill_Climbing(num_of_variables, num_of_clauses, clauses)
level = shc.process()
obj_val, res = shc.result()
print(f'After {level} level\nObject values is {obj_val}\n{res}')
