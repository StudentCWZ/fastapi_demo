#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Version:  Python 3.8.10
# @Software: Sublime Text 4
# @Author:   StudentCWZ
# @Email:    StudentCWZ@outlook.com
# @Date:     2023-03-09 08:50:57
# @Last Modified by: StudentCWZ
# @Last Modified time: 2023-03-09 15:11:31
# @Description: 异常处理函数
"""

# pylint: skip-file

import traceback

from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from loguru import logger

from app.libs.errcode import ErrorCodeEnum
from app.libs.logger import default_logger
from app.libs.responses import fail_response

from .global_exception import BusinessException


async def business_exception_handler(request: Request, exc: BusinessException):
    """全局业务异常处理"""
    data = default_logger(request, status_code=400)
    data["response"].update(code=exc.code, msg=exc.msg)
    logger.bind(data=data).error("Http 请求异常")
    return fail_response(status_code=400, code=exc.code, msg=exc.msg)


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """全局捕捉参数验证异常"""
    data = default_logger(request, status_code=400)
    msg = ".".join(
        [
            f'{".".join(map(lambda x: str(x), error.get("loc")))}:{error.get("msg")};'
            for error in exc.errors()
        ]
    )
    error = ErrorCodeEnum.REQUEST_FORMAT_ERROR
    data["response"].update(code=error.code, msg=msg)
    logger.bind(data=data).error("参数验证异常")
    return fail_response(status_code=400, code=error.code, msg=msg)


async def connection_exception_handler(request: Request, exc: ConnectionError):
    data = default_logger(request, status_code=502)
    msg = f"网络异常, {exc.__repr__()}:{traceback.format_exc()}"
    error = ErrorCodeEnum.SOCKET_ERR
    data["response"].update(code=error.code, msg=msg)
    logger.bind(data=data).error("网络异常")
    return fail_response(status_code=502, code=error.code, msg=msg)


async def global_exception_handler(request: Request, exc: Exception):
    """全局系统异常处理器"""
    msg = f"系统异常, {traceback.format_exc()}"
    error = ErrorCodeEnum.SYSTEM_ERR
    data = default_logger(request, status_code=500)
    data["response"].update(code=error.code, msg=msg)
    logger.bind(data=data).error("全局系统异常")
    return fail_response(status_code=500, code=error.code, msg=msg)
