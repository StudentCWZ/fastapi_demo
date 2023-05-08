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
# @Description: routers 封装模块
"""


from fastapi import APIRouter, FastAPI

from app import views
from app.utils import ContextIncludedRoute


def router_v1():
    """v1 版本路由"""
    router = APIRouter(route_class=ContextIncludedRoute)
    router.include_router(views.router, tags=["Article"])
    return router


def init_routers(app: FastAPI):
    """初始化路由"""
    app.include_router(router_v1(), prefix="/api/v1", tags=["v1"])
