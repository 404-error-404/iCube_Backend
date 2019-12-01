import json

from django.http import HttpResponse

# Create your views here.
from iCube_Application.function.File_operation.md5_encode import get_md5_encode
from iCube_Application.function.File_operation.save_file import save_file
from iCube_Application.function.ImageIdentification.BaiDu_image import \
    BaiDu_image_recognize
from iCube_Application.function.File_operation.upload_to_oss import \
    upload_to_oss_and_get_url
from iCube_Application.function.ImageIdentification.Face_recognize import \
    face_age_score
from iCube_Application.function.VerificationCode.get_verification_code import \
    aliyun_verification_code
from iCube_Application.function.article.article import get_article_information
from iCube_Application.function.change_image_style.change_image_style import \
    image_style_changed
from iCube_Application.function.user_operations.new_account_register \
    import sin_up_new_user
from iCube_Application.function.user_operations.sign_in import user_sign_in


def verification_code(request):
    """
    请求获取验证码
    :param request: django默认参数
    :return: 以HTTP返回值的形式返回json格式数据
    """
    json_result = {}  # 待返回的json字符串格式结果
    print(str(request))
    if request.method == 'POST':  # 当提交表单时
        # 判断是否传参
        if request.POST:
            phone = request.POST.get('phone', False)
            print(request.POST)
            # 判断参数中是否含有接受者邮箱
            if phone:
                # 函数相关操作
                json_result = aliyun_verification_code(phone)
            else:
                json_result["statusCode"] = 404  # 状态码：404为缺少参数
                json_result["messageDetail"] = "错误，缺少参数"
        else:
            json_result["statusCode"] = 403  # 状态码：403为没有参数
            json_result["messageDetail"] = "错误，没有参数"
    else:
        json_result["statusCode"] = 405  # 状态码：405为请求方法错误
        json_result["messageDetail"] = "请求方法错误"
    json_result = json.dumps(json_result, ensure_ascii=False)
    return HttpResponse(json_result)


def sign_up(request):
    """
    注册
    :param request: django默认参数
    :return: 以HTTP返回值的形式返回json格式数据
    """
    json_result = {
        "url": "/register"
    }  # 待返回的json字符串格式结果
    if request.method == 'POST':  # 当提交表单时
        # 判断是否传参
        if request.POST:
            phone = request.POST.get('phone', False)
            password = request.POST.get('password', False)
            user_verification_code = request.POST.get('verification_code',
                                                      False)
            user_name = request.POST.get('user_name', False)
            # 判断参数中是否含有接受者邮箱
            if phone and password and user_verification_code and user_name:
                # 函数相关操作
                json_result = sin_up_new_user(
                    phone, password, user_verification_code, user_name
                )
            else:
                json_result["statusCode"] = 404  # 状态码：404为缺少参数
                json_result["messageDetail"] = "错误，缺少参数"
        else:
            json_result["statusCode"] = 403  # 状态码：403为没有参数
            json_result["messageDetail"] = "错误，没有参数"
    else:
        json_result["statusCode"] = 405  # 状态码：405为请求方法错误
        json_result["messageDetail"] = "请求方法错误"
    json_result = json.dumps(json_result, ensure_ascii=False)
    return HttpResponse(json_result)


def sign_in(request):
    """
    登录
    :param request: django默认参数
    :return: 以HTTP返回值的形式返回json格式数据
    """
    json_result = {
        "url": "/login"
    }  # 待返回的json字符串格式结果
    if request.method == 'POST':  # 当提交表单时
        # 判断是否传参
        if request.POST:
            phone = request.POST.get('phone', False)
            password = request.POST.get('password', False)
            # 判断参数中是否含有接受者邮箱
            if phone and password:
                # 函数相关操作
                json_result = user_sign_in(phone, password)
            else:
                json_result["statusCode"] = 404  # 状态码：404为缺少参数
                json_result["messageDetail"] = "错误，缺少参数"
        else:
            json_result["statusCode"] = 403  # 状态码：403为没有参数
            json_result["messageDetail"] = "错误，没有参数"
    else:
        json_result["statusCode"] = 405  # 状态码：405为请求方法错误
        json_result["messageDetail"] = "请求方法错误"
    json_result = json.dumps(json_result, ensure_ascii=False)
    return HttpResponse(json_result)


