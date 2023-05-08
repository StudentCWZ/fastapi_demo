#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Version:  Python 3.11.2
# @Software: Sublime Text 4
# @Author:   StudentCWZ
# @Email:    StudentCWZ@outlook.com
# @Date:     2023-03-09 08:57:20
# @Last Modified by: StudentCWZ
# @Last Modified time: 2023-03-09 08:58:26
# @Description: 异常封装模块
"""


from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from .exception_handler import (
    business_exception_handler,
    global_exception_handler,
    validation_exception_handler,
)
from .global_exception import BusinessException


def create_global_exception_handler(app: FastAPI):
    """创建全局异常处理器"""
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(BusinessException, business_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)
