import base64
import io

from streamlit.components.v1 import html

from js import js
from logo.tg import get_contact_buttons
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


def get_html(title: str, address: str, data: str, data_urls: str, description: str, map_url: str,
             tg_username: str, phone: str):
    output = io.StringIO()
    output.write('<meta charset="UTF-8">')
    output.write('<link rel="stylesheet" href="https://use.fontawesome.com/releases/v6.0.0-beta3/css/all.css">')
    output.write(css)
    output.write(js)
    output.write(f"<h1 style='font-family: Arial, sans-serif;'>{title}</h1>\n")
    output.write(f"<h2 style='font-family: Times New Roman, serif;'>{address}</h2>\n")
    thumbnail_html = ""
    for index, data_url in enumerate(data_urls):
        thumbnail_html += f'<img class="expandable-image" src="{data_url}" onclick="expandImage(this, {index})">'
    output.write(f'<div class="preview">{thumbnail_html}</div>')
    output.write(f"<h3 style='font-family: Times New Roman, serif;'>{description}</h3>\n")
    for i in data:
        output.write(f"<b>{i['Название поля']}</b>: {i['Данные поля']}\n<br>")
    if map_url:
        output.write(f"{map_url}")
    tg_button, ws_button = get_contact_buttons(tg_username, phone)
    output.write(tg_button)
    output.write(ws_button)
    html_code = output.getvalue()
    return html_code


def create_contact_button(name, phone_number):
    return f'<a href="tel:{phone_number}"><button>{name}: {phone_number}</button></a>'
