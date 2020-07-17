from dwave.system import EmbeddingComposite, DWaveSampler
import dwave.inspector as inspector


'''
******** Ferromagnetic chain ********

1. Try to make an anti-ferromagnetic chain
2. What happens when you add linear biases on either end of a ferromagnetic chain?
3. What happens when you modify the J's so they aren't all the same value?
'''

# Modifiable parameters
num_qubits = 10                        # Number of qubits in our chain
fm_qubit_bias = [0] * num_qubits       # List of biases to apply to each qubit in our chain
fm_coupler_strength = -1               # The coupling we want to apply to two adjacent qubits

# Ising model parameters
h = fm_qubit_bias
J = {}

for i in range(num_qubits-1):
    J[(i, i+1)] = fm_coupler_strength

# Submit the problem to the QPU
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample_ising(h, J, num_reads=10)

inspector.show(response)

print("Ferromagetic QPU response")
print(response)