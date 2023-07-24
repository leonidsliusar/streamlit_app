import streamlit as st
import base64

from js import js
from styles import css


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


upload_images = st.file_uploader('Перетащите фотографии сюда', accept_multiple_files=True)


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
