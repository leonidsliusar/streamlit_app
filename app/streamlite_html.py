import os.path

import streamlit as st
from streamlit.components.v1 import html
from js import js
from logo.tg import get_contact_buttons
from styles import css
from utils import image_to_data_url, get_html

file_name = "Screencast from 07-24-2023 09_31_47 PM.mp4"
video_path = os.path.abspath(file_name)

data_urls = None
st.markdown('<link rel="stylesheet" href="https://use.fontawesome.com/releases/v6.0.0-beta3/css/all.css">',
            unsafe_allow_html=True)
st.title('Введите данные в поля')
upload_images = st.file_uploader('Перетащите фотографии сюда', accept_multiple_files=True)
title = st.text_input('Заголовок')
address = st.text_input('Адрес')
description = st.text_input('Описание')
tg_username = st.text_input('Введите имя пользователя телеграм')
phone = st.text_input('Введите номер телефона')
data = st.session_state.get("data", [])

if st.button("Добавить атрибут"):
    data.append({"Название поля": "", "Данные поля": ""})

table = st.table(data)

indices_to_remove = []
for i, row in enumerate(data):
    col1, col2, col3 = st.columns([2, 2, 1])
    row["Название поля"] = col1.text_input(f"Row {i + 1}, Название поля", row["Название поля"])
    row["Данные поля"] = col2.text_input(f"Row {i + 1}, Данные поля", row["Данные поля"])
    if col3.button(f"Удалить {i + 1}"):
        indices_to_remove.append(i)

for index in reversed(indices_to_remove):
    data.pop(index)

st.session_state["data"] = data
map_url = st.text_input("Введите ссылку на карту Google Maps:")
st.text('Как встроить карту Google Maps')
st.video(video_path)
st.markdown("## Превью:")
st.markdown(f"<h1 style='font-family: Arial, sans-serif;'>{title}</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 style='font-family: Times New Roman, serif;'>{address}</h2>", unsafe_allow_html=True)
if upload_images:
    images = []
    for image in upload_images:
        image_bytes = image.read()
        images.append(image_bytes)
    data_urls = image_to_data_url(images)
    thumbnail_html = ""
    for index, data_url in enumerate(data_urls):
        thumbnail_html += f'<img class="expandable-image" src="{data_url}" onclick="expandImage(this, {index})">'
    st.markdown(f'{css}<div class="preview">{thumbnail_html}</div>{js}', unsafe_allow_html=True)
st.markdown(f"<h3 style='font-family: Times New Roman, serif;'>{description}</h3>", unsafe_allow_html=True)
for i in data:
    st.markdown(f"<b>{i['Название поля']}</b>: {i['Данные поля']}", unsafe_allow_html=True)
st.markdown(f'{map_url}', unsafe_allow_html=True)
tg_button, ws_button = get_contact_buttons(tg_username, phone)
html(tg_button)
st.markdown(f'{css}{ws_button}', unsafe_allow_html=True)
phone = phone if phone else '4917623158848'
tg_username = tg_username if tg_username else '4917623158848'


def render():
    if title and data_urls:
        payload_data = {
            'title': title,
            'address': address,
            'data': data,
            'data_urls': data_urls,
            'description': description,
            'map_url': map_url,
            'tg_username': tg_username,
            'phone': phone
        }
        html_code = get_html(**payload_data)
        with open(f'rendered/{title}.html', 'w', encoding='utf-8') as file:
            file.write(html_code)
        file_url = f'rendered/{title}.html'
        st.markdown(f'<a href="{file_url}" target="_blank">Ваша ссылка</a>', unsafe_allow_html=True)


st.button(label='Получить ссылку', on_click=render)
