#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-11-30 13:43:49
# @Author   : 张佳乐
# @Remarks  : 百度云图像识别颜值打分
# @File     : Face_recognize.py
# @Software : PyCharm
# Copyright © 2019 张佳乐. All rights reserved.

from aip import AipFace


def face_age_score(image_url):
    # TODO 删除隐私信息
    """ 你的 APP_ID AK SK """
    app_id = '就不告诉你'
    api_key = '就不告诉你'
    secret_key = '就不告诉你'

    client = AipFace(
        app_id,
        api_key,
        secret_key
    )

    # image_url = r"I:\桌面\杂项\图库\仓木麻衣jpg (16).jpg"

    # with open(image_url,"rb") as f:
    #     # b64encode是编码，b64decode是解码
    #     base64_data = base64.b64encode(f.read())
    #     # base64.b64decode(base64data)
    #     # print(base64_data)

    image = image_url
    image_type = "URL"

    """ 如果有可选参数 """
    options = {
        "face_field": "age,beauty"
    }

    """ 带参数调用人脸检测 """
    result = client.detect(image, image_type, options)
    try:
        face_information = {
            "age": result["result"]["face_list"][0]["age"],
            "score": result["result"]["face_list"][0]["beauty"]
        }
    except Exception:
        face_information = "未识别到人脸"
    return face_information


# face_score("http://couseraccess.oss-cn-beijing.aliyuncs.com/%E4%BB%93%E6%9C%A8%E9%BA%BB%E8%A1%A3.jpg")
