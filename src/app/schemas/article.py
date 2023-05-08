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
# @Description: schemas 封装模块
"""


# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from datetime import datetime
from typing import Optional, TypeVar

from pydantic import BaseModel, constr

from app.models import BaseModel as DBModel

ModelSchema = TypeVar("ModelSchema", bound=DBModel)
CreateSchema = TypeVar("CreateSchema", bound=BaseModel)
UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)


class InDBMixin(BaseModel):
    """DB 相关类"""

    id: int

    def __repr__(self):
        return f"<{self.__class__}: {self.__dict__}>"

    def __str__(self):
        return self.__repr__()

    class Config:
        """配置"""

        orm_mode = True

        def __repr__(self):
            return f"<{self.__class__}: {self.__dict__}>"

        def __str__(self):
            return self.__repr__()


class BaseArticle(BaseModel):
    """文章基本字段"""

    title: constr(max_length=500)
    body: Optional[str] = None

    def __repr__(self):
        return f"<{self.__class__}: {self.__dict__}>"

    def __str__(self):
        return self.__repr__()


class ArticleSchema(BaseArticle, InDBMixin):
    """时间字段"""

    create_time: datetime
    update_time: datetime

    def __repr__(self):
        return f"<{self.__class__}: {self.__dict__}>"

    def __str__(self):
        return self.__repr__()


class CreateArticleSchema(BaseArticle):
    """创建文章字段"""

    def __repr__(self):
        return f"<{self.__class__}: {self.__dict__}>"

    def __str__(self):
        return self.__repr__()


class UpdateArticleSchema(BaseArticle):
    """更新文章字段"""

    title: Optional[constr(max_length=500)] = None

    def __repr__(self):
        return f"<{self.__class__}: {self.__dict__}>"

    def __str__(self):
        return self.__repr__()