def get_article(request):
    """
    获取相关文章函数
    :param request: django默认参数
    :return: 以HTTP返回值的形式返回json格式数据
    """
    json_result = {}  # 待返回的json字符串格式结果
    if request.method == 'POST':  # 当提交表单时
        # 判断是否传参
        if request.POST:
            stu = request.POST.get('stu', False)
            # 判断参数中是否含有文章id
            if stu:
                # 函数相关操作
                json_result = get_article_information(stu)
            else:
                json_result["statusCode"] = 404  # 状态码：404为缺少参数
                json_result["messageDetail"] = "错误，缺少参数"
        else:
            json_result["statusCode"] = 403  # 状态码：403为没有参数
            json_result["messageDetail"] = "错误，没有参数"
    else:
        json_result["statusCode"] = 405  # 状态码：405为请求方法错误
        json_result["messageDetail"] = "请求方法错误"
    json_result = json.dumps(json_result, ensure_ascii=False)
    return HttpResponse(json_result)


def image_recognize(request):
    """
    图像分析，从前端获取图片然后返回分析结果
    :param request: django默认参数
    :return: 以HTTP返回值的形式返回json格式数据
    """
    json_result = {}  # 待返回的json字符串格式结果
    if request.method == 'POST':  # 当提交表单时
        # 判断是否传参
        if request.FILES and request.POST:
            file = request.FILES.get("filename", False)
            recognize_type = request.POST.get("recognize_type", False)

            # 判断参数中是否含有待上传的文件
            if file and recognize_type:
                # 函数相关操作
                file_path = save_file(file)
                file_url = upload_to_oss_and_get_url(file_path, file.name)
                if file_path:
                    try:
                        recognize_type = int(recognize_type)
                    except Exception:
                        recognize_type = 1
                    result = BaiDu_image_recognize(file_path, recognize_type)
                    json_result["statusCode"] = 0
                    json_result["messageDetail"] = {
                        "file_url": file_url,
                        "image_detial": result
                    }
                else:
                    json_result["statusCode"] = 508
                    json_result["messageDetail"] = "文件上传失败"
            else:
                json_result["statusCode"] = 404  # 状态码：404为缺少参数, 这里没有选择文件
                json_result["messageDetail"] = "请选择文件"
        else:
            json_result["statusCode"] = 403  # 状态码：403为没有参数
            json_result["messageDetail"] = "错误，没有参数"
    else:
        json_result["statusCode"] = 405  # 状态码：405为请求方法错误
        json_result["messageDetail"] = "请求方法错误"
    json_result = json.dumps(json_result, ensure_ascii=False)
    return HttpResponse(json_result)


def face_recognize(request):
    """
    人脸分析，从前端获取图片然后返回分析人脸年龄和颜值打分
    :param request: django默认参数
    :return: 以HTTP返回值的形式返回json格式数据
    """
    json_result = {}  # 待返回的json字符串格式结果
    if request.method == 'POST':  # 当提交表单时
        # 判断是否传参
        if request.FILES:
            file = request.FILES.get("filename", False)
            # 判断参数中是否含有待上传的文件
            if file:
                # 函数相关操作
                file_path = save_file(file)
                file_url = upload_to_oss_and_get_url(file_path, file.name)
                if file_path:
                    # 获取人脸年龄和分数
                    result = face_age_score(file_url)
                    if result == "未识别到人脸":
                        json_result["statusCode"] = 509
                    else:
                        json_result["statusCode"] = 0
                    json_result["messageDetail"] = {
                        "file_url": file_url,
                        "image_detail": result
                    }
                else:
                    json_result["statusCode"] = 508
                    json_result["messageDetail"] = "文件上传失败"
            else:
                json_result["statusCode"] = 404  # 状态码：404为缺少参数, 这里没有选择文件
                json_result["messageDetail"] = "请选择文件"
        else:
            json_result["statusCode"] = 403  # 状态码：403为没有参数
            json_result["messageDetail"] = "错误，没有参数"
    else:
        json_result["statusCode"] = 405  # 状态码：405为请求方法错误
        json_result["messageDetail"] = "请求方法错误"
    json_result = json.dumps(json_result, ensure_ascii=False)
    return HttpResponse(json_result)


