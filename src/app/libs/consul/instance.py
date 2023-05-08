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
# @Description: consul 基本类
"""


# pylint: skip-file


class ServiceInstance:
    """服务 Instance 相关类"""

    def __init__(
        self,
        service_id: str,
        host: str,
        port: int,
        secure: bool = False,
        metadata: dict = None,
        instance_id: str = None,
    ):
        self.service_id = service_id
        self.host = host
        self.port = port
        self.secure = secure
        self.metadata = metadata
        self.instance_id = instance_id or self.get_instance_id()

    def get_instance_id(self) -> str:
        instance_id = "{}-{}-{}".format(self.service_id, self.host, self.port)
        return instance_id
