import logging
import json


def json2obj(json_str):
    try:
        obj = json.loads(json_str)
        return obj

    except json.JSONDecodeError as ex:
        logging.error("Parse json error: " + json_str)
        raise ex
    except ValueError as ve:
        logging.error("Parse json error: " + json_str)
        raise ve
