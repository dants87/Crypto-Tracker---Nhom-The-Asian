import datetime
def Data_Filter(reponse_json,loai_tien_ao,loai_tien_te):
    gia_thoigian=[]
    coin_price=reponse_json['data'][loai_tien_ao]
    gia_thoigian.append(coin_price['quote'][loai_tien_te]['price'])
    dt_now = datetime.datetime.now()
    dt_now = dt_now.strftime('%H:%M:%S, %d/%m/%Y')
    gia_thoigian.append(dt_now)
    return gia_thoigian
