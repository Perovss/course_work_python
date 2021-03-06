#!/usr/bin/env python
import api_service
import os
from subprocess import call


def open_token(filename: str):
    with open(f'{os.getcwd()}/{filename}', "r") as token_in_file:
        token = token_in_file.read().strip()
        return token


path = 'files'
ya_path = 'course'
url = 'https://api.vk.com/method/'
basic_count = 10
basic_id = 4321910

# os.system('cls||clear')
call("clear")

while True:
    id_vk = input(f'Введите ID пользователя в VK, по умолчанию ID = {basic_id}: ')
    if id_vk == '':
        id_vk = (basic_id)
    else:
        try:
            value = int(id_vk)
        except ValueError:
            print('ID - это численное значение')
            continue
    count = input(f'Введите количество скачиваемых фото по умолчанию - {basic_count}: ')
    if count == '':
        count = (basic_count)
    else:
        try:
            value = (count)
        except ValueError:
            print('ID - это численное значение')
            continue

    vk_import = api_service.VKservice(url, path, id_vk, open_token('token.txt'))
    vk_import.request_get(count)
    YA_export = api_service.YaUploader(path, open_token('token_yandex.txt'))
    YA_export.upload_file_to_disk(ya_path)

    print('Выходные данные находяться в photos.json')
    print('Ссылка на Yandex.Disc https://disk.yandex.ru/d/dR9b2W5qhYg7iw')
    break
