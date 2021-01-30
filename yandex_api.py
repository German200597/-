import requests
import os


token=input('Введите токен: ')
file_directory=input('Введите путь до файла на компьютере: ')

HEADERS = {'Authorization': f'OAuth {token}'}

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        self.file_path = file_directory
        step1 = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', 
        params={'path' : os.path.basename(file_directory), 'overwrite' : 'true'},
        headers=HEADERS)  
        step1 = step1.json()
        href = step1['href']
        with open (file_directory) as f:
            step2 = requests.put(href, files={'file': f})
        if step2.status_code == 201:
            print('Файл успешно загружен')
        else:
            print('Что-то пошло не так')    

if __name__ == '__main__':
    uploader = YaUploader(token)
    result = uploader.upload(file_directory)
    


