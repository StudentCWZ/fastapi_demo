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
# @Description: dependencies 封装模块
"""


from typing import Any

from elasticsearch import AsyncElasticsearch
from fastapi import Request
from sqlalchemy.orm import Session


def get_db(request: Request) -> Session:
    """获取 db"""
    return request.state.db


def get_redis(request: Request) -> Any:
    """获取 redis"""
    return request.state.redis


def get_es(request: Request) -> AsyncElasticsearch:
    """获取 es"""
    return request.state.es


class CommonQueryParams:
    """分页查询参数"""

    def __init__(self, offset: int = 1, limit: int = 10):
        self.offset = offset - 1
        self.offset = max(self.offset, 0)
        self.limit = limit

        if self.limit < 0:
            self.limit = 10

    def __repr__(self):
        return f"<{self.__class__}: {self.__dict__}>"

    def __str__(self):
        return self.__repr__()
