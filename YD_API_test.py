import requests
from pprint import pprint

def create_YD_folder(yd_token, folder_name):

    auth = {'Authorization': f'OAuth {yd_token}'}
    create_folder = requests.put(f'https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2F{folder_name}',
                            headers=auth)
    response = create_folder.json()

    return response

class TestYDAPI:

    def setup(self):
        print("method setup")

    def teardown(self):
        print("method teardown")

    def test_create_folder(self):
        assert create_YD_folder('correct_token', '111')['method'] == 'GET'

    def test_create_same_folder(self):
        assert create_YD_folder('correct_token', '111')['message'] == 'По указанному пути "disk:/111" уже существует папка с таким именем.'

    def test_wrong_token(self):
        assert create_YD_folder('wrong_token', '111')['description'] == 'Unauthorized'

if __name__ == '__main__':
    yd_token = ''
    folder_name = '111'
    response = create_YD_folder(yd_token,folder_name)