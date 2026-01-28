
import numpy as np
from qiskit.circuit.library import ZZFeatureMap
from qiskit.quantum_info import Statevector

class QuantumWeatherModel:
    def __init__(self):
        self.feature_map = ZZFeatureMap(feature_dimension=2, reps=2)

    def encode(self, x):
        """Encode classical data into quantum state"""
        circuit = self.feature_map.assign_parameters(x.flatten())
        state = Statevector.from_instruction(circuit)
        return state

    def compute_similarity(self, x1, x2):
        """Quantum kernel via state overlap"""
        state1 = self.encode(x1)
        state2 = self.encode(x2)
        return abs(state1.inner(state2)) ** 2
