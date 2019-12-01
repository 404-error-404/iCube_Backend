#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-11-30 12:06:35
# @Author   : 张佳乐
# @Remarks  : 上传文件到oss
# @File     : upload_to_oss.py
# @Software : PyCharm
# Copyright © 2019 张佳乐. All rights reserved.

import oss2


def upload_to_oss_and_get_url(image_url_local, filename):
    """
    上传图片到阿里云然后获取返回值
    :param filename: 文件名
    :param image_url_local: 图片本地地址
    :return:
    """
    # TODO 删除隐私信息
    # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录
    # https://ram.console.aliyun.com 创建RAM账号。
    auth = oss2.Auth('就不告诉你', '就不告诉你')
    # Endpoint以杭州为例，其它Region请按实际情况填写。
    bucket = oss2.Bucket(
        auth,
        'http://oss-cn-beijing.aliyuncs.com',
        'couseraccess'
    )

    # 必须以二进制的方式打开文件，因为需要知道文件包含的字节数。
    with open(image_url_local, 'rb') as file_obj:
        # Seek方法用于指定从第1000个字节位置开始读写。上传时会从您指定的第1000个字节位置开始上传，直到文件结束。
        # file_obj.seek(1000, os.SEEK_SET)
        # Tell方法用于返回当前位置。
        # current = file_obj.tell()
        result = bucket.put_object(filename, file_obj)
        return result.resp.response.url


# print(upload_to_oss_and_get_url(r"I:\桌面\杂项\图库\仓木麻衣jpg (16).jpg"))
