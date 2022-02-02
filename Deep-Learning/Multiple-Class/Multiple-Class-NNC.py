# # کدهای پیاده سازی پروژه پایان ترم بیگ دیتا  - امین زایراومالی

# # وارد کردن کتابخانه های مورد نیاز پایتون


# first neural network with keras tutorial with letter Dataset
# Dataset Link : https://archive.ics.uci.edu/ml/datasets/Letter+Recognition
# Powered By Amin Zayeromali  - amin.Zayeroamli@gmail.com
from keras.callbacks import ModelCheckpoint
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
from numpy import loadtxt
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.vis_utils import plot_model
import tensorflow as tf
from keras.models import Model, load_model
from sklearn import preprocessing
import math


# ## بارگزاری دیتاست و توضیحات مشخصه آن
# DataSet Information
# Author: David J. Slate
# Source: [UCI](https://archive.ics.uci.edu/ml/datasets/Letter+Recognition) - 01-01-1991
# Please cite: P. W. Frey and D. J. Slate. "Letter Recognition Using Holland-style Adaptive Classifiers". Machine Learning 6(2), 1991

# TITLE:  Letter Image Recognition Data
#
#    The objective is to identify each of a large number of black-and-white
#    rectangular pixel displays as one of the 26 capital letters in the English
#    alphabet.  The character images were based on 20 different fonts and each
#    letter within these 20 fonts was randomly distorted to produce a file of
#    20,000 unique stimuli.  Each stimulus was converted into 16 primitive
#    numerical attributes (statistical moments and edge counts) which were then
#    scaled to fit into a range of integer values from 0 through 15.  We
#    typically train on the first 16000 items and then use the resulting model
#    to predict the letter category for the remaining 4000.  See the article
#    cited above for more details.

# load the dataset
dataset = loadtxt('dataset_6_letter.txt', dtype=str, delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:10000, 0:16]  # انتخاب ۱۰۰۰۰ هزار رکورد از داده ها برای ترین
X = X.astype(float)
y = dataset[:10000, 16]
le = preprocessing.LabelEncoder()
y = le.fit_transform(y).astype(int)
print("Number Of Unique Label on Target :", len(
    set(y)))  # تعداد کلاسهای یونیک مشخص می شود
y = tf.keras.utils.to_categorical(y, num_classes=len(
    set(y)))  # تبدیل داده های اینتیجر لیبل به باینری

# نمایش تعداد رکوردهای دیتاست ( فیچرها و لیبلهای تارگت )
print(X.shape)
print(y.shape)
print(X)

print(y)  # لیبل بندی کلاسهای خروجی براساس تعداد اپوچ های خروجی با فرمت باینری

# # ساخت مدل برای دیتاست مذکور که به صورت چند کلاسه
# ##  مرحله اول فقط دو لایه پنهان با ورودی ۱۶ تایی و خروجی ۲۶ تایی ساخته و فیت می کنیم
# param_number = output_channel_number * (input_channel_number + 1)

# define the keras model
model = Sequential()
# تعداد نورون های ورودی برابر با فیچر ها ۱۶ تاست
model.add(Dense(32, input_dim=16, activation='relu'))
#model.add(Dense(64, activation='relu'))
# تعداد نورون های خروجی نیز برابر با تعداد لیبلهای غیر تکراری کلاس تارگت گرفتیم
model.add(Dense(26, activation='sigmoid'))
# compile the keras model
#from keral.optimizer import adam
model.compile(loss='categorical_crossentropy', optimizer='RMSProp', metrics=[
              'accuracy'])  # categorical_crossentropy or #binary_crossentropy
print(model.summary())
plot_model(model, show_shapes=True, to_file='mymodel.png')


# ## مدل را برای مقادیر epochs=50, batch_size=10 ساخته و فیت می کنیم

# fit the keras model on the dataset
history = model.fit(X, y, epochs=50, batch_size=10)

plt.figure()
plt.plot(history.history['loss'])


plt.figure()
plt.plot(history.history['accuracy'])

# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))


predictions = model.predict(X)
# summarize the first 5 cases
for i in range(10):
    print("\n------------------------------- Case ", i+1,
          " ---------------------------------------------------\n")
    print("Data is :\n", X[i].tolist(), "\nPredicted Value is :\n",
          predictions[i], "\nReal Value is :\n", y[i])


# ## مدل را برای مقادیر epochs=100, batch_size=50 ساخته و فیت می کنیم

