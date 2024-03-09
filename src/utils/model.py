import os
import pickle


def save_model(model_info):
    with open(f"{os.getcwd()}/model/xgb_model.pkl", "wb") as f:
        pickle.dump(model_info, f)


def load_model():
    with open(f"{os.getcwd()}/model/xgb_model.pkl", "rb") as f:
        model, scaler, label_encoder, columns = pickle.load(f)
    return model, scaler, label_encoder, columns
