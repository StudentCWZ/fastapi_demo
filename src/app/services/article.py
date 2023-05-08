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
# @Description: services.article 层封装模块
"""


from app.dao.mysql.article import ArticleDao
from app.models.article import Article
from app.schemas.article import CreateSchema, UpdateSchema
from app.services import BaseService


class ArticleService(BaseService[Article, CreateSchema, UpdateSchema]):
    """文章 services 层"""

    dao = ArticleDao()
