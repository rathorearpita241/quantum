import numpy as np
from src.modeling.classical_model import ClassicalWeatherModel
from src.modeling.quantum_model import QuantumWeatherModel

def compare_models(df):
    classical = ClassicalWeatherModel()
    classical.train(df)

    quantum = QuantumWeatherModel()

    x1 = np.array([[0.1, 0.2]])
    x2 = np.array([[0.2, 0.3]])

    similarity = quantum.compute_similarity(x1, x2)

    return {
        "classical_status": "trained",
        "quantum_similarity": similarity
    }

