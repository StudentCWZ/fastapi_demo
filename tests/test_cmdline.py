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
# @Description: cmdline 测试封装模块
"""

import uvicorn
from alembic import config

import app
from app.cmd import cmdline


def test_main(cli):
    """测试"""
    result = cli.invoke(cmdline.main)
    assert result.exit_code == 0
    result = cli.invoke(cmdline.main, "-V")
    assert result.exit_code == 0
    assert str(result.output).strip() == app.__version__


def test_run(cli, mocker):
    """测试"""
    mock_run = mocker.patch.object(uvicorn, "run")
    result = cli.invoke(cmdline.main, ["server", "-h", "127.0.0.1", "-p", "8080"])
    assert result.exit_code == 0
    mock_run.assert_called_once_with(app=mocker.ANY, host="127.0.0.1", port=8080)


def test_migrate(cli, mocker):
    """测试"""
    mock_main = mocker.patch.object(config, "main")
    cli.invoke(cmdline.main, ["migrate", "--help"])
    mock_main.assert_called_once()
