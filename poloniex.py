
import requests
import json
#requisicao = requests.get('https://poloniex.com/public?command=returnTicker')
#cotacao = json.loads(requisicao.text)
#print(cotacao['BTC_BCN']['last'])
#print(cotacao['BTC_BCN']['lowestAsk'])
#print(cotacao['BTC_BCN']['highestBid'])

def poloniex_btc_last():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['USDT_BTC']['last']

def poloniex_btc_ask():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['USDT_BTC']['lowestAsk']

def poloniex_btc_bid():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['USDT_BTC']['highestBid']

def poloniex_dash():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['USDT_DASH']['last']

def poloniex_ltc():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['USDT_LTC']['last']

def poloniex_nxt():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['USDT_NXT']['last']

def poloniex_zrx():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['BTC_ZRX']['last']

def poloniex_eos():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['USDT_EOS']['last']

def poloniex_omg():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['BTC_OMG']['last']

def poloniex_xmrbtc():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['BTC_XMR']['last']

def poloniex_xmr():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['USDT_XMR']['last']

def poloniex_xrp():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['USDT_XRP']['last']

def poloniex_eth():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['USDT_ETH']['last']

def poloniex_ethbtc():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['BTC_ETH']['last']

def poloniex_etcbtc():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['BTC_ETC']['last']

def poloniex_etc():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['USDT_ETC']['last']

def poloniex_ethetc():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['ETH_ETC']['last']

def poloniex_rep():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['USDT_REP']['last']

def poloniex_repbtc():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['BTC_REP']['last']

def poloniex_repeth():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['ETH_REP']['last']
def poloniex_zecbtc():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['BTC_ZEC']['last']
def poloniex_zeceth():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['ETH_ZEC']['last']
def poloniex_zec():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['USDT_ZEC']['last']
def poloniex_gntbtc():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['BTC_GNT']['last']
def poloniex_ethgnt():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['ETH_GNT']['last']
def poloniex_bchbtc():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['BTC_BCH']['last']
def poloniex_bcheth():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['ETH_BCH']['last']
def poloniex_bch():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['USDT_BCH']['last']
def poloniex_eosbtc():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['BTC_EOS']['last']
def poloniex_eoseth():
    poloniextick = requests.get("https://poloniex.com/public?command=returnTicker")
    return poloniextick.json()['ETH_EOS']['last']

print('--------------COTAÇÕES POLONIEX--------------')
poloniexliveeoseth = float(poloniex_eoseth())
print('EOS/ETH last',poloniexliveeoseth)
poloniexliveeosbtc = float(poloniex_eosbtc())
print('EOS/BTC last',poloniexliveeosbtc)
poloniexlivebch = float(poloniex_bch())
print('BCH/USDT last',poloniexlivebch)
poloniexlivebcheth = float(poloniex_bcheth())
print('BCH/ETH last',poloniexlivebcheth)
poloniexlivebchbtc = float(poloniex_bchbtc())
print('BCH/BTC last',poloniexlivebchbtc)
poloniexliveethgnt = float(poloniex_ethgnt())
print('GNT/ETH last',poloniexliveethgnt)
poloniexlivebtcgnt = float(poloniex_gntbtc())
print('BTC/GNT last',poloniexlivebtcgnt)
poloniexlivezec = float(poloniex_zec())
print('ZEC/USDT last',poloniexlivezec)
poloniexlivezeceth = float(poloniex_zeceth())
print('ETH/ZEC last',poloniexlivezeceth)
poloniexlivezecbtc = float(poloniex_zecbtc())
print('BTC/ZEC last',poloniexlivezecbtc)
poloniexliverepeth = float(poloniex_repeth())
print('ETH/REP last',poloniexliverepeth)
poloniexliverepbtc = float(poloniex_repbtc())
print('REP/BTC last',poloniexliverepbtc)
poloniexliverep = float(poloniex_rep())
print('REP/USDT last',poloniexliverep)
poloniexliveethetc = float(poloniex_ethetc())
print('ETC/ETH last',poloniexliveethetc)
poloniexliveetc = float(poloniex_etc())
print('ETC/USDT last',poloniexliveetc)
poloniexliveetcbtc = float(poloniex_etcbtc())
print('ETC/BTC last',poloniexliveetcbtc)
poloniexliveethbtc = float(poloniex_ethbtc())
print('ETH/BTC last',poloniexliveethbtc)
poloniexliveeth = float(poloniex_eth())
print('ETH/USDT last',poloniex_eth())
poloniexlivexrp = float(poloniex_xrp())
print('XRP/USD last',poloniexlivexrp)
poloniexlivexmr = float(poloniex_xmr())
print('XMR/USD last',poloniexlivexmr)
poloniexlivexmrbtc = float(poloniex_xmrbtc())
print('XMR/BTC last',poloniexlivexmrbtc)
poloniexliveomg = float(poloniex_omg())
print('OMG/BTC last',poloniexliveomg)
poloniexliveeos = float(poloniex_eos())
print('EOS/USDT last',poloniexliveeos)
poloniexlivezrx = float(poloniex_zrx())
print('ZRX/BTC Last',poloniexlivezrx)
poloniexlivenxt = float(poloniex_nxt())
print('NXT/USDT  last',poloniexlivenxt)

poloniexliveltc = float(poloniex_ltc())
print('LTC/USDT  last',poloniexliveltc)
poloniexlivedash = float(poloniex_dash())
print('DASH/USDT last',poloniexlivedash)
poloniexlivebtclast = float(poloniex_btc_last())
print('BTC/USDT  Last',poloniexlivebtclast)
poloniexlivebtcask = float(poloniex_btc_ask())
#print('BTC_USDT  Ask',poloniexlivebtcask)
poloniexlivebtcbid = float(poloniex_btc_bid())
#print('BTC_USDT  Bid',poloniexlivebtcbid)
