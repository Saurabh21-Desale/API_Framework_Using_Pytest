import json
import requests
from api_framework.src.helper.write_json_file import WriteJsonFile


class ReadJsonFile(object):

    def __init__(self):
        self.load_json_file = WriteJsonFile()

    def post_method(self, payload, object_names, url, header=None):
        json_file = self.load_json_file.read_data_from_json_file(payload, object_names)
        file = json.loads(json_file)
        for i in file[object_names]:
            response = requests.post(url, data=json.dumps(i), headers=header)
            yield response

    def get_method(self, url, header=None):
        response = requests.get(url)
        return response

    def put_mehtod(self, payload, object_name, url, update_payload, body_id, header=None):
        data = self.load_json_file.update_payload(payload, object_name, body_id, update_payload)
        response = requests.put(url, data=json.dumps(data), headers=header)
        return response

    def remove_object_put_method(self, payload, object_name, url, delete_payload, body_id, header=None):
        data = self.load_json_file.delete_payload(payload, object_name, body_id, delete_payload)
        response = requests.put(url, data=json.dumps(data), headers=header)
        return response

    def patch_method(self, payload, object_name, url, append_payload, body_id, header=None):
        data = self.load_json_file.update_payload(payload, object_name, body_id, append_payload)
        response = requests.patch(url, data=json.dumps(data), headers=header)
        return response

    def delete_method(self, url):
        response = requests.delete(url)
        return response
