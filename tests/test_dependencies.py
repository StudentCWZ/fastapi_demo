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
# @Description: dependencies 测试封装模块
"""


import pytest

from app.libs.dependencies import CommonQueryParams


@pytest.mark.parametrize(
    ["args", "expect_value"],
    [
        ((), (0, 10)),
        ((0,), (0, 10)),
        ((-10, -10), (0, 10)),
        ((5, 100), (4, 100)),
    ],
)
def test_common_query_params(args, expect_value):
    """测试"""
    params = CommonQueryParams(*args)
    print(params)
    assert params.offset == expect_value[0]
    assert params.limit == expect_value[1]
