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
# @Description: dao 层测试封装模块
"""


# pylint: skip-file

import pytest

from app.dao.mysql.article import ArticleDao
from app.models.article import Article
from app.schemas.article import CreateArticleSchema, UpdateArticleSchema


class TestArticle:
    """Article Dao 层测试"""

    @pytest.fixture()
    def dao(self, init_article):
        """Dao 层测试"""
        yield ArticleDao()

    def test_get(self, dao, session):
        """get 测试"""
        users = dao.get(session)
        assert len(users) == 3
        users = dao.get(session, limit=2)
        assert len(users) == 2
        users = dao.get(session, offset=4)
        assert not users

    def test_get_by_id(self, dao, session):
        """get_by_id 测试"""
        user = dao.get_by_id(session, 1)
        assert user.id == 1

    def test_create(self, dao, session):
        """create 测试"""
        origin_count = session.query(dao.model).count()
        obj_in = CreateArticleSchema(title="test")
        dao.create(session, obj_in)
        count = session.query(dao.model).count()
        assert origin_count + 1 == count

    def test_patch(self, dao, session):
        """patch 测试"""
        obj: Article = session.query(dao.model).first()
        body = obj.body
        obj_in = UpdateArticleSchema(body="test")
        updated_obj: Article = dao.patch(session, obj.id, obj_in)
        assert body != updated_obj.body

    def test_delete(self, dao, session):
        """delete 测试"""
        origin_count = session.query(dao.model).count()
        dao.delete(session, 1)
        count = session.query(dao.model).count()
        assert origin_count - 1 == count

    def test_count(self, dao, session):
        """count 测试"""
        count = dao.count(session)
        assert count == 3
