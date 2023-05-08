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
# @Description: 类型转换封装模块
"""


# pylint: skip-file


class Dict(dict):
    """自定义字典类"""

    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__


def dict_to_obj(dic):
    """字典转对象"""
    if not isinstance(dic, dict):
        return dic
    d = Dict()
    for key, value in dic.items():
        d[key] = dict_to_obj(value)
    return d
