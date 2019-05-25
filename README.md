### 图书馆自动预约的实现

#### 基本原理
通过selenium工具登录图书馆预约网址，获取一定量的验证码图片，然后对图片进行灰度、二值化、分割、调整大小最终称为28x28的单字符图片的训练样本，然后进行归一化和onehot编码批量输入图片和标签进入神经网络，训练好模型，随后即可利用模型识别验证码

![](https://ztq-img.oss-cn-hangzhou.aliyuncs.com/captcha.png)

#### 前期工作

* 步骤一：环境配置
  
    安装keras、tensorflow框架，Python3环境安装

* 步骤二：生成验证码

        python3 captcha_gen.py
    
* 步骤三：批量处理验证码

        python3 captcha_process.py

* 步骤四：统一图片的大小

        python3 captcha_resize.py

* 步骤五：训练模型

        python3 captcha_train.py
    
* 步骤六：识别验证码

        python3 captcha_predict.py


#### 最终实现

最终用于图书馆预约处理的程序就是主程序：main.py

    python3 main.py

由于时间紧迫，程序只实现了所需主要功能，还有很多细节有待完善，以后有时间再慢慢完善