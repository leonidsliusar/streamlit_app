import base64
import os
from typing import Union
from jinja2 import Environment, FileSystemLoader


image_dir = './img'
map_path = 'Screenshot from 2023-07-23 15-04-33.png'
rendered_path = 'output.html'
tem_path = './'


def get_image_paths(folder_path: str) -> list[str]:
    image_path_set = []
    for filename in os.listdir(folder_path):
        image_path = os.path.join(folder_path, filename)
        image_path_set.append(image_path)
    return image_path_set


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


def paste_in(tem_path: str, rendered_path: str, data: dict) -> None:
    env = Environment(loader=FileSystemLoader(tem_path))
    template = env.get_template('template.html')
    output = template.render(data)
    with open(rendered_path, 'w') as file:
        file.write(output)


def main() -> None:
    mapping = {
        'Typ': 'Etagenwohnung',
        'Etage': '1 von 5',
        'Preis': '100.000'
    }
    mapping_set = [list(mapping.items())[i: i + 2] for i in range(0, len(mapping), 2)]
    print(mapping_set)
    image_path_set = get_image_paths(image_dir)
    data_url_images = image_to_data_url(image_path_set)
    data_url_map = image_to_data_url(map_path)
    data = {
        'map_img': data_url_map,
        'image_path_set': data_url_images,
        'description': 'Some text here',
        'mapping_set': mapping_set
    }
    paste_in(tem_path, rendered_path, data)


main()
