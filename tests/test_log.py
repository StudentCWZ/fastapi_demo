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
# @Description: log 测试封装模块
"""


import pytest

from app.libs.logger import LoggerBase


@pytest.mark.parametrize(
    ["debug", "level", "expect_value"],
    [
        (True, "", "DEBUG"),
        (True, "INFO", "DEBUG"),
        (False, "DEBUG", "DEBUG"),
        (False, "INFO", "INFO"),
    ],
)
def test_log_level(debug: bool, level: str, expect_value):
    """Test log level"""
    log_level_name = LoggerBase().update_log_level(debug, level)
    assert log_level_name == expect_value
