import random
import math


class Simulated_Annealing:
    def __init__(self, num_of_variables, num_of_clauses, clauses):
        self.num_of_variables = num_of_variables
        self.num_of_clauses = num_of_clauses
        self.clauses = clauses
        self.variables = {var: bool(random.getrandbits(1))
                          for var in range(1, num_of_variables+1)}
        self.best = (0, {})

    def process(self, level=-1, time_init=10, time_step=0.99, chance=100000):
        cp_level, cp_chance = level, chance
        current_obj_val = self.get_objective_values(self.variables)
        while level and chance:
            neighbor = self.get_random_neighbor()
            neighbor_obj_val = self.get_objective_values(neighbor)
            if neighbor_obj_val > current_obj_val:
                self.variables = neighbor
                current_obj_val = neighbor_obj_val
                if current_obj_val > self.best[0]:
                    self.best = (current_obj_val, self.variables)
                    chance = cp_chance
                    if self.best[0] == self.num_of_clauses:
                        break
            elif random.random() < math.exp((neighbor_obj_val-current_obj_val)/time_init):
                self.variables = neighbor
                current_obj_val = neighbor_obj_val
            chance -= 1
            level -= 1
            time_init *= time_step
        return cp_level if cp_level > 0 else -level

    def get_objective_values(self, variables):
        satisfied_clauses = 0
        for clause in self.clauses:
            for var in clause:
                if (var > 0 and variables[var]) or (var < 0 and not variables[-var]):
                    satisfied_clauses += 1
                    break
        return satisfied_clauses

    def get_random_neighbor(self):
        neighbor = self.variables.copy()
        randnum = random.randint(1, self.num_of_variables)
        neighbor[randnum] = not neighbor[randnum]
        return neighbor

    def result(self):
        obj_val = self.best[0]
        result = ''
        for i in range(1, self.num_of_variables+1):
            result += '1' if self.variables[i] else '0'
        return obj_val, result


num_of_variables, num_of_clauses = map(int, input().split())
clauses = [list(map(int, input().split()))[:-1] for _ in range(num_of_clauses)]
sa = Simulated_Annealing(num_of_variables, num_of_clauses, clauses)
level = sa.process()
obj_val, res = sa.result()
print(f'After {level} level\nObject values is {obj_val}\n{res}')
