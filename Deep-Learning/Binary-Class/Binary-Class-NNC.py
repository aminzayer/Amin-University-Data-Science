# first neural network with keras tutorial
from keras.callbacks import ModelCheckpoint
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
from numpy import loadtxt
from pandas import read_csv
#from pandas import read_
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.vis_utils import plot_model
from keras.models import Model, load_model

# load the dataset
dataset = loadtxt('heart-failure.data.txt', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:, 0:12]
y = dataset[:, 12]

print(X.shape)
print(y.shape)
print(type(X))

print(y)

# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
#from keral.optimizer import adam
model.compile(loss='binary_crossentropy', optimizer='RMSProp',
              metrics=['accuracy'])  # categorical_crossentropy
print(model.summary())
plot_model(model, show_shapes=True, to_file='model1.png')


# param_number = output_channel_number * (input_channel_number + 1)
# fit the keras model on the dataset
history = model.fit(X, y, epochs=100, batch_size=10)

plt.figure()
plt.plot(history.history['loss'])

# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

predictions = model.predict(X)
# summarize the first 5 cases
for i in range(10):
    print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))

es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=20)
mc = ModelCheckpoint('best_model.h5', monitor='val_accuracy',
                     mode='max', verbose=1, save_best_only=True)
history = model.fit(X, y, epochs=100, batch_size=10, verbose=1, validation_split=0.2, callbacks=[
                    mc, es])  # validation_data=[test_x, test_y]
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['loss', 'val_loss'], loc='upper right')
plt.figure()
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.legend(['acc', 'val_acc'], loc='upper right')

model = load_model('best_model.h5')
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
predictions = model.predict(X)
# summarize the first 5 cases
for i in range(5):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))
