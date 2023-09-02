from dotenv import load_dotenv
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

load_dotenv()


qubits = 2
classical_bits = 2

quantum_circuit = QuantumCircuit(qubits, classical_bits)

# add hadamard gate to qubit 0
quantum_circuit.h(0)

# Perform a controlled-x gate on qubit 1 controlled by qubit 0
quantum_circuit.cx(0, 1)

# measure qubit 0 to classical bit 0
# and qubit 1 to classical bit 1
quantum_circuit.measure(0, 0)
quantum_circuit.measure(1, 1)

# draw the circuit
quantum_circuit.draw("mpl")

service = QiskitRuntimeService()
backend = service.least_busy(simulator=True, operational=True)

sampler = Sampler(backend)

# submit circuit to the sampler
print('submitting circuit...')
job = sampler.run(quantum_circuit)

# Wait for the job to complete, then get the result
print('waiting for results...')
result = job.result()
quasi_dists = result.quasi_dists
print(f"result: {result}")

plot_histogram(quasi_dists)
plt.savefig('./hello-world/plots/simple-circuit.png')