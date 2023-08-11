import os
import random
import streamlit as st
from dotenv import load_dotenv
from github import GithubException
from streamlit.components.v1 import html
from pages import side_bars, load_data
from streamlit_lottie import st_lottie_spinner
from utils import write_in_json, render_index, load_lottiefile, run_pages

load_dotenv()
tg_username = os.getenv('TG_USERNAME')
phone = os.getenv('PHONE')
if not tg_username:
    tg_username = st.secrets.get("tg")
if not phone:
    phone = st.secrets.get("phone")


st.set_page_config(
    page_title='Real Estate Config',
    page_icon='🏡',
    layout='wide'
)
side_bars()

animation_files = os.listdir("/animations")
random_animation_file = random.choice(animation_files)
lottie_streamlit = load_lottiefile(f"animations/{random_animation_file}")

col1, col2 = st.columns(2)

col1.header("Загрузка данных")
with col1:
    lang = st.radio('выбор языка', ('английский', 'немецкий', 'русский'), horizontal=True)
    data = load_data(lang)
    if data:
        if but := st.button(label='Развернуть страницу'):
            st.toast('Страница разворачивается', icon='⏳')
            with st_lottie_spinner(lottie_streamlit):
                title = data.get('title')
                obj_num = data.get('upd_data_df').get('objectnumber')
                try:
                    link = run_pages(rendered_html=st.session_state.page, obj_num=obj_num)
                    write_in_json(obj_num=obj_num, link=link, json_path='map.json')
                    st.experimental_rerun()
                    st.toast('Ссылка в сайд-баре слева', icon='🟢')
                except GithubException:
                    st.toast('Объект {obj_num} уже существует', icon='🔴')


with col2:
    if data:
        data.update({'tg_username': tg_username, 'phone': phone})
        rendered_html = render_index(data)
        html(rendered_html, height=2500)
        st.session_state.page = rendered_html
        with open('template.html', 'w') as file:
            file.write(rendered_html)
