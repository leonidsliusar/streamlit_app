import os
from typing import Optional
import pandas as pd
import streamlit as st
from utils import load_lottiefile, dict_to_df, read_from_json, remove_repo, df_to_dict
from streamlit_lottie import st_lottie
from key_val_map import values, keys, en_attr_key, de_attr_key, ru_attr_key, keys_en, obj_type_back_mapping
from utils import upload_photo

lang_map = {
    'английский': 'en',
    'немецкий': 'de',
    'русский': 'ru'

}


def side_bars():
    path = os.path.dirname(__file__)
    path_to_json = path + '/map.json'
    hint_lottie = load_lottiefile(path_to_json + '/hint.json')
    link_mapping_data = read_from_json(path_to_json)
    with st.sidebar.expander('Соответствие существующих заголовков и ссылок'):
        df = dict_to_df(link_mapping_data)
        edited_df = st.data_editor(df, hide_index=True)
        if st.button('✅ подтвердить изменения'):
            update_map = df_to_dict(edited_df)
            remove_repo(update_map, path_to_json)
            st.experimental_rerun()
    with st.sidebar.expander('Как встроить карту Google Maps'):
        st_lottie(hint_lottie, loop=True, quality='high')


def load_data(lang: str) -> Optional[dict]:
    if 'data' not in st.session_state:
        st.session_state.data = {}
    upload_images = st.file_uploader('Перетащите фотографии сюда', accept_multiple_files=True)
    img = None
    img_plan = None
    data = None
    lang_key = lang_map.get(lang)
    if upload_images:
        with st.sidebar.expander(label='Порядок фото', expanded=False):
            img = upload_photo(upload_images)
    default_data = st.session_state.data.get(lang_key, {})
    title = st.text_input(f'Заголовок {lang_key}', value=default_data.get('title', ''))
    data_df = pd.DataFrame(
        {
            'key': keys,
            'value': values
        }
    )
    column_config = {
        'key': st.column_config.TextColumn(
            label='параметры',
            disabled=True,
        ),
        'value': st.column_config.TextColumn(
            label='значения',
        ),
    }
    with st.expander('Ввод параметров', expanded=False):
        upd_data_df = st.data_editor(
            data_df,
            use_container_width=True,
            column_config=column_config,
            hide_index=True,
        )
    description = st.text_area(f'Описание {lang_key}', height=300, max_chars=None,
                               value=default_data.get('description', ''),
                               help='Для перехода на новую строку нажать Enter+shift')
    map_url = st.text_input("Введите ссылку на карту Google Maps:", help='Подсказка в сайд-баре слева')
    st.session_state.data.update(
        {
            lang_key: {
                'title': title,
                'description': description,
            }
        }
    )
    title_flag = any((item.get('title') for item in st.session_state.data.values()))
    if title_flag and upd_data_df['value'].values[1]:
        if st.session_state.data.get('en'):
            st.session_state.data.get('en').update(en_attr_key)
        if st.session_state.data.get('de'):
            st.session_state.data.get('de').update(de_attr_key)
        if st.session_state.data.get('ru'):
            st.session_state.data.get('ru').update(ru_attr_key)
        key_val_obj_type_map = {}
        for ln in ('en', 'de', 'ru'):
            key_val_obj_type_map.update({ln: upd_data_df.loc[upd_data_df['key'] == f'object type {ln}']})
        for ln_key in key_val_obj_type_map:
            ln_val = key_val_obj_type_map.get(ln_key)
            if not ln_val.empty:
                obj_type = obj_type_back_mapping.get(ln_val['key'].values[0])
                obj_type_value = ln_val['value'].values[0]
                st.session_state.data.get(f'{ln_key}', {}).update(
                    {'objecttype': f'{obj_type}', 'objecttypeval': obj_type_value})
        data = {
            'data': st.session_state.data,
            'upd_data_df': dict(zip(keys_en, upd_data_df['value'])),
            'map_url': map_url,
            'images': img
        }
    return data
