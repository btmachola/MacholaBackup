import matplotlib.pyplot as plt
import numpy as np
import cv2
import tensorflow as tf
import pathlib

from tensorflow import keras
from sklearn.model_selection import train_test_split

dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file('flower_photos', origin=dataset_url,  cache_dir='.', untar=True)

data_dir = pathlib.Path(data_dir)

image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)

flowers_images_dict = {
    'roses': list(data_dir.glob('roses/*')),
    'daisy': list(data_dir.glob('daisy/*')),
    'dandelion': list(data_dir.glob('dandelion/*')),
    'sunflowers': list(data_dir.glob('sunflowers/*')),
    'tulips': list(data_dir.glob('tulips/*')),
}

flowers_labels_dict = {
    'roses': 0,
    'daisy': 1,
    'dandelion': 2,
    'sunflowers': 3,
    'tulips': 4,
}


X, y = [], []
a=[]
b=[]

for x, z in flowers_images_dict.items():
    for image in z:
        img = cv2.imread(str(image))
       
        resized_img = cv2.resize(img,(180,180))
        X.append(resized_img)
        y.append(flowers_labels_dict[x])
        


X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.25, random_state=0)

X_train_scaled = X_train / 255
X_test_scaled = X_test / 255

num_classes = 5

model = keras.Sequential([
  keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(180,180,3)),
  keras.layers.MaxPooling2D((2,2)),
  keras.layers.Conv2D(40, (3,3), activation='relu'),
  keras.layers.MaxPooling2D((2,2)),
  keras.layers.Conv2D(100, (3,3), activation='relu'),
  keras.layers.MaxPooling2D((2,2)),
  keras.layers.Flatten(),
  keras.layers.Dense(128, activation='relu'),
  keras.layers.Dense(num_classes)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
              
model.fit(X_train_scaled, y_train, epochs=3)


model.evaluate(X_test_scaled,y_test)

predictions = model.predict(X_test_scaled)

model.save("mycnnf.h5")
