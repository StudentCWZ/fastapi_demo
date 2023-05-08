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
# @Description: 数据库初始化封块
"""


from sqlalchemy.engine import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker

from app.config import settings

url = URL(
    drivername=settings.Database.Driver,
    username=settings.Database.get("Username", None),
    password=settings.Database.get("Password", None),
    host=settings.Database.get("Host", None),
    port=settings.Database.get("Port", None),
    database=settings.Database.get("Name", None),
    query=settings.Database.get("Query", None),
)
engine: Engine = create_engine(url, echo=False)


SessionFactory = sessionmaker(bind=engine, autocommit=False, autoflush=True)

ScopedSession = scoped_session(SessionFactory)
