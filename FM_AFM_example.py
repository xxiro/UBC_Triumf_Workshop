from dwave.system import EmbeddingComposite, DWaveSampler


'''
******** Ferromagnetic chain ********
'''

# Modifiable parameters
num_qubits = 10                     # Number of qubits in our chain
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

print("Ferromagetic QPU response")
print(response)

'''
******** Anti-ferromagnetic chain ********
'''

# Modifiable parameters
num_qubits = 10
afm_qubit_bias = [0] * num_qubits
afm_coupler_strength = 1

# Ising model parameters
h = afm_qubit_bias
J = {}

for i in range(num_qubits-1):
    J[(i, i+1)] = afm_coupler_strength

# Submit the problem to the QPU
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample_ising(h, J, num_reads=10)

print("Anti-ferromagetic QPU response")
print(response)