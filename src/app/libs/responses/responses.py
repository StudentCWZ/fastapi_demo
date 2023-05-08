#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Version:  Python 3.8.10
# @Software: Sublime Text 4
# @Author:   StudentCWZ
# @Email:    StudentCWZ@outlook.com
# @Date:     2023-03-09 08:57:20
# @Last Modified by: StudentCWZ
# @Last Modified time: 2023-03-09 08:58:26
# @Description: 服务返回结果封装模块
"""

from typing import Union

from fastapi import status
from fastapi.responses import JSONResponse, Response


def success_response(data: Union[list, dict, str]) -> Response:
    """正确返回"""
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": 200,
            "msg": "Success",
            "data": data,
        },
    )


def fail_response(status_code: int, code: int, msg: str, data: dict = None) -> Response:
    """错误返回"""
    return JSONResponse(
        status_code=status_code,
        content={
            "code": code,
            "msg": msg,
            "data": data,
        },
    )
