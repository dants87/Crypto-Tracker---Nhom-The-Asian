import getdata
import sendmessage
import datafilter
import time
#from gui import *
#_____________________________________________________
api_key="d4e19d4e-eef3-48da-aea8-6bb8c9826532"
bot_token='5083403560:AAEHfZeL6NTOQhMErqOZzGHSM44kxcHotg4'
#chat_id='5019415587'
coin_name={
    0:'Bitcoin',
    1:'Etherum'
}

#______________________________________________________
ds = []

def execute(chat_id,loai_tien_ao,time_interval,N,gia_canhbao,loai_tien_te):
    global ds
    reponse_json=getdata.GetData(loai_tien_te)
    gia_thoigian=datafilter.Data_Filter(reponse_json,loai_tien_ao,loai_tien_te)
    if gia_thoigian[0] <= gia_canhbao:
        sendmessage.SendWarning(gia_thoigian,bot_token,chat_id,coin_name[loai_tien_ao],loai_tien_te,gia_canhbao)
    ds.append(gia_thoigian)
    if len(ds)>=N:
        sendmessage.SendMessage(ds,bot_token,chat_id,coin_name[loai_tien_ao],loai_tien_te)
        ds=[]
    time.sleep(time_interval/N)
