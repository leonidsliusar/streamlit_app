import os
from typing import Optional
import pandas as pd
import streamlit as st
from utils import load_lottiefile, dict_to_df, read_from_json, remove_repo, df_to_dict
from streamlit_lottie import st_lottie
from key_val_map import values, keys, en_attr_key, de_attr_key, ru_attr_key, keys_en
from utils import hint_desc, upload_photo


lang_map = {
    'английский': 'en',
    'немецкий': 'de',
    'русский': 'ru'

}


def side_bars():
    path = os.path.dirname(__file__)
    path_to_json = path + '/map.json'
    hint_lottie = load_lottiefile('hint.json')
    with st.sidebar.expander('Подсказка для поля "описание":\n\nтеги для форматирования текста'):
        st.markdown(hint_desc)
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
                               value=default_data.get('description', ''))
    plan = st.file_uploader('Планировка', accept_multiple_files=True)
    if plan:
        with st.sidebar.expander(label='Порядок фото планировки', expanded=False):
            img_plan = upload_photo(plan)
    furnishing = st.text_input(f'Мебелирование {lang_key}', value=default_data.get('furnishing', ''))
    map_url = st.text_input("Введите ссылку на карту Google Maps:", help='Подсказка в сайд-баре слева')
    additional = st.text_input(f'Особенности {lang_key}', value=default_data.get('additional', ''))
    st.session_state.data.update(
        {
            lang_key: {
                'title': title,
                'description': description,
                'furnishing': furnishing,
                'additional': additional,
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
        data = {
            'data': st.session_state.data,
            'upd_data_df': dict(zip(keys_en, upd_data_df['value'])),
            'plan': img_plan,
            'map_url': map_url,
            'images': img
        }
    return data
