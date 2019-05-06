import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image
from sklearn import metrics
import os
import keras
import tensorflow as tf

class_name = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def load_data(dir_path):
    x, y = None, None
    for i in range(len(class_name)):
        train_path = dir_path + class_name[i]
        files = os.listdir(train_path)
        for file in files:
            fullpath = os.path.join(train_path, file)
            im = Image.open(fullpath)
            im = im.convert('L')
            # print('++++++++++++')
            # print(im.size)
            im = Image.fromarray(np.uint8(im))
            im = np.array(im)
            # print('-----------')
            # print(im.shape)
            im = (np.expand_dims(im, 0))
            # print('*****************')
            # print(im.shape)

            if x is None:
                x = im
            else:
                x = np.vstack((x, im))
            if y is None:
                y = i
            else:
                y = np.vstack((y, i))
    return x, y


if __name__ == '__main__':
    epoch = 500
    print('start loading data')
    train_dir = './project/Subscribe/dataset/train/'
    test_dir = './project/Subscribe/dataset/test/'

    train_capt, train_label = load_data(train_dir)
    print(train_capt.shape, train_label.shape)
    test_capt, test_label = load_data(test_dir)
    print(test_capt.shape, test_label.shape)

    print('start building model')
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(16,16)),
        keras.layers.Dense(512, activation=tf.nn.relu),
        keras.layers.Dropout(0.4, noise_shape=None, seed=None),
        keras.layers.Dense(10, activation=tf.nn.softmax),
    ])
    model.summary()
    model.compile(optimizer=tf.train.AdadeltaOptimizer(),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    print('strat training')
    hist = model.fit(train_capt, train_label, epochs=epoch, shuffle=True)

    print('get accuracy')
    test_loss, test_acc = model.evaluate(test_capt, test_label)
    print('Test Accuracy', test_acc)
    model.save('./project/Subscribe/model.cy')
