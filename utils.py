import base64
import io

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


def get_preview_html(title, address, data, data_urls, description, upload_map):
    output = io.StringIO()
    output.write(f"<h1 style='font-family: Arial, sans-serif;'>{title}</h1>\n")
    output.write(f"<h2 style='font-family: Times New Roman, serif;'>{address}</h2>\n")
    thumbnail_html = ""
    for index, data_url in enumerate(data_urls):
        thumbnail_html += f'<img class="expandable-image" src="{data_url}" onclick="expandImage(this, {index})">'
    output.write(f'{css}<div class="preview">{thumbnail_html}</div>{js}\n')
    output.write(f"<h3 style='font-family: Times New Roman, serif;'>{description}</h3>\n")
    for i in data:
        output.write(f"<b>{i['Название поля']}</b>: {i['Данные поля']}\n<br>")
    html_code = output.getvalue()
    return html_code
