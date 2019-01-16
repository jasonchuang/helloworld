from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(633, activation='relu', input_shape=(784,)))
model.add(Dense(92, activation='relu'))
model.add(Dense(426, activation='relu'))
model.add(Dense(689, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.summary()

