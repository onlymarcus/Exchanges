import time
import datetime
import json
import requests

def kraken_ltc():
    krakenTick1 = requests.post('https://api.kraken.com/0/public/Ticker',data=json.dumps({"pair":"XLTCZUSD"}),
        headers={"content-type":"application/json"})
    return krakenTick1.json()['result']['XLTCZUSD']['c'][0]

def kraken_eth():
    krakenTick3 = requests.post('https://api.kraken.com/0/public/Ticker',data=json.dumps({"pair":"XETHZUSD"}),
        headers={"content-type":"application/json"})
    return krakenTick3.json()['result']['XETHZUSD']['c'][0]

while True:
    

    krakenliveltc = float(kraken_ltc())
    krakenliveeth = float(kraken_eth())

    print ('##################--KRAKEN--###########################')

    print ('ETH = U$',krakenliveeth)
    print ('LTC = U$',krakenliveltc)
    time.sleep(60)
