import json
# XFaaS specific imports
from .python.src.utils.classes.commons.serwo_objects import SerWOObject


def user_function(xfaas_object) -> SerWOObject:
    try:
        data = xfaas_object.get_body()
        data = json.loads(data)
        if "result" in data:
            result = data["result"] + "from func2"
            res = {"result":result}
        else:
            res = {"result":"Missing args"}
        result = json.dumps(res)
        return SerWOObject(body=result)
    except Exception as e:
        print(e)
        raise Exception("[SerWOLite-Error]::Error at user function",e)




