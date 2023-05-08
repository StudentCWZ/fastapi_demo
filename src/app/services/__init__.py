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
# @Description: services 层封装模块
"""


from typing import Generic, List

from sqlalchemy.orm import Session

from app.dao.mysql.article import BaseDao
from app.schemas.article import CreateSchema, ModelSchema, UpdateSchema


class BaseService(Generic[ModelSchema, CreateSchema, UpdateSchema]):
    """基础 services 层"""

    dao: BaseDao

    def get(self, session: Session, offset=0, limit=10) -> List[ModelSchema]:
        """get 操作"""
        return self.dao.get(session, offset=offset, limit=limit)

    def total(self, session: Session) -> int:
        """获取总数"""
        return self.dao.count(session)

    def get_by_id(self, session: Session, primary_key: int) -> ModelSchema:
        """Get by id"""
        return self.dao.get_by_id(session, primary_key)

    def create(self, session: Session, obj_in: CreateSchema) -> ModelSchema:
        """Create a object"""
        return self.dao.create(session, obj_in)

    def patch(
        self, session: Session, primary_key: int, obj_in: UpdateSchema
    ) -> ModelSchema:
        """Update"""
        return self.dao.patch(session, primary_key, obj_in)

    def delete(self, session: Session, primary_key: int) -> None:
        """Delete a object"""
        return self.dao.delete(session, primary_key)
