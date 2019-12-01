#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-11-23 03:48:26
# @Author   : 张佳乐
# @Remarks  : 获取相关文章的详细信息
# @File     : article.py
# @Software : PyCharm
# Copyright © 2019 张佳乐. All rights reserved.

from iCube_Application.models import Article


def get_article_information(id):
    json_result = {}  # 待返回的json字符串格式结果
    try:
        article = Article.objects.get(id=id)
        title = article.title
        image = article.image
        article_text = article.article_text
        source = article.source
        article_information = {
            "title": title,
            "image": image,
            "article_text": article_text,
            "source": source
        }
        json_result["statusCode"] = 0  # 状态码：0为成功获取文章信息
        json_result["messageDetail"] = article_information
    except Exception as e:
        print(e)
        json_result["statusCode"] = 505  # 状态码：505为文章id有误
        json_result["messageDetail"] = "请核对文章id"
    return json_result