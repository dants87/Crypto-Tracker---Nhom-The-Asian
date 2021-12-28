import requests
import json

def GetData(loai_tien_te):
    api_key = 'd4e19d4e-eef3-48da-aea8-6bb8c9826532'
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': api_key}
    parameters = {'convert': loai_tien_te.upper()}
# gửi request đến coinmarketcap api
    response = requests.get(url, headers = headers, params = parameters)
    response_json = response.json()
    return response_json



