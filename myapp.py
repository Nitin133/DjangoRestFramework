import requests
import json
import io

URL="http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data= {'id': id}
    json_data=json.dumps(data)

    r=requests.get(url=URL, data=json_data)

    #data=r.json()
    #print(r)
    print(json_data)


#get_data()


