import os
from PIL import Image


class_name = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def load_data(dir_path):
    for i in range(len(class_name)):
        train_path = dir_path + class_name[i]
        files = os.listdir(train_path)
        for file in files:
            fullpath = os.path.join(train_path, file)
            im = Image.open(fullpath)
            print(fullpath)
            im = im.resize((25,25), Image.ANTIALIAS)
            im.save(fullpath)
            
if __name__ == '__main__':
    train_dir = './project/Subscribe/dataset/train/'
    load_data(train_dir)