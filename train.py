import numpy as np
from PIL import Image
import os


def capt_inference(sub_capt):
    capt = Image.open(sub_capt)
    char_array = np.array(capt)
    print(char_array)
    total_pixels = np.sum(char_array)
    cols_pixels = np.sum(char_array, 0)
    rows_pixels = np.sum(char_array, 1)
    char_features = np.append(cols_pixels, rows_pixels)
    char_features = np.append(total_pixels, char_features)
    return char_features.tolist()


def train(train_path):
    files = os.listdir(train_path)
    train_table = []
    train_label = []
    for file in files:
        train_label += list(file.split('_')[0])
        char_features = capt_inference(train_path + file)
        train_table.append(char_features)
    return train_table, train_label


def nnc(train_tabel, test_vec, train_label):
    dist_mat = np.square(np.subtract(train_tabel, test_vec))
    dist_vec = np.sum(dist_mat, axis=1)
    pos = np.argmin(dist_vec)
    return train_label[pos]

def test(train_path):
    test_label = []
    train_tabel, train_label = train(train_path)
    files = os.listdir(train_path)
    for file in files:
        char_features = capt_inference(train_path + file)
        label = nnc(train_tabel, char_features, train_label)
        test_label.append(label)      
    test_label = "".join(test_label)
    return test_label

if __name__ == '__main__':
    train_path = './project/Subscribe/train/'
    res = test(train_path)
    print(res)
