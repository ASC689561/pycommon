import logging


def execute_curl(curl):
    import json
    import subprocess
    try:
        p = subprocess.Popen(curl, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        obj = json.loads(out.decode())
        return obj
    except Exception as e:
        logging.error('Error when execute url')
        raise e
