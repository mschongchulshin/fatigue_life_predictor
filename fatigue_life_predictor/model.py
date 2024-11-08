from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError
import os
from .attention import Attention  


def load_trained_model():
    model_path = os.path.join(os.path.dirname(__file__), 'fatigue_life_model.h5')
    model = load_model(
        model_path, 
        custom_objects={
            'Attention': Attention, 
            'mse': MeanSquaredError()
        }
    )
    return model
    
def predict_fatigue_life(model, X, nf_scaler):
    y_pred, _ = model.predict(X)
    return nf_scaler.inverse_transform(y_pred)
