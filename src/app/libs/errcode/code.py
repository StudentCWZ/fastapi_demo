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
# @Description: 错误码封装模块
"""


from app.libs.constants import BaseEnum


class ErrorCodeEnum(BaseEnum):
    """错误码枚举类"""

    ERROR = (-1, "failed")
    REQUEST_FORMAT_ERROR = (1401, "请求格式错误")
    NODATA_ERR = (1402, "无用户信息")
    AUTHORIZATION_ERR = (1403, "身份认证失败")
    SYSTEM_ERR = (1500, "内部服务错误")
    SEMANTICS_NOT_SUPPORT_ERR = (1250, "语义不支持")
    SEMANTICS_INCOMPLETE_ERR = (1251, "语义完整")
    SOCKET_ERR = (1502, "网络错误")

    @property
    def code(self):
        """获取错误码"""
        return self.value[0]

    @property
    def msg(self):
        """获取错误码码信息"""
        return self.value[1]
