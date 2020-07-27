'''
Problem: Partition the set [-5, 9, 4] such that the sum of the subsets are equal

We will use the ExactSolver to evaluate all possible solutions to this problem
'''

# 1. Import packages
from dimod import ExactSolver

# 2. Define the problem
Q = {('x0', 'x0'): 260, ('x1', 'x1'): 36, ('x2', 'x2'): -64,
     ('x0', 'x1'): -360, ('x1', 'x2'): 288, ('x0', 'x2'): -160}

# 3. Instantiate a solver
solver = ExactSolver()

# 4. Solve the problem
sampleset = solver.sample_qubo(Q)

# 5. Interpret results
print(sampleset)