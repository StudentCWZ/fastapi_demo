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
# @Description: 上下文路径管理封装模块
"""


import contextlib
import os
from os import PathLike
from typing import Union


@contextlib.contextmanager
def chdir(path: Union[str, PathLike]):
    """路径"""
    cwd = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(cwd)
