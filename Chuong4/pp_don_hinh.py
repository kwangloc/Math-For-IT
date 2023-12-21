from __future__ import division
from numpy import *
from fractions import Fraction

def main():
    t = pp_don_hinh([-2, -3, -2])
    t.add_constraint([2, 1, 1], 4)
    t.add_constraint([1, 2, 1], 7)
    t.add_constraint([0, 0, 1], 5)
    t.is_fraction = True
    t.solve()

class pp_don_hinh:
    def __init__(self, obj):
        self.obj = [1] + obj
        self.rows = []
        self.cons = []
        self.no_variables = len(obj)
        self.no_constraints = 0
        self.is_fraction = False
        self.basic_variables = []

    def add_constraint(self, expression, value):
        self.rows.append([0] + expression)
        self.cons.append(value)
        self.no_constraints += 1
        self.basic_variables.append("s" + str(self.no_constraints))

    def _pivot_column(self):
        return argmin(self.obj[1:-1]) + 1

    def _pivot_row(self, col):
        return argmin([self.rows[i][-1] / self.rows[i][col] if self.rows[i][col] != 0 else float('inf') for i in range(len(self.rows))])

    def display(self):
        fmt = '{:<8}'.format("Basic") \
              + "".join(['{:>8}'.format(f"x{i+1}") for i in range(self.no_variables)])   \
              + "".join(['{:>8}'.format(f"s{i+1}") for i in range(self.no_constraints)]) \
              + '{:>8}'.format("Sol.")

        fmt += "\n"
        fmt += '{:<8}'.format("z") \
               + "".join(["{:>8}".format(str(Fraction(item).limit_denominator(3))) for item in self.obj[1:]])

        for i, row in enumerate(self.rows):
            fmt += "\n"
            fmt += '{:<8}'.format(self.basic_variables[i]) \
                   + "".join(["{:>8}".format(str(Fraction(item).limit_denominator(3))) for item in row[1:]])
        print(fmt)

    def _pivot(self, row, col):
        self.rows[row] /= self.rows[row][col]
        for r in range(len(self.rows)):
            if r == row:
                continue
            self.rows[r] = self.rows[r] - self.rows[r][col] * self.rows[row]
        self.obj = self.obj - self.obj[col] * self.rows[row]

    def _check(self):
        return min(self.obj[1:-1]) >= 0

    def solve(self):
        for i in range(len(self.rows)):
            self.obj += [0]
            ident = [0] * len(self.rows)
            ident[i] = 1
            self.rows[i] += ident + [self.cons[i]]
            self.rows[i] = array(self.rows[i], dtype=float)
        self.obj = array(self.obj + [0], dtype=float)

        self.display()
        while not self._check():
            c, r = self._pivot_column(), self._pivot_row(self._pivot_column())
            self._pivot(r, c)
            print('\nEntering Variable:', f"{self.basic_variables[r]}  |  Leaving Variable: {self.basic_variables[c-1]}\n")
            self.basic_variables[r] = self.basic_variables[c-1]
            self.display()

if __name__ == '__main__':
    main()
