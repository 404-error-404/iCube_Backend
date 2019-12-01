#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-11-23 03:26:13
# @Author   : 张佳乐
# @Remarks  : 注册新账号
# @File     : new_account_register.py
# @Software : PyCharm
# Copyright © 2019 张佳乐. All rights reserved.
from iCube_Application.models import User


def sin_up_new_user(phone, password, verification_code, user_name):
    """
    新用户注册
    :param phone: 手机号
    :param password: 密码
    :param verification_code: 验证码
    :param user_name: 用户昵称
    :return: json格式数据
    """
    json_result = {
        "url": "/register"
    }  # 待返回的json字符串格式结果
    try:
        new_user = User.objects.get(phone=phone)
        sent_verification_code = new_user.verification_code
        # 检测验证码是否正确
        if verification_code == sent_verification_code:
            if_password = new_user.password  # 如果可以获得密码则说明已注册
            if if_password != "":
                json_result["statusCode"] = 502  # 状态码：502为该账号已注册
                json_result["messageDetail"] = "该账号已注册"
                return json_result
            new_user.password = password
            new_user.user_name = user_name
            new_user.save()
            json_result["statusCode"] = 0  # 状态码：0为注册成功
            json_result["messageDetail"] = "注册成功"
            json_result["url"] = "/login"
        else:
            json_result["statusCode"] = 503  # 状态码：503为验证码错误
            json_result["messageDetail"] = "验证码错误"
    except:
        json_result["statusCode"] = 504  # 状态码：504为未获得验证码
        json_result["messageDetail"] = "您尚未获得验证码，请先获得验证码"
    return json_result
