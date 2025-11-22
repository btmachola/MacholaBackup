import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM, Flatten
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


dataframe = read_csv('gold_prices_india.csv', usecols=[1])


dataset = dataframe.values
dataset = dataset.astype('float32')

scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)

def to_sequences(dataset, seq_size):
    x = []
    y = []

    for i in range(len(dataset)-seq_size-5):
       
        window = dataset[i:(i+seq_size), 0]
        x.append(window)
        y.append(dataset[i+seq_size, 0])
        
    return np.array(x),np.array(y)

seq_size = 20

X, Y = to_sequences(dataset, seq_size)

X = np.reshape(X, (X.shape[0], 1, X.shape[1]))

model = Sequential()
model.add(LSTM(50, input_shape=(None, seq_size)))
model.add(Dense(100))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

model.summary()


model.fit(X, Y, validation_data=(X, Y),
          verbose=2, epochs=100)

trainPredict = model.predict(X)

trainPredict1 = scaler.inverse_transform(trainPredict)
YI = scaler.inverse_transform([Y])

def to_sequences_P(dataset, seq_size):
    x = []

    for i in range(len(dataset)-seq_size-5, len(dataset)-seq_size+1):
       
        window = dataset[i:(i+seq_size), 0]
        x.append(window)
        
        
    return np.array(x)

XP = to_sequences_P(dataset, seq_size)

XP = np.reshape(XP, (XP.shape[0], 1, XP.shape[1]))

print(scaler.inverse_transform(model.predict(XP)))
