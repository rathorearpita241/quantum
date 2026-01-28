
import pandas as pd

class Preprocessor:
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Handle missing values and invalid rows"""
        df = df.dropna()
        return df

    def normalize(self, df: pd.DataFrame) -> pd.DataFrame:
        """Normalize numeric columns"""
        numeric_cols = df.select_dtypes(include="number").columns
        df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std()
        return df