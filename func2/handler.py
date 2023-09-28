# XFaaS specific imports
from .python.src.utils.classes.commons.serwo_objects import SerWOObject
from .python.src.utils.classes.commons.serwo_objects import build_serwo_object
from .helper import user_function
import datetime



import json

def handle(req):
    try:
        print("req from func2",req,"\n")
        XfaaSObj = SerWOObject(body=json.loads(req))
        result = user_function(XfaaSObj)
        res = result.get_body()
        return json.dumps(res)
    except Exception as e:
        print(f"func2 Error : {str(e)}")



