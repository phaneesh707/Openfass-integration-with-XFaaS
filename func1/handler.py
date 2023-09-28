# XFaaS specific imports
from .python.src.utils.classes.commons.serwo_objects import SerWOObject
from .python.src.utils.classes.commons.serwo_objects import build_serwo_object
from .helper import user_function
import datetime

import json

def handle(req):
    try:
        data = json.loads(req)
        # XFaaSObj = unmarshall(data);
        XfaaSObj = SerWOObject(body=data)
        result = user_function(XfaaSObj)
        res = result.get_body()
        return json.dumps(res)
    except Exception as e:
        print(f"func1 Error : {str(e)}")

