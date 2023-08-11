import base64
import io
import json
import os
from typing import Optional
from urllib.parse import urlparse

import requests
import streamlit as st
import pandas as pd
from PIL import Image
from jinja2 import Environment, FileSystemLoader
from pandas import DataFrame
from streamlit_image_select import image_select
from streamlit_sortables import sort_items

from key_val_map import editor_keys
from github_hook import GitHubManager


def image_to_data_url(images):
    if isinstance(images, list):
        encoded_image_set = []
        for image in images:
            encoded_image = base64.b64encode(image).decode('utf-8')
            data_url = f"data:image/jpeg;base64,{encoded_image}"
            encoded_image_set.append(data_url)
        output = encoded_image_set
    else:
        with open(images, 'rb') as image_file:
            image_data = image_file.read()
            encoded_image = base64.b64encode(image_data).decode('utf-8')
            _, image_extension = images.split('.')
            mime_type = f"image/{image_extension.lower()}"
            output = f"data:{mime_type};base64,{encoded_image}"
    return output


def write_in_json(obj_num: str, link: str, json_path: str) -> None:
    with open(json_path, 'r') as file:
        link_mapping_data = json.load(file)
    if 'None' in link_mapping_data:
        link_mapping_data = {obj_num: link}
    else:
        link_mapping_data.update({obj_num: link})
    with open(json_path, 'w') as file:
        json.dump(link_mapping_data, file)


def read_from_json(json_path: str) -> dict:
    with open(json_path, 'r') as file:
        link_mapping_data = json.load(file)
    return link_mapping_data


def update_from_json(update_map: dict, json_path: str) -> None:
    with open(json_path, 'w') as file:
        json.dump(update_map, file)


def remove_repo(update_map: dict, json_path: str) -> None:
    with open(json_path, 'r') as file:
        linked_map = json.load(file)
    obj_num_set = set(linked_map).difference(set(update_map))
    manager = GitHubManager(obj_num='000')
    for obj_num in obj_num_set:
        manager.delete_repo(obj_num)
    update_from_json(update_map, json_path)


def upload_photo(photo) -> Optional[list]:
    if not photo:
        return
    original_items = [str(file.id) for file in photo]
    sorted_items = sort_items(original_items)
    images = []
    for img in photo:
        img_data = io.BytesIO(img.read())
        images.append(Image.open(img_data).convert('RGB'))
    img_index_map = dict(zip(original_items, images))
    if sorted_items is not original_items:
        images = []
        for i in sorted_items:
            images.append(img_index_map.get(i))
    image_select(label='Загруженные фото', images=images, use_container_width=False)
    img_data_set = []
    for im in images:
        data = io.BytesIO()
        im.save(data, 'JPEG')
        encoded_img_data = base64.b64encode(data.getvalue())
        img_data_set.append(encoded_img_data.decode('utf-8'))
    return img_data_set


def render_index(data: dict):
    path = os.path.dirname(__file__)
    env = Environment(loader=FileSystemLoader('.'))
    path_to_template = path + '/index.html'
    template = env.get_template(path_to_template)
    rendered_html = template.render(data)
    return rendered_html


def load_lottiefile(filepath: str) -> dict:
    with open(filepath, "r") as f:
        return json.load(f)


def dict_to_df(data: dict) -> DataFrame:
    data_set = []
    for key in data:
        value = data.get(key)
        data_set.append({editor_keys[0]: key, editor_keys[1]: value, editor_keys[2]: False})
    df = pd.DataFrame(data_set)
    return df


def df_to_dict(df: DataFrame) -> dict:
    data = {}
    for val in df.values:
        if not val[2]:
            data.update({val[0]: val[1]})
    return data


def run_pages(rendered_html, obj_num: str) -> str:
    if rendered_html:
        manager = GitHubManager(rendered_html, obj_num)
        page_link = manager.get_link
        while not link_checker(page_link):
            ...
        return page_link


def link_checker(page_link: str) -> bool:
    response = requests.head(page_link)
    return str(response.status_code).startswith('2') or str(response.status_code).startswith('3')


hint_desc = '''
Основные теги HTML разетки для форматирование текста
Подробнее: https://html5book.ru/html-html5/

<br>Текст: Перенос строки - создает перенос строки (без абзацев) ЗАКРЫВАЮЩИЙСЯ ТЕГ НЕ ТРЕБУЕТСЯ.\n\n
<p>Текст</p>: Параграф - создает абзац текста.\n
<strong>Текст</strong>: Жирный шрифт - используется для выделения текста жирным.\n
<em>Текст</em>: Курсив - используется для выделения текста курсивом.\n
<u>Текст</u>: Подчеркивание - применяет подчеркивание к тексту.\n
<ul>Текст</ul>: Маркированный список - создает маркированный список (с точками, кружками и т.д.).\n\n
<ol>Текст</ol>: Нумерованный список - создает нумерованный список (с цифрами).\n\n
<li>Текст</li>: Элемент списка - используется внутри <ul> или <ol> для создания элементов списка.\n\n
<a>Ссылка</a>: Гиперссылка - создает ссылку на другую страницу или ресурс.\n
'''
