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
# @Description: redis 初始化封装模块
"""


from typing import Any

from redis import asyncio as aioredis

from app.config import settings


async def init_redis() -> Any:
    """初始化 redis 连接"""
    redis = await aioredis.from_url(
        url=f"redis://{settings.Redis.Host}",
        port=int(f"{settings.Redis.port}"),
        username=f"{settings.Redis.username}",
        password=f"{settings.Redis.password}",
        db=int(f"{settings.Redis.DB}"),
        encoding=f"{settings.Redis.Encoding}",
        decode_responses=True,
    )
    return redis
