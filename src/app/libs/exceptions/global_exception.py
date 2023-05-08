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
# @Description: 全局异常类封装模块
"""


from app.libs.errcode import ErrorCodeEnum


class BusinessException(Exception):
    """业务异常类"""

    def __init__(self, code: int = None, msg: str = None):
        """
        业务异常初始化
        :param code: 错误码
        :param msg: 错误信息
        """
        self.code = code
        self.msg = msg

    def exc_data(self, error_enum: ErrorCodeEnum):
        """
        设置异常信息
        :param error_enum: 错误信息枚举
        :return:
        """
        self.code = error_enum.code
        self.msg = error_enum.msg
        return self
