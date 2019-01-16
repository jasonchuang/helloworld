from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from PIL import Image

import numpy as np
import pandas as pd

num_classes = 10
num_epochs = 20
num_batch_size = 300

# Read MNIST data
print 'read mnist data...'
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# outpout image in advance for train and test in advance
img = Image.fromarray(x_train[0], 'L')
img.save('mnist_train_0.png')

img = Image.fromarray(x_test[240], 'L')
img.save('mnist_test_240.png')
img = Image.fromarray(x_test[249], 'L')
img.save('mnist_test_249.png')

# 60000 for train and 10000 for test
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# Use reshape to flatten to 768 input vector
print 'data translation to 768 input vector'
x_train = x_train.reshape(x_train.shape[0], 28 * 28).astype('float32')
x_test = x_test.reshape(x_test.shape[0], 28 * 28).astype('float32')

# Standardize feature data for x and y respectively
print 'standardize x and y'
origin_y_test = y_test
x_train /= 255
x_test /= 255

print(y_train[0], ' y_train[0] before categorical')
y_train = np_utils.to_categorical(y_train, num_classes)
print(y_train[0], ' y_train[0] after categorical')
y_test = np_utils.to_categorical(y_test, num_classes)

print 'model init and summary'
model = Sequential()
model.add(Dense(633, activation='relu', input_shape=(784,)))
model.add(Dense(92, activation='relu'))
model.add(Dense(426, activation='relu'))
model.add(Dense(689, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.summary()

# training, keras losses: https://keras.io/losses/
model.compile(loss='mean_squared_error', optimizer='sgd',
		metrics=['accuracy'])
# model.compile(loss='categorical_crossentropy', optimizer='adam',

train_history = model.fit(x_train, y_train,
				validation_split = 0.2,
                epochs = num_epochs,
				batch_size = num_batch_size,
				verbose = 2)

# try to infer via test dataset
scores = model.evaluate(x_test, y_test)
print("\t[Info] Accuracy of testing data = {:2.1f}%".format(scores[1]*100.0))

# result
print("\t[Info] Making prediction of x_test")
prediction = model.predict_classes(x_test)
print()
print("\t[Info] Show 10 prediction result (from 240):")
print("\n\n\t[Result]: %s\n\n" % (prediction[240:250]))

# confusion matrix
print("\t[Info] Display Confusion Matrix:")
print("%s\n" % pd.crosstab(origin_y_test, prediction, rownames=['label'], colnames=['predict']))

