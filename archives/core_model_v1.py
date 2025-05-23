import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def train_brain(data):
    xor_result = np.bitwise_xor(data[:-1], data[1:])

    def moving_average(values, window_size):
        return np.convolve(values, np.ones(window_size)/window_size, mode='valid')

    ma_3 = moving_average(xor_result, 3)

    correlation_matrix = np.corrcoef(np.vstack([xor_result[:len(ma_3)], ma_3]))
    correlation_strength = correlation_matrix[0, 1]

    X = np.array([data[i:i+3] for i in range(len(data)-3)], dtype=np.float32).reshape(-1, 1, 3)
    y = np.array([data[i+3] for i in range(len(data)-3)], dtype=np.float32)

    model = Sequential([
        LSTM(50, activation='relu', input_shape=(1, 3)),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=200, verbose=0)

    return model, correlation_strength
