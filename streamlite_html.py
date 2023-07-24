import streamlit as st
from js import js
from styles import css
from utils import image_to_data_url, get_preview_html

data_urls = None
st.title('Введите данные в поля')
upload_images = st.file_uploader('Перетащите фотографии сюда', accept_multiple_files=True)
title = st.text_input('Заголовок')
address = st.text_input('Адрес')
description = st.text_input('Описание')
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
upload_map = st.file_uploader('Перетащите сюда карту')
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
if upload_map:
    map_bytes = upload_map.read()
    data_url_map = image_to_data_url(map_bytes)

if data_urls:
    payload_data = {
        'title': title,
        'address': address,
        'data': data,
        'data_urls': data_urls,
        'description': description,
        'upload_map': upload_map
    }
    html_code = get_preview_html(**payload_data)
    st.download_button('Скачать HTML', html_code, file_name='preview.html', mime='text/html')
