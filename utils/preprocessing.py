import pandas as pd

def clean_missing(df):
    return df.dropna()

def fill_missing(df, method="mean"):
    return df.fillna(df.mean()) if method == "mean" else df.fillna(method)

def encode_categoricals(df):
    return pd.get_dummies(df)
