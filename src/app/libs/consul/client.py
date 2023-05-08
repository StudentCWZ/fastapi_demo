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
# @Description: consul-client 初始化模块
"""


import consul


class ConsulClient:
    """consul 基本类"""

    def __init__(self, host: str, port: int, token: str = None):
        self.host = host
        self.port = port
        self.token = token
        self.client = self.__init_client()

    def __repr__(self):
        return f"<{self.__class__}: {self.__dict__}>"

    def __str__(self):
        return self.__repr__()

    def __init_client(self) -> consul.std.Consul:
        return consul.Consul(host=self.host, port=self.port, token=self.token)
