import requests
import json


base_url = 'http://127.0.0.1:8000/'
end_point = 'api/'


# def get_resource(id=None):
#     data = {}
#     if id is not None:
#         data = {
#             'id':id,
#         }
#     resp = requests.get(base_url+end_point, data = json.dumps(data))
#     print(resp.status_code)
#     data = resp.json()
#     for d in data:
#         print(d, end='\n')

# get_resource()


# def create_resource():
#     new_emp = {
#         'eno':601,
#         'ename':'Abhishek Dubey',
#         'esal':6000,
#         'eaddr':'Chennai',
#     }
#     r = requests.post(base_url+end_point, data=json.dumps(new_emp))
#     print(r.json())
#     print(r.status_code)
    

# create_resource()

def update_resource(id):
    new_data = {
        'eno':111,
        'ename':'Avdesh',
        # 'esal':10000,
        # 'eaddr':'Allahabad' ,
    }
    r = requests.put(base_url+end_point, data = json.dumps(new_data))
    print(r.status_code)
    print(r.json())

update_resource(10)


# def delete_resource(id):
#     data = {
#         'id':id,
#     }
#     r = requests.delete(base_url+end_point, data = json.dumps(data))
#     print(r.status_code)
#     print(r.json())

# delete_resource(3)