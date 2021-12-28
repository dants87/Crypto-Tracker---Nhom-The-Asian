import requests
def SendMessage(ds,bot_token,chat_id,loai_tien_ao,loai_tien_te):
    msg = ""
    for i in range(len(ds)):
        msg += f"Giá {loai_tien_ao} lúc {ds[i][1]} là: {ds[i][0]} {loai_tien_te}\n"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)
def SendWarning(gia,bot_token,chat_id,loai_tien_ao,loai_tien_te,gia_canhbao):
    msg = f"Cảnh báo! Giá {loai_tien_ao} đã rơi xuống dưới {gia_canhbao}. Giá hiện tại là {gia[0]} {loai_tien_te}"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)

