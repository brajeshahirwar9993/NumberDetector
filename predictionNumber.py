import tensorflow as tf
import numpy as np
from tensorflow import keras
model = tf.keras.Sequential([keras.layers.Dense(units = 1,input_shape=[1])])
model.compile(optimizer='sgd',loss='mean_squared_error')
xs = np.array([1,2,3,4],dtype='float')
ys = np.array([5, 10, 15, 20],dtype='float')
model.fit(xs,ys,epochs=5000)
results = model.predict([34])
print(results)

