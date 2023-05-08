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
# @Description: 服务启动封装模块
"""


import uvicorn
from fastapi import FastAPI
from loguru import logger

from app import middlewares, routers
from app.config import settings
from app.libs import exceptions
from app.libs.logger import LoggerBase


class Server:
    """服务启动类"""

    def __init__(self):
        LoggerBase().__call__()
        self.app = FastAPI()

    def init_app(self):
        """初始化 app"""
        middlewares.init_middleware(self.app)
        routers.init_routers(self.app)
        exceptions.create_global_exception_handler(self.app)

    def run(self):
        """启动服务"""
        self.init_app()
        logger.info("Server start ...")
        uvicorn.run(
            app=self.app,
            host=settings.Server.Host,
            port=settings.Server.Port,
        )
