from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as IMG

def binarizing(img,threshold):
    """传入image对象进行灰度、二值处理"""
    img = img.convert("L") # 转灰度
    pixdata = img.load()
    w, h = img.size
    # 遍历所有像素，大于阈值的为黑色
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img

def vertical(img):
    """传入二值化后的图片进行垂直投影"""
    pixdata = img.load()
    w,h = img.size
    ver_list = []
    # 开始投影
    for x in range(w):
        black = 0
        for y in range(h):
            if pixdata[x,y] == 0:
                black += 1
        ver_list.append(black)
    # 判断边界
    l,r = 0,0
    flag = False
    cuts = []
    for i,count in enumerate(ver_list):
        # 阈值这里为0
        if flag is False and count > 0:
            l = i
            flag = True
        if flag and count == 0:
            r = i-1
            flag = False
            cuts.append((l,r))
    return cuts

if __name__ == '__main__':
    captcha_dir = './project/Subscribe/test/'
    p = Image.open('./project/Subscribe/test/132.png')
    
    b_img = p.convert('L')
    b_img = binarizing(b_img,200)
    # b_img.save('./project/Subscribe/test/132_gray.png')
    # im = Image.open('./project/Subscribe/test/132_gray.png')
    boxs = vertical(b_img)
    print(boxs)
    print(len(boxs))
    cnt = 1
    for subbox in boxs:
        subbox = (subbox[0], 0, subbox[1], 48)
        img = b_img.crop(subbox)
        width = img.size[0] 
        if width >= 15:
            mid = img.size[0] // 2
            print('mid = %d' % mid)
            img1 = img.crop((0, 0, mid, 48))
            img1.save(captcha_dir + str(cnt) + '.png')
            cnt += 1
            img2 = img.crop((mid, 0, width, 48))
            print('++++++++++++')
            img2.save(captcha_dir + str(cnt) + '.png')
            cnt += 1
            print('---------------')
        else:
            img.save(captcha_dir + str(cnt) + '.png')
            cnt += 1
    # im = Image.open('./project/Subscribe/test/2.png')
    # im = im.resize((8,48))
    # im.save('./project/Subscribe/test/2.png')
    # img = IMG.imread('./project/Subscribe/test/2.png')
    # plt.imshow(img)
    # plt.show()