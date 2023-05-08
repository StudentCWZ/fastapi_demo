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
# @Description: 自定义路由封装模块
"""


# pylint: skip-file

import json
import uuid
from typing import Callable

from fastapi import Request, Response
from fastapi.routing import APIRoute
from loguru import logger


async def get_form(request: Request):
    """获取请求体表单"""
    form = ""
    try:
        form = await request.form()
    except Exception as e:
        logger.debug(f"请求表单没有数据：{e}")
    return form


async def get_body(request: Request):
    """获取请求体"""
    body = ""
    # 获取请求体
    try:
        body_bytes = await request.body()
        if body_bytes:
            try:
                body = await request.json()
            except Exception as e:
                logger.debug(f"无法获取请求体 Json 格式数据：{e}")
                if body_bytes:
                    try:
                        body = body_bytes.decode("utf-8")
                    except Exception as e:
                        logger.debug(f"无法获取请求体 UTF-8 格式编码数据：{e}")
                        body = body_bytes.decode("gb2312")
    except Exception as e:
        print(f"无法获取请求体任何格式数据：{e}")
    return body


class ContextIncludedRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            # 生成 request_id
            request_id = str(uuid.uuid4())
            # Add context to all loggers in all views
            with logger.contextualize(request_id=request_id):
                # 获取 form
                form = await get_form(request)
                if not form:
                    # 获取 body
                    body = await get_body(request)
                    try:
                        body = json.loads(body)
                    except Exception as e:
                        logger.debug(f"无法将 body 转为字典: {e}")
                        body = {}
                else:
                    body = {}
                request.scope.setdefault("request_id", request_id)
                request.scope.setdefault("request_form", form)
                request.scope.setdefault("request_body", body)
                response: Response = await original_route_handler(request)
                dic = {
                    "http": {
                        "ip": dict(request.headers).get("x-real-ip", "")
                        or request.client.host,
                        "uri": request.url.path,
                        "user_agent": dict(request.headers).get("user-agent", ""),
                        "method": request.method,
                        "status_code": response.status_code,
                    },
                    "request": {"body": body, "form": dict(form) if form else {}},
                    "response": {
                        "request_id": request_id,
                    },
                }
                # 由于返回的 data 过长，则忽略
                tmp = json.loads(response.body.decode())
                tmp["data"] = {}
                dic["response"].update(**tmp)
                logger.bind(data=dic).success("成功返回")
            return response

        return custom_route_handler
