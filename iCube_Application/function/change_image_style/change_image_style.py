#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-12-01 02:39:16
# @Author   : 张佳乐
# @Remarks  : 图像风格转换
# @File     : change_image_style.py
# @Software : PyCharm
# Copyright © 2019 张佳乐. All rights reserved.

from iCube_Application.models import ImageStyleChange


def image_style_changed(content_image_url, style_image_url):
    json_result = {}
    try:
        # 获取文件名
        content_image = content_image_url[-36:]
        style_image = style_image_url[-36:]
        # 查看网址是否符合要求
        if not content_image_url[:-36] == style_image_url[:-36] == \
                "http://couseraccess.oss-cn-beijing.aliyuncs.com/":
            json_result["statusCode"] = 510
            json_result["messageDetail"] = "图片不合法"
        else:
            # 如果这两张图片已经合成过
            find_image_changed = ImageStyleChange.objects.get(
                content_image=content_image,
                style_image=style_image
            )
            amazing_image = find_image_changed.amazing_image
            amazing_image_url = "http://couseraccess.oss-cn-beijing.aliyuncs.com/" + amazing_image
            json_result["statusCode"] = 0
            json_result["messageDetail"] = {
                "content_image_url": content_image_url,
                "style_image_url": style_image_url,
                "amazing_image_url": amazing_image_url
            }
    except Exception:
        # 添加异步处理
        json_result["statusCode"] = 511
        json_result["messageDetail"] = "图片处理时间较长（可能2~4个小时）我们已经在后台进行处理，请稍后再来查看"
    return json_result
