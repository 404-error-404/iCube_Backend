#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-11-23 02:40:44
# @Author   : 张佳乐
# @Remarks  : 获取验证码函数
# @File     : get_verification_code.py
# @Software : PyCharm
# Copyright © 2019 张佳乐. All rights reserved.

import json
import random

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

from iCube_Application.models import User


def create_verification_code():
    """
    生成4位验证码
    :return: 4位验证码
    """
    verification_code = ""
    for i in range(4):
        random_num = random.randint(0, 9)  # 随机生成0-9的数字
        verification_code += str(random_num)
    return verification_code


def write_into_database(phone, code):
    try:
        new_user = User.objects.get(phone=phone)
        new_user.verification_code = code
        new_user.save()
    except:
        new_user = User(phone=phone, verification_code=code)
        new_user.save()



def aliyun_verification_code(phone):
    """
    调用阿里云接口发送验证码
    :param phone: 用于接收验证码的手机号
    :param code: 验证码
    :return: 成功发送则返回True，失败返回False
    """
    # 先生成验证码并保存
    code = create_verification_code()
    write_into_database(phone, code)
    # TODO 删除隐私信息
    # 接下来发送短信
    client = AcsClient('就不告诉你', '就不告诉你', 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https') # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendBatchSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumberJson', '["{}"]'.format(phone))
    request.add_query_param('SignNameJson', "[\"iCube\"]")
    request.add_query_param('TemplateCode', "SMS_177539454")
    request.add_query_param('TemplateParamJson', "[{\"code\":\"%s\"}]"%code)

    response = client.do_action(request)
    response_json = json.loads(response)
    json_result = {}  # 待返回的json字符串格式结果
    if response_json["Message"] == "OK":
        json_result["statusCode"] = 0  # 状态码：0为验证码发送成功
        json_result["messageDetail"] = "验证码发送成功"
    else:
        json_result["statusCode"] = 501  # 状态码：501为验证码发送失败，请检查阿里云账户是否欠费
        json_result["messageDetail"] = "验证码发送失败，请检查阿里云账户是否欠费"
    return json_result
