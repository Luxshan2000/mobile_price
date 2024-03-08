import pandas as pd
from src.utils.model import(load_model)
from flask import Flask, request, jsonify
from .predict import (get_predictions)
from src.utils.load_logging import(get_logger)

logger = get_logger(__name__)
app = Flask(__name__)
model, scaler, encoder = load_model()


@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    data = pd.DataFrame(data).fillna(0)
    logger.info(data)
    # prediction = get_predictions(model,scaler,encoder,data)
    # return jsonify({'prediction': prediction})
    return "done"


if __name__ == '__main__':
    app.run(debug=True)
