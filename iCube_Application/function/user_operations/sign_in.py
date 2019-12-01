#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-11-23 15:32:59
# @Author   : 张佳乐
# @Remarks  : 登录
# @File     : sign_in.py
# @Software : PyCharm
# Copyright © 2019 张佳乐. All rights reserved.
from iCube_Application.models import User


def user_sign_in(phone, password):
    """
    用户登录函数
    :param phone: 手机号
    :param password: 密码
    :return: 返回手机号和用户昵称
    """
    json_result = {
        "url": "/login"
    }  # 待返回的json字符串格式结果
    try:
        user = User.objects.get(phone=phone)
        user_password = user.password
        # 无密码则说明已发送验证码但未注册
        if user_password == "":
            json_result["statusCode"] = 507  # 状态码：507为该账号未注册
            json_result["messageDetail"] = "该账号未注册，请先注册"
        # 检测密码是否正确
        elif user_password == password:
            user_name = user.user_name
            user_information = {
                "user_name": user_name,
                "user_phone": phone
            }
            json_result["statusCode"] = 0  # 状态码：0为登录成功
            json_result["messageDetail"] = user_information
            json_result["url"] = "/"
        else:
            json_result["statusCode"] = 506  # 状态码：506为密码错误
            json_result["messageDetail"] = "密码错误"
    except:
        json_result["statusCode"] = 507  # 状态码：507为该账号未注册
        json_result["messageDetail"] = "该账号未注册，请先注册"
    return json_result
