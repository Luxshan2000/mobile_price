import pandas as pd
from flask import Flask, jsonify, make_response, request

from src.utils.load_logging import get_logger
from src.utils.model import load_model

from .predict import get_predictions

logger = get_logger(__name__)
app = Flask(__name__)
model, scaler, encoder, train_columns = load_model()


@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.json
    columns = data["columns"]
    rows = data["rows"]

    try:
        data = pd.DataFrame(columns=columns, data=rows).fillna(0)
        data = data[train_columns]
        predictions = get_predictions(model, scaler, encoder, data)
        logger.info(predictions)
        return jsonify({"predictions": predictions})
    except Exception as ep:
        response = make_response(jsonify({"Error": ep}))
        response.status_code = 400
        return response


if __name__ == "__main__":
    app.run(debug=True)
