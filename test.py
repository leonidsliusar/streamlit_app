import streamlit as st
import base64
from streamlit.components.v1 import html

from logo.tg import telegram_code


def create_contact_button(name, link, icon_dataurl):
    return f'<a href="{link}" target="_blank"><img src="{icon_dataurl}" alt="{name}"></a>'


# Контакты в WhatsApp и Telegram
contacts = {
    "WhatsApp": "https://wa.me/1234567890",
    "Telegram": "https://t.me/sales_department",
    "Phone Call": "tel:+1234567890",
}

# Создание словаря с соответствием между именем контакта и его значком (data URL)
contact_icons = {}
with open("logo/wsup.jpg", "rb") as image_file:
    contact_icons["WhatsApp"] = base64.b64encode(image_file.read()).decode("utf-8")

with open("logo/tg.png", "rb") as image_file:
    contact_icons["Telegram"] = base64.b64encode(image_file.read()).decode("utf-8")

with open("logo/phone.png", "rb") as image_file:
    contact_icons["Phone Call"] = base64.b64encode(image_file.read()).decode("utf-8")

# Создание кнопок для контактов с использованием соответствующих значков
for name, link in contacts.items():
    icon_dataurl = contact_icons[name]
    st.markdown(create_contact_button(name, link, icon_dataurl), unsafe_allow_html=True)



