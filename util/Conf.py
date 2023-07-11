#!/usr/local/bin/python3
'''
根据保存的连接信息读取配置信息到dict并返回
'''
import os


class Conf:
    def __init__(self, conn_name):
        """
        :type conn_name: string
        """
        self.conf_dict = {}
        conf_content = open(
            '{path}/{name}.conf'.format(path=os.path.dirname(os.path.dirname(__file__)), name=conn_name), mode="r")
        conf_data = conf_content.read().split("\n")
        conf_content.close()
        self.conf_dict['url'] = conf_data[1]
        self.conf_dict['port'] = conf_data[2]
        self.conf_dict['username'] = conf_data[3]
        self.conf_dict['password'] = conf_data[4]

    # 读取配置信息dict根据连接名
    def read_conn_conf(self):
        return self.conf_dict
