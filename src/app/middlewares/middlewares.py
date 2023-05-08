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
# @Description: 中间件封装模块
"""


import time
from typing import Callable

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from app.dao.elastic import init_es
from app.dao.mysql.db import SessionFactory
from app.dao.redis import init_redis


async def db_session_middleware(request: Request, call_next: Callable) -> Response:
    """db 中间件"""
    response = Response("Internal services error", status_code=500)
    try:
        request.state.db = SessionFactory()
        response = await call_next(request)
    finally:
        request.state.db.close()

    return response


async def redis_session_middleware(request: Request, call_next: Callable) -> Response:
    """redis 中间件"""
    response = Response("Internal services error", status_code=500)
    try:
        request.state.redis = await init_redis()
        response = await call_next(request)
    finally:
        await request.state.redis.close()
    return response


async def es_session_middleware(request: Request, call_next: Callable) -> Response:
    """es 中间件"""
    response = Response("Internal services error", status_code=500)
    try:
        request.state.es = await init_es()
        response = await call_next(request)
    finally:
        await request.state.es.close()
    return response


async def prevent_crawler_middleware(request: Request, call_next: Callable) -> Response:
    """预防爬虫中间件"""
    permission_list = ["PostmanRuntime", "Python"]
    headers = request.headers
    if headers.get("user-agent") in permission_list:
        return Response("Bad Gateway", status_code=502)
    response = await call_next(request)
    return response


async def add_process_time_middleware(
    request: Request, call_next: Callable
) -> Response:
    """请求时间中间件"""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


def init_middleware(app: FastAPI) -> None:
    """注册中间件"""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.middleware("http")(prevent_crawler_middleware)
    app.middleware("http")(add_process_time_middleware)
    app.middleware("http")(redis_session_middleware)
    app.middleware("http")(db_session_middleware)
    app.middleware("http")(es_session_middleware)
