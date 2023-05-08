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
# @Description: consul 服务发现、注册、获取相关配置模块(该模块没有调用--根据需要调用)
"""


# pylint: skip-file


import yaml

from app.libs.consul.client import ConsulClient
from app.libs.consul.discovery import ConsulServiceDiscovery
from app.libs.consul.instance import ServiceInstance
from app.libs.consul.register import ConsulServiceRegistry
from app.utils.convert import Dict, dict_to_obj


class ConsulOperator(ConsulClient):
    """consul 操作类"""

    def __init__(self, host: str, port: int, key: str, dc: str, token: str = None):
        super().__init__(host, port, token)
        self.key = key
        self.dc = dc

    def get_data(self) -> dict:
        """获取注册中心中的数据"""
        data = self.client.kv.get(key=self.key, dc=self.dc)
        result = yaml.load(data[1]["Value"], Loader=yaml.FullLoader)
        return result

    @staticmethod
    def set_instance(name: str, host: str, port: int) -> ServiceInstance:
        return ServiceInstance(name, host, port)

    @staticmethod
    def service_registry(host: str, port: int, token: str) -> ConsulServiceRegistry:
        """服务注册"""
        return ConsulServiceRegistry(host, port, token)

    @staticmethod
    def service_discovery(host: str, port: int, token: str) -> ConsulServiceDiscovery:
        """服务发现"""
        return ConsulServiceDiscovery(host, port, token)

    def __call__(self, *args, **kwargs) -> Dict:
        """更改全局变量"""
        result = self.get_data()
        # 从注册中心获取的配置文件信息
        settings = dict_to_obj(result)
        # 获取相关 server 配置信息
        server_name, server_host, server_port = (
            settings.Server.Name,
            settings.Server.Host,
            int(settings.Server.Port),
        )
        # 服务注册与发现
        instance = self.set_instance(server_name, server_host, server_port)
        registry = self.service_registry(self.host, self.port, self.token)
        discovery = self.service_discovery(self.host, self.port, self.token)
        if not discovery.get_instances(server_name):
            registry.register(instance)
        return settings
