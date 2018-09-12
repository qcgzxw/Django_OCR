# Django_OCR
接口练习，调用腾讯云OCR接口实现各种图片的识别。

## 配置说明：
Python 3.7

Django 2.1a1

## 使用说明：
下载所有代码后，更改 ==/apps/txystsb/== 目录下的conf.py配置文件。

进入到虚拟环境，在根目录下执行 ==python manager.py runserver [端口]==

访问 ==127.0.0.1:[端口]== 即可看到初始界面，直接上传图片，选择对应的识别方式开始图片识别。

## 功能为实现原因
由于腾讯云OCR接口问题，目前就通用印刷体和手写体识别能够正常使用
* 接口返回值错误码不一致
* 接口返回值非Json数据
* ···

![IMG01](https://i.loli.net/2018/09/12/5b98812fbbad5.png)

![IMG02](https://i.loli.net/2018/09/12/5b98812fc610f.png)