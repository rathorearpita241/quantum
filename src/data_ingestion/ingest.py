import pandas as pd

class DataIngestion:
    def load_dummy_bee_data(self):
        """
        Temporary dummy dataset for testing pipeline
        """
        data = {
            "bee_id": [1, 2, 3, 4],
            "latitude": [18.52, 18.53, 18.54, 18.55],
            "longitude": [73.85, 73.86, 73.87, 73.88],
            "temperature": [30, 31, 29, 32]
        }
        return pd.DataFrame(data)