# define the keras model
model = Sequential()
# تعداد نورون های ورودی برابر با فیچر ها ۱۶ تاست
model.add(Dense(32, input_dim=16, activation='relu'))
#model.add(Dense(64, activation='relu'))
# تعداد نورون های خروجی نیز برابر با تعداد لیبلهای غیر تکراری کلاس تارگت گرفتیم
model.add(Dense(26, activation='sigmoid'))
# compile the keras model
#from keral.optimizer import adam
model.compile(loss='categorical_crossentropy', optimizer='RMSProp', metrics=[
              'accuracy'])  # categorical_crossentropy or #binary_crossentropy
print(model.summary())
plot_model(model, show_shapes=True, to_file='mymodel.png')

# fit the keras model on the dataset
history = model.fit(X, y, epochs=100, batch_size=50)


plt.figure()
plt.plot(history.history['loss'])


plt.figure()
plt.plot(history.history['accuracy'])


# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

predictions = model.predict(X)
# summarize the first 5 cases
for i in range(10):
    print("\n------------------------------- Case ", i+1,
          " ---------------------------------------------------\n")
    print("Data is :\n", X[i].tolist(), "\nPredicted Value is :\n",
          predictions[i], "\nReal Value is :\n", y[i])


# #   مدل را سه لایه پنهان  و برای مقادیر توینیگ شده و بهینه فیت و ترین می کنیم
# define the keras model
model = Sequential()
# تعداد نورون های ورودی برابر با فیچر ها ۱۶ تاست
model.add(Dense(32, input_dim=16, activation='relu'))
model.add(Dense(64, activation='relu'))
# تعداد نورون های خروجی نیز برابر با تعداد لیبلهای غیر تکراری کلاس تارگت گرفتیم
model.add(Dense(26, activation='sigmoid'))
# compile the keras model
#from keral.optimizer import adam
model.compile(loss='categorical_crossentropy', optimizer='RMSProp', metrics=[
              'accuracy'])  # categorical_crossentropy or #binary_crossentropy
print(model.summary())
plot_model(model, show_shapes=True, to_file='mymodel.png')

# fit the keras model on the dataset
history = model.fit(X, y, epochs=100, batch_size=50)

plt.figure()
plt.plot(history.history['loss'])


plt.figure()
plt.plot(history.history['accuracy'])

# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

predictions = model.predict(X)
# summarize the first 5 cases
for i in range(10):
    print("\n------------------------------- Case ", i+1,
          " ---------------------------------------------------\n")
    print("Data is :\n", X[i].tolist(), "\nPredicted Value is :\n",
          predictions[i], "\nReal Value is :\n", y[i])


# # این بار مدل را برای اپوچ ۲۵۰ تایی اجرا می کنیم
# define the keras model
model = Sequential()
# تعداد نورون های ورودی برابر با فیچر ها ۱۶ تاست
model.add(Dense(32, input_dim=16, activation='relu'))
model.add(Dense(64, activation='relu'))
# تعداد نورون های خروجی نیز برابر با تعداد لیبلهای غیر تکراری کلاس تارگت گرفتیم
model.add(Dense(26, activation='sigmoid'))
# compile the keras model
#from keral.optimizer import adam
model.compile(loss='categorical_crossentropy', optimizer='RMSProp', metrics=[
              'accuracy'])  # categorical_crossentropy or #binary_crossentropy
print(model.summary())
plot_model(model, show_shapes=True, to_file='mymodel.png')

# fit the keras model on the dataset
history = model.fit(X, y, epochs=250, batch_size=50)

plt.figure()
plt.plot(history.history['loss'])

plt.figure()
plt.plot(history.history['accuracy'])

# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

predictions = model.predict(X)
# summarize the first 5 cases
for i in range(10):
    print("\n------------------------------- Case ", i+1,
          " ---------------------------------------------------\n")
    print("Data is :\n", X[i].tolist(), "\nPredicted Value is :\n",
          predictions[i], "\nReal Value is :\n", y[i])


# # ساخت مدل با ولیدیشن و استاپ لاست برای مدل بهینه تر

es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=20)
mc = ModelCheckpoint('best_model.h5', monitor='val_accuracy',
                     mode='max', verbose=1, save_best_only=True)
history = model.fit(X, y, epochs=250, batch_size=10, verbose=1, validation_split=0.2, callbacks=[
                    mc, es])  # validation_data=[test_x, test_y]
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['loss', 'val_loss'], loc='upper right')
plt.figure()
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.legend(['acc', 'val_acc'], loc='upper right')


# # با استفاده از مدل بهینه تعداد ۵ نمونه را تست میگیریم و نتایج را مشخص می کنیم
model = load_model('best_model.h5')
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
predictions = model.predict(X)
# summarize the first 5 cases
for i in range(5):
    print("\n------------------------------- Case ", i+1,
          " ---------------------------------------------------\n")
    print("Data is :\n", X[i].tolist(), "\nPredicted Value is :\n",
          predictions[i], "\nReal Value is :\n", y[i])
