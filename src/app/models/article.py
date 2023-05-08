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


from datetime import datetime

from sqlalchemy import Column, DateTime, String, Text

from app.models import BaseModel


class Article(BaseModel):
    """Article table"""

    title = Column(String(500))
    body = Column(Text(), nullable=True)
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    update_time = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )

    def __repr__(self):
        return f"<{self.__class__}: {self.__dict__}>"

    def to_dict(self) -> dict:
        """数据模型转字典"""
        dic = super().to_dict()
        return dic
