import os

import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from xgboost import XGBClassifier

from src.utils.load_logging import get_logger
from src.utils.model import save_model

# Define logger
logger = get_logger(__name__)

# Load the processed-data
logger.info("Data Loading Started!")
df_train = pd.read_csv(f"{os.getcwd()}/data/processed/train.csv")

# Get columns
columns = df_train.columns.values.tolist()
columns.pop()
logger.info(columns)

# Split X,Y
x = df_train.iloc[:, :-1].values
y = df_train.iloc[:, -1].values

# Split train, test
logger.info("Splitting data into train and test sets")
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.20, random_state=1234
)

# Scaling
logger.info("Scaling features")
standardScaler = StandardScaler()
x_train[:, :] = standardScaler.fit_transform(x_train[:, :])
x_test[:, :] = standardScaler.transform(x_test[:, :])

# Encoding
logger.info("Encoding target variable")
labelEncoder = LabelEncoder()
y_train = labelEncoder.fit_transform(y_train)

# Train the model
logger.info("Training the model")
XGB = XGBClassifier()
XGB.fit(x_train, y_train)

# Predict
logger.info("Making predictions")
y_pred = XGB.predict(x_test)
y_pred = labelEncoder.inverse_transform(y_pred)

# Validate
logger.info("Calculating accuracy")
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

logger.info(f"Confusion Matrix:\n{cm}")
logger.info(f"Accuracy: {accuracy}")

# Save Model
save_model((XGB, standardScaler, labelEncoder, columns))
logger.info(
    "XGBClassifier, StandardScaler, \
LabelEncoder,\
Columns stored succesfully!"
)
