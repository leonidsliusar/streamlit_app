

def get_contact_buttons(tg_username: str, phone: str):
    telegram_code = (
        "<script type='text/javascript'>(function() {var script = document.createElement('script');"
        "script.type = 'text/javascript';"
        "script.async = true;"
        f"script.src = '//telegram.im/widget-button/index.php?id=@{tg_username}';"
        "document.getElementsByTagName('head')[0].appendChild(script);"
        "})();"
        "</script>"
        f"<a href='https://telegram.im/@{tg_username}' target='_blank' "
        "class='telegramim_button telegramim_shadow telegramim_pulse' "
        "style='font-size: 31px; width: 78px; background: #27A5E7;"
        "box-shadow:1px 1px 5px #27A5E7;color:#FFFFFF;border-radius:43px;"
        "position: fixed; bottom: 20px; right: 20px;' title=''><i></i></a>"
    )
    ws_code = (
        f"<a href='https://api.whatsapp.com/send?phone={phone}' target='_blank' "
        "title='' rel='noopener noreferrer'><div class='whatsapp-button'>"
        "<i class='fab fa-whatsapp' aria-hidden='true'></i></div></a>"
    )
    return telegram_code, ws_code
