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
# @Description: views 测试封装模块
"""


# pylint: skip-file

import pytest
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response

from app.models.article import Article
from app.schemas.article import ModelSchema


def test_docs(client):
    """Test view"""
    response = client.get("/docs")
    assert response.status_code == 200


class BaseTest:
    version = "v1"
    base_url: str
    model: ModelSchema

    @pytest.fixture()
    def init_data(self):
        pass

    def url(self, pk: int = None) -> str:
        url_split = ["api", self.version, self.base_url]
        if pk:
            url_split.append(str(pk))
        return "/".join(url_split)

    @staticmethod
    def assert_response_ok(response: Response):
        assert response.status_code == 200

    def test_get(self, client, session, init_data):
        count = session.query(self.model).count()
        response = client.get(self.url())
        self.assert_response_ok(response)
        assert count == len(response.json())

    def test_get_by_id(self, client, session, init_data):
        obj = session.query(self.model).first()
        response = client.get(self.url(obj.id))
        self.assert_response_ok(response)
        assert jsonable_encoder(obj) == response.json()

    def test_delete(self, client, session, init_data):
        count = session.query(self.model).count()
        session.close()
        response = client.delete(self.url(1))
        self.assert_response_ok(response)
        after_count = session.query(self.model).count()
        assert after_count == 2
        assert count - 1 == after_count


class TestArticle(BaseTest):
    model = Article
    base_url = "articles"

    @pytest.fixture()
    def init_data(self, init_article):
        pass

    def test_create(self, client, session, init_data):
        response = client.post(self.url(), json={"title": "xxx"})
        self.assert_response_ok(response)
        assert response.json().get("title") == "xxx"

    def test_patch(self, client, session, init_data):
        obj = session.query(Article).first()
        response = client.patch(self.url(obj.id), json={"body": "xxx"})
        self.assert_response_ok(response)
        assert response.json().get("body") != obj.body
