from sklearn.preprocessing import(StandardScaler,LabelEncoder)

def get_predictions(model,scaler:StandardScaler, encoder:LabelEncoder,data):
    data[:,:] = scaler.transform(data[:,:])
    predictions = model.predict()

    return predictions
