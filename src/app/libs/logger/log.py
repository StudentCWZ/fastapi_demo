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
# @Description: 日志封装模块
"""


# pylint: skip-file

import json
import logging
import os
import sys
import threading
from pathlib import Path

from fastapi.requests import Request
from loguru import logger

from app.config import settings


def default_logger(request: Request, status_code=200) -> dict:
    dic = {
        "http": {
            "ip": dict(request.headers).get("x-real-ip", "") or request.client.host,
            "uri": request.url.path,
            "user_agent": dict(request.headers).get("user-agent", ""),
            "method": request.method,
            "status_code": status_code,
        },
        "request": {
            "body": request.scope.get("request_body", {}),
            "form": request.scope.get("request_form", {}),
        },
        "response": {
            "request_id": request.scope.get("request_id", ""),
        },
    }
    return dic


class LoggerBase:
    """日志基本类"""

    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(LoggerBase, "_instance"):
            with LoggerBase._instance_lock:
                if not hasattr(LoggerBase, "_instance"):
                    LoggerBase._instance = object.__new__(cls)
        return LoggerBase._instance

    def __init__(self):
        self._base_dir = os.path.join(
            Path(__file__).parent.parent.parent.parent.parent, settings.Logger.Path
        )
        self._mkdirs(self._base_dir)

    @staticmethod
    def _mkdirs(_dir: str) -> None:
        os.makedirs(_dir, exist_ok=True)

    @staticmethod
    def _serialize(record: dict) -> str:
        time_stamp = record["time"]
        time_stamp = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
        subset = {
            "time": time_stamp,
            "message": record["message"],
            "level": record["level"].name.lower(),
            "tag": "{}:{}".format(record["file"].path, record["line"]),
            "field": {"data": record["extra"].get("data", {})},
        }
        return json.dumps(subset, ensure_ascii=False)

    def _patching(self, record: dict) -> str:
        record["extra"]["serialized"] = self._serialize(record)
        return "{extra[serialized]}\n"

    @staticmethod
    def verbose_formatter(verbose: int) -> str:
        """formatter factory"""
        if verbose is True:
            return "verbose"
        return "simple"

    @staticmethod
    def update_log_level(debug: bool, level: str) -> str:
        """update log level"""
        if debug is True:
            level_num = logging.DEBUG
        else:
            level_num = logging.getLevelName(level)

        settings.Logger.Level = logging.getLevelName(level_num)
        return settings.Logger.Level

    def __call__(self, *args, **kwargs) -> None:
        level = self.update_log_level(
            settings.Logger.Debug, str(settings.Logger.Level).upper()
        )
        log_conf = {
            "server_handler": {
                "file": os.path.join(self._base_dir, settings.Logger.File),
                "level": level,
                "rotation": settings.Logger.Rotation,
                "backtrace": False,
                "diagnose": False,
                "encoding": settings.Logger.Encoding,
                "retention": settings.Logger.Retention,
                "enqueue": True,
            },
        }
        logger.remove()
        for _, conf in log_conf.items():
            log_file = conf.pop("file", None)
            logger.add(log_file, format=self._patching, **conf)
        logger.add(sys.stderr, format="{extra[serialized]}")
