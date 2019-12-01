#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-11-29 00:02:32
# @Author   : 张佳乐
# @Remarks  : 保存文件，返回文件位置
# @File     : save_file.py
# @Software : PyCharm
# Copyright © 2019 张佳乐. All rights reserved.

import os


def save_file(file):
    """
    保存文件并返回文件位置
    :param file: 待保存的文件
    :return: 文件保存位置
    """
    saved_files_dir = os.getcwd()
    pathname = os.path.join(saved_files_dir, "iCube_Application", "files", file.name)
    try:
        with open(pathname, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return pathname
    except Exception:
        try:
            os.remove(pathname)
        except Exception:
            pass
        return False
