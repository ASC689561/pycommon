import configparser
import logging
import os

from kazoo.client import KazooClient


class ConfigBase:
    def __init__(self):
        pass

    def merge_file(self, file_path, session_name='DEFAULT'):
        config = configparser.ConfigParser()
        config.read(file_path)
        session_value = config[session_name]
        self_attr = list(self._get_all_attr())

        for v in list(session_value):
            for k in self_attr:
                if v == k.lower():
                    setattr(self, k, session_value[v])

    def from_dic(self, dic):
        for k, v in dic.items():
            setattr(self, k, v)

    def merge_env(self, *list_property_name):
        self_attr_dic = list(self._get_all_attr())
        if len(list_property_name) == 0:
            for v in self_attr_dic:
                if v in os.environ:
                    setattr(self, v, os.environ[v])
        else:
            for v in list_property_name:
                if v not in self_attr_dic:
                    raise Exception("Property {} not in attribute of config".format(v))
                if v in os.environ:
                    try:
                        setattr(self, v, os.environ[v])
                    except:
                        logging.error("Error while try set atribute: {}".format(v))

    def __str__(self):
        import json
        return json.dumps(self.__dict__, indent=4)

    def _get_all_attr(self):
        attr = dir(self)
        for v in attr:
            if str.startswith(v, '__'):
                continue
            yield v

#
# class AmisConfig(ObjectConfig):
#     NluProject = None
#     SmeService = None
#     BotDataService = None
#     USERNAME = None
#
#     def __init__(self):
#         super().__init__()
#
#
# obj = AmisConfig()
# obj.merge_file('/opt/projects/bot/botmit/botmit/config.ini')
# # obj.merge_env('USERNAME', 'SmeService')
# obj.merge_env()
# # print(obj.NluProject)
# print(obj)
