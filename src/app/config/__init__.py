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
# @Description: config 封装模块
"""

# pylint: skip-file

import sys
import threading
from pathlib import Path

from dynaconf import Dynaconf


class Settings:
    """设置类"""

    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Settings, "_instance"):
            with Settings._instance_lock:
                if not hasattr(Settings, "_instance"):
                    Settings._instance = object.__new__(cls)
        return Settings._instance

    def __init__(self):
        self._base_dir = Path(__file__).parent.parent
        self._settings_files = [Path(__file__).parent / "settings.yml"]
        self._external_files = [Path(sys.prefix, "etc", "fastapi_demo", "settings.yml")]

    def __call__(self, *args, **kwargs):
        return Dynaconf(
            # Set env `FASTAPI_DEMO_FOO='bar'`，use `settings.FOO` .
            envvar_prefix="FASTAPI_DEMO",
            settings_files=self._settings_files,  # load user configuration.
            # environments=True,  # Enable multi-level configuration，eg: default, development, production
            load_dotenv=True,  # Enable load .env
            # env_switcher='FASTAPI_DEMO_ENV',
            lowercase_read=False,  # If true, can't use `settings.foo`, but can only use `settings.FOO`
            includes=self._external_files,  # Customs settings.
            base_dir=self._base_dir,  # `settings.BASE_DIR`
        )


settings = Settings().__call__()
