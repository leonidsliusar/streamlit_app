

def get_contact_buttons(tg_username: str):
    telegram_code = (
        "<div style='position: fixed; bottom: 20px; right: 20px;'>"
        "<script type='text/javascript'>"
        "(function() {"
        "var script = document.createElement('script');"
        "script.type = 'text/javascript';"
        "script.async = true;"
        f"script.src = '//telegram.im/widget-button/index.php?id=@{tg_username}';"
        "document.getElementsByTagName('head')[0].appendChild(script);"
        "})();"
        "</script>"
        f"<a href='https://telegram.im/@{tg_username}' target='_blank' "
        "class='telegramim_button telegramim_shadow telegramim_pulse' "
        "style='font-size: 31px; width: 78px; background: #27A5E7; border-radius: 43px; "
        "display: flex; align-items: center; justify-content: center; position: relative; "
        "margin-top: 10px; margin-right: 10px;'>"
        "<i style='font-size: 31px; color: #FFFFFF;'>.</i>"
        "</a>"
        "</div>"
    )
    return telegram_code
