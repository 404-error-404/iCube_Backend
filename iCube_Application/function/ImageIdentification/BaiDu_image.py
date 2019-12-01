#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-11-28 19:47:05
# @Author   : 张佳乐
# @Remarks  : 百度云图像分析调用
# @File     : BaiDu_image.py
# @Software : PyCharm
# Copyright © 2019 张佳乐. All rights reserved.

from aip import AipImageClassify


def get_file_content(file_path):
    """
    读取图片文件
    :param file_path: 文件路径
    :return: 读取到的文件数据
    """
    with open(file_path, 'rb') as fp:
        return fp.read()


def BaiDu_image_recognize(file_path, recognize_type):
    """
    图像识别
    :param file_path: 文件路径
    :param recognize_type: 识别类型，共12种：
                1. 通用图像识别
                2. 菜品识别
                3. 车辆识别
                4. logo商标识别
                5. 动物识别
                6. 植物识别
                7. 图像主体检测
                8. 地标识别
                9. 食材识别
                10. 红酒识别
                11. 货币识别
    :return:
    """
    # TODO 隐私信息
    """ 你的 APP_ID API_KEY SECRET_KEY """
    app_id = '就不告诉你'     # '你的 App ID'
    api_key = '就不告诉你'    # '你的 Api Key'
    secret_key = '就不告诉你 '    # '你的 Secret Key'

    # 获取百度云操作类对象
    client = AipImageClassify(app_id, api_key, secret_key)
    image = get_file_content(file_path)

    # """ 调用通用物体识别 """
    # result = client.dishDetect(image)
    # print(result)
    """ 如果有可选参数 """
    options = {
        "baike_num": 5
    }

    """ 带参数调用通用物体识别 """
    if recognize_type == 1:     # 通用图像识别
        response = client.advancedGeneral(image, options)
    elif recognize_type == 2:   # 菜品识别
        response = client.dishDetect(image, options)
    elif recognize_type == 3:   # 车辆识别
        response = client.carDetect(image, options)
    elif recognize_type == 4:   # logo商标识别
        response = client.logoSearch(image)
    elif recognize_type == 5:   # 动物识别
        response = client.animalDetect(image, options)
    elif recognize_type == 6:   # 植物识别
        response = client.plantDetect(image, options)
    elif recognize_type == 7:   # 图像主体检测
        response = client.objectDetect(image)
    elif recognize_type == 8:   # 地标识别
        response = client.landmark(image)
    # 花卉识别已经移除
    # elif recognize_type == 9:   # 花卉识别
    #     response = client.flower(image)
    elif recognize_type == 9:   # 食材识别
        response = client.ingredient(image, options)
    elif recognize_type == 10:   # 红酒识别
        response = client.redwine(image)
    elif recognize_type == 11:   # 货币识别
        response = client.currency(image)
    else:
        response = None
    response = response['result'][0]
    return response


# image_url = r"C:\Users\APTX4869\Desktop\零杯\小功能\图像分析\{name}.jpg"
# for i in range(1, 12):
#     image_url_now = image_url.format(name=str(i))
#     result = BaiDu_image_recognize(image_url_now, i)
#     print(result)
