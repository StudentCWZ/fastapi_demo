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
# @Description: views.article 封装模块
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.libs.dependencies import CommonQueryParams, get_db
from app.schemas.article import ArticleSchema, CreateArticleSchema, UpdateArticleSchema
from app.services.article import ArticleService

router = APIRouter()

_service = ArticleService()


@router.get("/articles")
def get(session: Session = Depends(get_db), commons: CommonQueryParams = Depends()):
    """分页获取文章"""
    return _service.get(session, offset=commons.offset, limit=commons.limit)


@router.get("/articles/{aid}")
def get_by_id(aid: int, session: Session = Depends(get_db)):
    """根据 id 获取文章"""
    return _service.get_by_id(session, aid)


@router.post("/articles", response_model=ArticleSchema)
def create(
    obj_in: CreateArticleSchema,
    session: Session = Depends(get_db),
):
    """添加文章"""
    return _service.create(session, obj_in)


@router.patch("/articles/{aid}", response_model=ArticleSchema)
def patch(aid: int, obj_in: UpdateArticleSchema, session: Session = Depends(get_db)):
    """更新文章"""
    return _service.patch(session, aid, obj_in)


@router.delete("/articles/{aid}")
def delete(aid: int, session: Session = Depends(get_db)):
    """删除文章"""
    return _service.delete(session, aid)
