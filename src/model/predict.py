import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from xgboost import XGBClassifier


def get_predictions(
    model: XGBClassifier,
    scaler: StandardScaler,
    encoder: LabelEncoder,
    data: pd.DataFrame,
):
    x_source = data.values
    x_source[:, :] = scaler.transform(x_source[:, :])
    y_source = model.predict(x_source)
    predictions = encoder.inverse_transform(y_source)

    return predictions.tolist()