def upload_image(request):
    """
    上传图片返回阿里云对象服务器oss网址
    :param request: django默认参数
    :return: 以HTTP返回值的形式返回json格式数据
    """
    json_result = {}  # 待返回的json字符串格式结果
    if request.method == 'POST':  # 当提交表单时
        # 判断是否传参
        if request.FILES:
            image = request.FILES.get("image", False)
            # 判断参数中是否含有待上传的文件
            if image:
                # 函数相关操作
                # 先保存图片
                image_path = save_file(image)
                # 获取图片md5值
                md5_image = get_md5_encode(image_path)
                # 再获取两个图片的阿里云对象服务器URL
                image_url = upload_to_oss_and_get_url(
                    image_path,
                    str(md5_image) + ".jpg"
                )
                # 成功获取则继续进行
                if image_url:
                    json_result["statusCode"] = 0
                    json_result["messageDetail"] = {
                        "image_url": image_url
                    }
                else:
                    json_result["statusCode"] = 508
                    json_result["messageDetail"] = "文件上传失败"
            else:
                json_result["statusCode"] = 404  # 状态码：404为缺少参数, 这里没有选择文件
                json_result["messageDetail"] = "请选择文件"
        else:
            json_result["statusCode"] = 403  # 状态码：403为没有参数
            json_result["messageDetail"] = "错误，没有参数"
    else:
        json_result["statusCode"] = 405  # 状态码：405为请求方法错误
        json_result["messageDetail"] = "请求方法错误"
    json_result = json.dumps(json_result, ensure_ascii=False)
    return HttpResponse(json_result)


def image_change_style(request):
    """
    图像风格转换
    :param request: django默认参数
    :return: 以HTTP返回值的形式返回json格式数据
    """
    json_result = {}  # 待返回的json字符串格式结果
    if request.method == 'POST':  # 当提交表单时
        # 判断是否传参
        if request.POST:
            content_image = request.POST.get("content_image", False)
            style_image = request.POST.get("style_image", False)
            # 判断参数中是否含有待上传的文件
            if content_image and style_image:
                # 函数相关操作
                json_result = image_style_changed(content_image, style_image)

            else:
                json_result["statusCode"] = 404  # 状态码：404为缺少参数, 这里没有选择文件
                json_result["messageDetail"] = "请选择文件"
        else:
            json_result["statusCode"] = 403  # 状态码：403为没有参数
            json_result["messageDetail"] = "错误，没有参数"
    else:
        json_result["statusCode"] = 405  # 状态码：405为请求方法错误
        json_result["messageDetail"] = "请求方法错误"
    json_result = json.dumps(json_result, ensure_ascii=False)
    return HttpResponse(json_result)


def post_demo(request):
    """
    POST请求函数模板
    :param request: django默认参数
    :return: 以HTTP返回值的形式返回json格式数据
    """
    json_result = {}  # 待返回的json字符串格式结果
    if request.method == 'POST':  # 当提交表单时
        # 判断是否传参
        if request.POST:
            id1 = request.POST.get('id1', False)
            # 判断参数中是否含有接受者邮箱
            if id1:
                # 函数相关操作
                pass
            else:
                json_result["statusCode"] = 404  # 状态码：404为缺少参数
                json_result["messageDetail"] = "错误，缺少参数"
        else:
            json_result["statusCode"] = 403  # 状态码：403为没有参数
            json_result["messageDetail"] = "错误，没有参数"
    else:
        json_result["statusCode"] = 405  # 状态码：405为请求方法错误
        json_result["messageDetail"] = "请求方法错误"
    json_result = json.dumps(json_result, ensure_ascii=False)
    return HttpResponse(json_result)
