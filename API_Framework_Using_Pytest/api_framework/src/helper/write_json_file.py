import json
from api_framework.src.helper.create_payload import CreatePayload


class WriteJsonFile(object):

    def __init__(self):
        self.dictobj = []
        self.add_multi_element = {}
        self.create_payload = CreatePayload()

    def read_data_from_json_file(self, payload, object_name):
        with open(payload) as json_file:
            self.dictobj = json.load(json_file)
        for i in self.dictobj[object_name]:
            i.update({"email": f"{self.create_payload.create_email()}"})
            with open(payload, "w", encoding='utf-8') as json_file:
                json.dump(self.dictobj, json_file, indent=4)
        json_file = json.dumps(self.dictobj)
        return json_file

    def update_payload(self, payload, object_name, body_id, update_payload=None):
        json_file = self.read_data_from_json_file(payload, object_name)
        file = json.loads(json_file)
        for self.add_multi_element in file[object_name]:
            if self.add_multi_element["id"] == body_id:
                self.add_multi_element.update(update_payload)
                with open(payload, "w", encoding='utf-8') as json_file:
                    json.dump(file, json_file, indent=4)
        return self.add_multi_element













    # def delete_payload(self, payload, object_names, body_id, delete_payload=None):
    #     json_file = self.read_data_from_json_file(payload, object_names)
    #     file = json.loads(json_file)
    #     for self.delete_payload in file[object_names]:
    #         if self.delete_payload["id"] == body_id:
    #             self.delete_payload.pop(delete_payload)
    #             with open(payload, "w", encoding='utf-8') as json_file:
    #                 json.dump(file, json_file, indent=4)
    #     return self.delete_payload
