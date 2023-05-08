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
# @Description: consul 服务发现
"""


# pylint: skip-file


import abc

from app.libs.consul.client import ConsulClient
from app.libs.consul.instance import ServiceInstance


class ServiceDiscovery(abc.ABC):
    """服务发现"""

    @abc.abstractmethod
    def get_services(self) -> list:
        """获取服务"""

    @abc.abstractmethod
    def get_instances(self, service_id: str) -> list:
        """获取 instances"""


class ConsulServiceDiscovery(ServiceDiscovery):
    _consul = None

    def __init__(self, host: str, port: int, token: str = None):
        self._consul = ConsulClient(host, port, token=token).client

    def get_services(self) -> list:
        return self._consul.catalog.services()[1].keys()

    def get_instances(self, service_id: str) -> list:
        """获取 instances"""
        origin_instances = self._consul.catalog.service(service_id)[1]
        result = []
        for oi in origin_instances:
            result.append(
                ServiceInstance(
                    oi.get("ServiceName"),
                    oi.get("ServiceAddress"),
                    oi.get("ServicePort"),
                    oi.get("ServiceTags"),
                    oi.get("ServiceMeta"),
                    oi.get("ServiceID"),
                )
            )
        return result
