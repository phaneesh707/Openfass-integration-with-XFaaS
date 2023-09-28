import json
# XFaaS specific imports
from .python.src.utils.classes.commons.serwo_objects import SerWOObject


def user_function(xfaas_object) -> SerWOObject:
    try:
        data = xfaas_object.get_body()
        if "string1" in data and "string2" in data:
            str1 = data["string1"]
            str2 = data["string2"]
            result = str1 + str2
            res = {"result":result}
        else:
            res = {"result":"Missing args"}
        result = json.dumps(res)
        return SerWOObject(body=result)
    except Exception as e:
        print(e)
        raise Exception("[SerWOLite-Error]::Error at user function",e)




