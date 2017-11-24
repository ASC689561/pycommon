# import configparser
#
#
# class ObjectConfig:
#     NluProject = None
#
#     def __init__(self, config_file):
#         config = configparser.ConfigParser()
#         config.read(config_file)
#
#         self.__set_value()
#         pass
#
#     def __get_env_or_config(key, default_value=None, session='DEFAULT'):
#         session = config[session]
#         if key in os.environ:
#             return os.environ[key]
#
#         value = session.get(key, None)
#         if value is None:
#             return default_value
#         return value
#
#     def __set_value(self):
#         attrs = dir(self)
#         for v in attrs:
#             if str.startswith(v, '__'):
#                 continue
#             print(v)
#             value = get_env_or_config(v)
#             setattr(self, v, value)
#
#     def list_all(self):
#         pass
