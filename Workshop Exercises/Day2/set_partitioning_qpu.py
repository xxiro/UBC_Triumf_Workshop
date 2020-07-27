'''
Problem: Partition the set [-5, 9, 4] such that the sum of the subsets are equal

'''

# 1. Import packages
from dwave.system import DWaveSampler, EmbeddingComposite

# 2. Define the problem
Q = {('x0', 'x0'): 260, ('x1', 'x1'): 36, ('x2', 'x2'): -64,
     ('x0', 'x1'): -360, ('x1', 'x2'): 288, ('x0', 'x2'): -160}

# 3. Instantiate a solver
solver = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))

# 4. Solve the problem
sampleset = solver.sample_qubo(Q, chain_strength=200,  num_reads=100)

# 5. Interpret results
print(sampleset)