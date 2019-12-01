#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-11-30 16:37:21
# @Author   : 张佳乐
# @Remarks  : MD5加密
# @File     : md5_encode.py
# @Software : PyCharm
# Copyright © 2019 张佳乐. All rights reserved.

from hashlib import md5


def get_md5_encode(image_local_url):
    """
    获取图片md5值
    :param image_url: image地址
    :return: 图片md5值
    """
    md5_encoding = md5()
    img = open(image_local_url, 'rb')
    md5_encoding.update(img.read())
    img.close()
    return md5_encoding.hexdigest()


# result = get_md5_encode(r"C:\Users\APTX4869\Desktop\零杯\小功能\图像分析\1.jpg")
# print(result)
