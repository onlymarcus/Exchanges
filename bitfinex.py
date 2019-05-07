import time
import datetime
import json
import requests


def bitfinex_btc(): 
    bitFinexTick1 = requests.get("https://api.bitfinex.com/v1/ticker/btcusd")
    return bitFinexTick1.json()['last_price']

def bitfinex_eth(): 
    bitFinexTick2 = requests.get("https://api.bitfinex.com/v1/ticker/ethusd")
    return bitFinexTick2.json()['last_price']

def bitfinex_ltc(): 
    bitFinexTick3 = requests.get("https://api.bitfinex.com/v1/ticker/ltcusd")
    return bitFinexTick3.json()['last_price']

def bitfinex_xrp(): 
    bitFinexTick4 = requests.get("https://api.bitfinex.com/v1/ticker/xrpusd")
    return bitFinexTick4.json()['last_price']

#def bitfinex_bch(): 
#    bitFinexTick5 = requests.get("https://api.bitfinex.com/v1/ticker/bchusd")
#    return bitFinexTick5.json()['last_price']

def bitfinex_xmr(): 
    bitFinexTick6 = requests.get("https://api.bitfinex.com/v1/ticker/xmrusd")
    return bitFinexTick6.json()['last_price']

def bitfinex_sng(): 
    bitFinexTick7 = requests.get("https://api.bitfinex.com/v1/ticker/sngusd")
    return bitFinexTick7.json()['last_price']

def bitfinex_trx(): 
    bitFinexTick8 = requests.get("https://api.bitfinex.com/v1/ticker/trxusd")
    return bitFinexTick8.json()['last_price']

def bitfinex_zec(): 
    bitFinexTick9 = requests.get("https://api.bitfinex.com/v1/ticker/zecusd")
    return bitFinexTick9.json()['last_price']

def bitfinex_eos(): 
    bitFinexTick10 = requests.get("https://api.bitfinex.com/v1/ticker/eosusd")
    return bitFinexTick10.json()['last_price']

def bitfinex_omg(): 
    bitFinexTick11 = requests.get("https://api.bitfinex.com/v1/ticker/omgusd")
    return bitFinexTick11.json()['last_price']

def bitfinex_etc(): 
    bitFinexTick12 = requests.get("https://api.bitfinex.com/v1/ticker/etcusd")
    return bitFinexTick12.json()['last_price']

def bitfinex_gnt(): 
    bitFinexTick13 = requests.get("https://api.bitfinex.com/v1/ticker/gntusd")
    return bitFinexTick13.json()['last_price']

def bitfinex_btg(): 
    bitFinexTick14 = requests.get("https://api.bitfinex.com/v1/ticker/btgusd")
    return bitFinexTick14.json()['last_price']

while True:
    bitfinexlivebtc = float(bitfinex_btc())
    bitfinexliveeth = float(bitfinex_eth())
    bitfinexliveltc = float(bitfinex_ltc())
    bitfinexlivexrp = float(bitfinex_xrp())
    #bitfinexlivebch = float(bitfinex_bch())
    bitfinexlivexmr = float(bitfinex_xmr())
    bitfinexlivebtg = float(bitfinex_btg())
    bitfinexlivesng = float(bitfinex_sng())
    bitfinexlivetrx = float(bitfinex_trx())
    bitfinexlivezec = float(bitfinex_zec())
    bitfinexliveeos = float(bitfinex_eos())
    bitfinexliveomg = float(bitfinex_omg())
    bitfinexliveetc = float(bitfinex_etc())
    bitfinexlivegnt = float(bitfinex_gnt())

    print ('###################--BITFINEX--########################')
    print ('Hora: ', datetime.datetime.now())

    print ('BTC = U$',bitfinexlivebtc)
    print ('ETH = U$',bitfinexliveeth)
    print ('LTC = U$',bitfinexliveltc)
    print ('XRP = U$',bitfinexlivexrp)
    #print ('BCH = U$',bitfinexlivebch)
    print ('XMR = U$',bitfinexlivexmr)
    print ('BTG = U$',bitfinexlivebtg)
    print ('SNG = U$',bitfinexlivesng)
    print ('TRX = U$',bitfinexlivetrx)
    print ('ZEC = U$',bitfinexlivezec)
    print ('EOS = U$',bitfinexliveeos)
    print ('OMG = U$',bitfinexliveomg)
    print ('ETC = U$',bitfinexliveetc)
    print ('GNT = U$',bitfinexlivegnt)
    time.sleep(60)

    
