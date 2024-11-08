import os
import pickle
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from fatigue_life_predictor.attention import Attention
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from tensorflow.keras.metrics import MeanSquaredError
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.layers import Layer


def load_trained_model():
    model_path = os.path.join(os.path.dirname(__file__), 'fatigue_life_model.h5')
    model = load_model(
        model_path, 
        custom_objects={
            'Attention': Attention, 
            'MeanSquaredError': MeanSquaredError,
            'mse': MeanSquaredError()
        }
    )
    model.compile(optimizer='adam', loss='mse', metrics=[MeanSquaredError()])
    return model

def load_scalers():
    # 스케일러 파일 경로 설정
    scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')
    nf_scaler_path = os.path.join(os.path.dirname(__file__), 'nf_scaler.pkl')
    
    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)
    with open(nf_scaler_path, 'rb') as f:
        nf_scaler = pickle.load(f)
    
    return scaler, nf_scaler

def predict_fatigue_life(model, scaler, nf_scaler, df, n_timesteps=50):
    # 데이터 전처리
    if len(df) < n_timesteps:
        raise ValueError("입력 데이터의 길이가 n_timesteps보다 짧습니다.")
    
    X_input = df[['Stress', 'Strain']].values[:n_timesteps]
    X_input = X_input.reshape(1, n_timesteps, 2)
    X_input_scaled = scaler.transform(X_input.reshape(-1, 2)).reshape(1, n_timesteps, 2)
    
    # 예측 수행
    y_pred, _ = model.predict(X_input_scaled)
    y_pred_original = nf_scaler.inverse_transform(y_pred)
    
    return y_pred_original[0][0]
