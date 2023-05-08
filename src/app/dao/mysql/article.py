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
# @Description: article 封装模块
"""


# pylint: skip-file

from typing import Generic, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.models.article import Article
from app.schemas.article import (
    CreateArticleSchema,
    CreateSchema,
    ModelSchema,
    UpdateArticleSchema,
    UpdateSchema,
)


class BaseDao(Generic[ModelSchema, CreateSchema, UpdateSchema]):
    """Dao 基本数据库操作"""

    model: ModelSchema

    def get(self, session: Session, offset=0, limit=10) -> List[ModelSchema]:
        """分页查询操作"""
        result = session.query(self.model).offset(offset).limit(limit).all()
        return result

    def get_by_id(self, session: Session, primary_key: int) -> ModelSchema:
        """基于主键查询"""
        return session.query(self.model).get(primary_key)

    def create(self, session: Session, obj_in: CreateSchema) -> ModelSchema:
        """Create"""
        obj = self.model(**jsonable_encoder(obj_in))
        session.add(obj)
        session.commit()
        return obj

    def patch(
        self, session: Session, primary_key: int, obj_in: UpdateSchema
    ) -> ModelSchema:
        """Patch"""
        obj = self.get_by_id(session, primary_key)
        update_data = obj_in.dict(exclude_unset=True)
        for key, val in update_data.items():
            setattr(obj, key, val)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

    def delete(self, session: Session, primary_key: int) -> None:
        """Delete"""
        obj = self.get_by_id(session, primary_key)
        session.delete(obj)
        session.commit()

    def count(self, session: Session):
        """计数"""
        return session.query(self.model).count()


class ArticleDao(BaseDao[Article, CreateArticleSchema, UpdateArticleSchema]):
    """文章 Dao 层"""

    model = Article
