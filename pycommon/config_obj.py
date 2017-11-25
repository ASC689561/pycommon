import configparser


class ObjectConfig:
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

    def merge_env(self):
        import os
        self_attr = list(self._get_all_attr())
        for v in self_attr:
            if v in os.environ:
                setattr(self, v, os.environ[v])

    def __str__(self):
        return str(self.__dict__)

    def _get_all_attr(self):
        attrs = dir(self)
        for v in attrs:
            if str.startswith(v, '__'):
                continue
            yield v


# class AmisConfig(ObjectConfig):
#     NluProject = None
#     SmeService = None
#     BotDataService = None
#     USERNAME = None
#
#     def __init__(self):
#         super().__init__()


# obj = AmisConfig()
# obj.merge_file('/opt/projects/bot/botmit/botmit/config.ini')
# obj.merge_env('USERNAME','SmeService')
# print(obj.NluProject)
# print(obj)
