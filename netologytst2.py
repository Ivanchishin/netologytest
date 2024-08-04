import pytest
import requests

#Задача №2 Автотест API Яндекса

class TestYandexDisk:
    def setup_method(self):
        ya_token = 'ВСТАВИТЬ ЯНДЕКС ТОКЕН СЮДА'
        self.headers = {
            'Authorization': f'OAuth {ya_token}'
        }

    @pytest.mark.parametrize(
        'key,value,status',
        (
                ['path', 'Image', 201],
                ['path', 'Image', 409],
                ['pat', 'Image', 400],
        )
    )
    def test_create_folder_201(self, key, value, status):
        params = {
            key: value
        }
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)
        assert response.status_code == status

    @pytest.mark.parametrize(
        'key, path, permanently, value, status',
        (
                ['path', 'Image','permanently', True, 204],
                ['path', 'Image','permanently', True, 404],
        )
    )
    def test_delete_folder(self, key,path, permanently,value, status):
        params = {
            key: path,
            permanently:value
        }
        response = requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)
        assert response.status_code == status