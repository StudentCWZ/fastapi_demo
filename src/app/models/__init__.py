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
# @Description: models 层封装模块
"""


from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base, declared_attr


class CustomBase:
    """https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html"""

    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {"mysql_engine": "InnoDB", "mysql_collate": "utf8mb4_general_ci"}

    id = Column(Integer, primary_key=True, autoincrement=True)

    def to_dict(self):
        """数据模型对象转字典"""
        data_dict = {}
        base_dict = self.__dict__
        for key, value in base_dict.items():
            if str(key).startswith("_"):
                # 前缀带下划线不要
                continue
            data_dict[key] = value
        return data_dict


BaseModel = declarative_base(cls=CustomBase)
