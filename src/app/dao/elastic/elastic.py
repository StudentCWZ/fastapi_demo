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
# @Description: ES 初始化封装模块
"""

# from functools import lru_cache  # 一个缓存装饰器， 在网上找寻的方法

import elasticsearch
from elasticsearch import AsyncElasticsearch

from app.config import settings


async def init_es() -> elasticsearch.AsyncElasticsearch:
    """初始化连接 es"""
    cnf: dict = {
        "hosts": settings.ElasticSearch.Hosts,
        "http_auth": (settings.ElasticSearch.Username, settings.ElasticSearch.Password),
        "timeout": 3600,
        # 上传之前记得取消下面参数注释
        # "use_ssl": True,
        # "verify_certs": True,
        # "ca_certs": settings.ElasticSearch.Cert
    }
    return AsyncElasticsearch(**cnf)
