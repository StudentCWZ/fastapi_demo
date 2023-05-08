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
# @Description: consul 服务注册
"""


# pylint: skip-file


import abc

import consul

from app.libs.consul.client import ConsulClient
from app.libs.consul.instance import ServiceInstance


class ServiceRegistry(abc.ABC):
    """服务注册"""

    @abc.abstractmethod
    def register(self, service_instance: ServiceInstance):
        """服务注册"""

    @abc.abstractmethod
    def deregister(self):
        """服务注销"""


class ConsulServiceRegistry(ServiceRegistry):
    """consul 服务注册"""

    _consul = None
    _instance_id = None

    def __init__(self, host: str, port: int, token: str = None):
        self.host = host
        self.port = port
        self.token = token
        self._consul = ConsulClient(host, port, token=token).client

    def register(
        self,
        service_instance: ServiceInstance,
        interval: str = "5s",
        timeout: str = "30s",
        deregister: str = "30s",
    ):
        check = consul.Check().tcp(
            service_instance.host, service_instance.port, interval, timeout, deregister
        )
        self._consul.agent.service.register(
            service_instance.service_id,
            service_id=service_instance.instance_id,
            address=service_instance.host,
            port=service_instance.port,
            check=check,
        )
        self._instance_id = service_instance.instance_id

    def deregister(self):
        if self._instance_id:
            self._consul.agent.service.deregister(service_id=self._instance_id)
            self._instance_id = None
