import json
import subprocess


def execute_curl(curl):
    try:
        p = subprocess.Popen(curl, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        obj = json.loads(out.decode())
        return obj
    except Exception as e:
        print(err)
        print(out)
        raise e