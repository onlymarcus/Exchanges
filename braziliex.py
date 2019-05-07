import time
import datetime
import json
import requests

def braziliex_usdt():
    braziliexusdttick = requests.get('https://braziliex.com/api/v1/public/ticker/usdt_brl')
    return braziliexusdttick.json()['lowestAsk']

def braziliex_btc():
    braziliextick = requests.get('https://braziliex.com/api/v1/public/ticker/btc_brl')
    return braziliextick.json()['lowestAsk']

def braziliex_eth():
    braziliexeth = requests.get('https://braziliex.com/api/v1/public/ticker/eth_brl')
    return braziliexeth.json()['lowestAsk']

def braziliex_ltc():
    braziliexltc = requests.get('https://braziliex.com/api/v1/public/ticker/ltc_brl')
    return braziliexltc.json()['lowestAsk']

def braziliex_mxt():
    braziliexmxt = requests.get('https://braziliex.com/api/v1/public/ticker/mxt_brl')
    return braziliexmxt.json()['lowestAsk']

def braziliex_sngls():
    braziliexsngls = requests.get('https://braziliex.com/api/v1/public/ticker/sngls_brl')
    return braziliexsngls.json()['lowestAsk']

#def braziliex_trx():
     #braziliextrx = requests.get('https://braziliex.com/api/v1/public/ticker/trx_brl')
     #return braziliextrx.json()['lowestAsk']

def braziliex_xmr():
    braziliexxmr = requests.get('https://braziliex.com/api/v1/public/ticker/xmr_brl')
    return braziliexxmr.json()['lowestAsk']

#def braziliex_eos():
     #braziliexeos = requests.get('https://braziliex.com/api/v1/public/ticker/eos_brl')
     #return braziliexeos.json()['lowestAsk']

def braziliex_bch():
    braziliexbch = requests.get('https://braziliex.com/api/v1/public/ticker/bch_brl')
    return braziliexbch.json()['lowestAsk']

def braziliex_btg():
    braziliexbtg = requests.get('https://braziliex.com/api/v1/public/ticker/btg_brl')
    return braziliexbtg.json()['lowestAsk']

def braziliex_omg():
    braziliexomg = requests.get('https://braziliex.com/api/v1/public/ticker/omg_brl')
    return braziliexomg.json()['lowestAsk']

def braziliex_zec():
    braziliexzec = requests.get('https://braziliex.com/api/v1/public/ticker/zec_brl')
    return braziliexzec.json()['lowestAsk']

def braziliex_crw():
    braziliexcrw = requests.get('https://braziliex.com/api/v1/public/ticker/crw_brl')
    return braziliexcrw.json()['lowestAsk']

def braziliex_gnt():
    braziliexgnt = requests.get('https://braziliex.com/api/v1/public/ticker/gnt_brl')
    return braziliexgnt.json()['lowestAsk']

def braziliex_xrp():
    braziliexxrp = requests.get('https://braziliex.com/api/v1/public/ticker/xrp_brl')
    return braziliexxrp.json()['lowestAsk']

def braziliex_etc():
    braziliexetc = requests.get('https://braziliex.com/api/v1/public/ticker/etc_brl')
    return braziliexetc.json()['lowestAsk']

while True:
    braziliexliveusdt = float(braziliex_usdt())
    braziliexlivebtc = float(braziliex_btc())
    braziliexliveeth = float(braziliex_eth())
    braziliexliveltc = float(braziliex_ltc())
    #braziliexlivemxt = float(braziliex_mxt())
    #braziliexlivesngls = float(braziliex_sngls())
    #braziliexlivetrx = float(braziliex_trx())
    braziliexlivexmr = float(braziliex_xmr())
    #braziliexlivebtg = float(braziliex_btg())
    #braziliexliveeos = float(braziliex_eos())
    braziliexlivebch = float(braziliex_bch())
    #braziliexliveomg = float(braziliex_omg())
    braziliexlivezec = float(braziliex_zec())
    #braziliexlivecrw = float(braziliex_crw())
    #braziliexlivegnt = float(braziliex_gnt())
    braziliexlivexrp = float(braziliex_xrp())
    #braziliexliveetc = float(braziliex_etc())

    print ('###################--BRAZILIEX--########################')

    print ('BTC = BRL',braziliexlivebtc)
    print ('ETH = BRL',braziliexliveeth)
    print ('LTC = BRL',braziliexliveltc)
    print ('XRP = BRL',braziliexlivexrp)
    print ('BCH = BRL',braziliexlivebch)
    print ('XMR = BRL',braziliexlivexmr)
    #print ('BTG = BRL',braziliexlivebtg)
    #print ('SNG = BRL',braziliexlivesngls)
    #print ('TRX = BRL',braziliexlivetrx)
    print ('ZEC = BRL',braziliexlivezec)
    #print ('EOS = BRL',braziliexliveeos)
    #print ('OMG = BRL',braziliexliveomg)
    #print ('ETC = BRL',braziliexliveetc)
    #print ('GNT = BRL',braziliexlivegnt)
    time.sleep(60)




