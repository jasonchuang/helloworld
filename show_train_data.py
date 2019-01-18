from keras.datasets import mnist
from keras.utils import np_utils
from PIL import Image

# Read MNIST data
print 'read mnist data...'
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# outpout image in advance for train and test in advance
img = Image.fromarray(x_train[0], 'L')
img.save('mnist_train_0.png')

# 60000 for train and 10000 for test
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# Use reshape to flatten to 768 input vector
print 'data translation to 768 input vector'
x_train = x_train.reshape(x_train.shape[0], 28 * 28).astype('float32')
x_test = x_test.reshape(x_test.shape[0], 28 * 28).astype('float32')

# Standardize feature data
print 'standardize'
x_train /= 255
x_test /= 255

print(y_train[0], ' y_train[0] before categorical')
y_train = np_utils.to_categorical(y_train, 10)
print(y_train[0], ' y_train[0] after categorical')
