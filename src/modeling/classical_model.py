
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

class ClassicalWeatherModel:
    def __init__(self):
        self.model = RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )

    def train(self, df: pd.DataFrame):
        X = df[["latitude", "longitude"]]
        y = df["temperature"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.25, random_state=42
        )

        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)

        mse = mean_squared_error(y_test, predictions)
        print(f"Model trained | MSE: {mse:.4f}")

    def predict(self, lat, lon):
        return self.model.predict([[lat, lon]])[0]
