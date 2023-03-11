import logging
import pytest
from api_framework.src.utilities.loggings import Log
from api_framework.src.config.base_url import BaseUrl
from api_framework.src.utilities.endpoints import Endpoints
from api_framework.src.utilities.json_files_path import JsonFilesPath
from api_framework.src.utilities.read_json_file import ReadJsonFile
from api_framework.src.helper.csv_to_json_file import CsvToJsonFile

csv_json_file = CsvToJsonFile()
base_url = BaseUrl()
endpoint = Endpoints()
json_files_path = JsonFilesPath()
read_json_file = ReadJsonFile()

# log = Log()
# abc = log.custome_log(loglevel=logging.DEBUG)

final_post_url = base_url.reqres_api_domain + endpoint.reqres_patch_endpoint


def init_values(path, object_name, url, header):
    csv_json_file.convert_csv_to_json(json_files_path.csv_file_path, json_files_path.json_file_path)
    return read_json_file.post_method(path, object_name, url, header)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("test", init_values(json_files_path.json_file_path,
                                             json_files_path.fake_rest_api_object_name, final_post_url,
                                             base_url.headers))
def test_post_request(test):
    assert test.status_code == 201
    data = test.json()
    print(data)
    global id
    id = data["id"]
    #abc.info("this test is demo")


@pytest.mark.smoke
@pytest.mark.regression
def test_get_request():
    final_url = final_post_url + f'/{id}'
    response = read_json_file.get_method(final_url, base_url.headers)
    assert response.status_code == 200


@pytest.mark.sanity
@pytest.mark.regression
def test_put_request():
    final_url = final_post_url + "/" + f'{id}'
    update_payload = {"sal": 25000, "designation": "Engineer"}
    response = read_json_file.put_mehtod(json_files_path.patch_request_data, json_files_path.fake_rest_api_object_name,
                                         final_url, update_payload, id, base_url.headers)
    assert response.status_code == 200


@pytest.mark.regression
def test_delete_request():
    final_url = final_post_url + "/" + f'{id}'
    response = read_json_file.delete_method(final_url)
    assert response.status_code == 204













# @pytest.mark.parametrize("test_1", read_json_file.post_method(json_files_path.fake_rest_api,
#                                                               json_files_path.fake_rest_api_object_name, final_demo_url,
#                                                               base_url.headers))
# def test_post_parameter(test_1):
#     assert test_1.status_code == 200
#     data = test_1.json()
#     print(data)


# def test_delete_object_put_request():
#     final_url = final_post_url + "/" +f'{id}'
#     delete_payload = {"sal" : 25000}
#     response = read_json_file.remove_object_put_method(json_files_path.fake_rest_api, json_files_path.fake_rest_api_object_name, final_url, delete_payload, id, base_url.headers)
#     print(response)
