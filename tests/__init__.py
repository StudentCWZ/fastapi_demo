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
# @Description: tests 封装模块
"""


import os

from app.config import settings

settings.load_file(os.path.join(os.path.dirname(__file__), "settings.yml"))
settings.load_file(os.path.join(os.path.dirname(__file__), "settings.local.yml"))
